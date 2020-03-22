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


def send_mail_participant(helper, institution):
    template = """
    Hallo {},\n
    \n
    herzlich willkommen bei Virushelfer.\n
    Wir danken dir für dein Interesse.\n
    {}\n
    \n
    \n
    Hier haben wir einige Tipps für dich:\n
    \n
    Wenn du im Patientenkontakt arbeitest: Lass dir unbedingt eine Hygieneeinweisung vor Ort geben und lerne die Station kennen, um dann besser und sicherer arbeiten und helfen zu können. Versuche gerade solange nicht so viel zu tun ist, herauszufinden, wo auf deiner Station was liegt, um später schneller helfen zu können, wenn etwas benötigt wird.\n
    \n
    Tue nichts, womit du dir nicht sicher bist und spreche im Zweifelsfall das Pflegepersonal oder auch die Personalleitung an!\n
    \n
    Das genaue Anstellungsverhältnis ist sehr unterschiedlich, informiere dich bitte an deinem ersten Tag in deinem Krankenhaus, wie es mit Vergütung oder mit der Anerkennung als Praktikum für dein Studium oder ähnliches aussieht, wir hoffen, dass die Universitäten hier recht kulant sein werden.\n
    \n
    Am ersten Tag mitbringen:\n
    - Impfnachweis (Masern, Tetanus, Hepatitis A;B, Diphtherie, Pertussis , Tetanus), wenn vorhanden\n
    - ggf. aktuelle Immatrikulationsbescheinigung oder Nachweis der abgeschlossenen Berufsausbildung \n
    - feste Schuhe\n
    \n
    Und auch an dieser Stelle noch einmal der Hinweis: solltest du eine der folgenden Gruppen angehören, teilt dies unbedingt vorab der Klinik mit:  \n
    Aufenthalt in Hochrisikogebieten nach RKI in den letzten 2 Wochen \n
    Kontakt zu CoVID19-Infizierten oder Verdachtsfällen in den letzten 2 Wochen \n
    Zugehörigkeit zu einer Risikogruppe (Personen über 50 Jahre, Schwangere, Vorerkrankungen)\n
    \n
    Danke für deine Teilnahme :)\n
    Schöne Grüße und bleib gesund,\n
    dein Team von Virushelfer\n
        """

    hospital_notice = 'Leider benötigt gerade kein Krankenhaus deine Hilfe, aber wir melden uns bei dir, sobald wir ein Match für dich gefunden haben' if institution is None else f'Das folgende Krankenhaus benötigt deine Hilfe: {institution.name}'

    message = template.format(f'{helper.first_name} {helper.last_name}', hospital_notice)
    return send_mail(helper.e_mail, message)

def send_mail_inquiry(institution):
    template = """
Sehr geehrte/r Herr/Frau {},

vielen Dank für die Registrierung der Institution {}.

Sobald Helfer gefunden wurden, die den Anforderungen entsprechen, werden wir Sie umgehend benachrichten.

Bis dahin wünschen wir viel Erfolg im Kampf gegen COVID-19.

Schöne Grüße
das Virushelden Team
    """
    message = template.format(institution.last_name_contact, institution.name)
    return send_mail(institution.e_mail, message)

def send_mail(e_mail, message):
    # mail setup
    # set up the SMTP server
    s = smtplib.SMTP(host='mail.example.net', port=587)
    s.starttls()
    s.login('virushelden@example.de', 'xxxxxxxxxxxxx')

    msg = MIMEMultipart()  # create a message

    # setup the parameters of the message
    msg['From'] = 'virushelden@example.de'
    msg['To'] = e_mail
    msg['Subject'] = "Deine Anmeldung bei Virushelden"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()
