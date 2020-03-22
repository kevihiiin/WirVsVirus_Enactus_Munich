import pgeocode


# this method takes a list of hospitals and a list of helpers and returns a dictionary,
# containing of hospitals as keys and a list of helpers as values
def match(hospitals, helpers):
    # initial setup for GeoDistance
    dist = pgeocode.GeoDistance('DE')

    # output dictionary which will be returned by the method
    # keys are hospitals, values are lists of helpers that are within range
    matching_results = {}
    # the method is triggered when a hospital poses an inquiry
    # this is why we can do it from the perspective of each hospital individually
    for hospital in hospitals:
        # adding an empty list for the hospital
        matching_results[hospital.id] = []
        # going through all of the helpers
        for helper in helpers:
            # obtaining the distance between the hospital and the helper
            distance = dist.query_postal_code(hospital.post_code, helper.post_code)
            # if the helper is within distance, he gets added to the list
            if distance < helper.radius:
                matching_results[hospital.id].append(helper.id)
    return matching_results
