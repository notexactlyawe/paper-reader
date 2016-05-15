import wikipedia


def get_summary(name, sen):
    return wikipedia.summary(name, sentences=sen)

