import shortuuid


def generate_uri():
    """
    Generate the 6-letter URI from a namespace
    """
    return shortuuid.ShortUUID(alphabet="123456789").random(length=6)
