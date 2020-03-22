import pgeocode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# this method takes a list of inquiries and a list of helpers and returns a dictionary,
# containing inquiry ids as keys and a list of helpers as values
def match_all(inquiries, helpers):

    # initial setup for GeoDistance
    dist = pgeocode.GeoDistance('DE')

    # in order to distribute the helpers best, we sort them by skill level, so that hospitals with only basic needs
    # get basic helpers first
    helpers.sort(key=lambda x: x.skill_level)

    # output dictionary which will be returned by the method
    # keys are hospitals, values are lists of helpers that are within range
    matching_results = {}

    # list of helpers that are already assigned to a hospital
    assigned_helpers = []

    # the method is triggered when a hospital poses an inquiry
    # this is why we can do it from the perspective of each hospital individually
    for inquiry in inquiries:
        # adding an empty list for the hospital
        hospital = inquiry.hospital
        matching_results[inquiry.id] = []

        # going through all of the helpers
        for helper in helpers:

            # if the helper is already assigned, he shall not get assigned to a second hospital
            if helper.id in assigned_helpers:
                continue

            # if we have enough helpers for the inquiry, we can jump to the next one
            if len(matching_results[inquiry.id]) == inquiry.number_of_helpers:
                break

            # obtaining the distance between the hospital and the helper
            distance = dist.query_postal_code(hospital.post_code, helper.post_code)

            # if the helper is within distance, he gets added to the list
            # we are also checking if the level of the helper is equal or above what the inquiries needs
            if distance < helper.radius and inquiry.skill_level <= helper.skill_level:
                matching_results[inquiry.id].append(helper.id)
                assigned_helpers.append(helper.id)

    return matching_results


# this method takes a list of OPEN inquiries and a helper and returns an inquiry that will be assigned to that helper
def match_indiviual(inquiries, helper):
    # initial setup for GeoDistance
    dist = pgeocode.GeoDistance('DE')
    # checking if the helper is already assigned
    assigned_inquiry = None

    # the method is triggered when a hospital poses an inquiry
    # this is why we can do it from the perspective of each hospital individually
    for inquiry in inquiries:
        hospital = inquiry.hospital

        # obtaining the distance between the hospital and the helper
        distance = dist.query_postal_code(hospital.post_code, helper.post_code)

        # if the helper is within distance, he gets added to the list
        # we are also checking if the level of the helper is equal or above what the inquiries needs
        if distance < helper.radius and inquiry.skill_level <= helper.skill_level:
            assigned_inquiry = inquiry

        # if the helper is already assigned, he shall not get assigned to a second hospital
        if assigned_inquiry:
            return assigned_inquiry

    return None


def send_mail(helper):
    # mail setup
    # set up the SMTP server
    s = smtplib.SMTP(host='mail.gmx.net', port=587)
    s.starttls()
    s.login('virushelden@gmx.de', 'nedlehsuriV')

    msg = MIMEMultipart()  # create a message

    message = f"Hi {helper.first_name}, danke fürs Anmelden. Wenn du diese Mail bekommst, bsit du cool." \
              f"Schöne Grüße, deine Virushelden"

    # setup the parameters of the message
    msg['From'] = 'virushelden@gmx.de'
    msg['To'] = helper.e_mail
    msg['Subject'] = "Deine Anmeldung bei Virushelden"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

