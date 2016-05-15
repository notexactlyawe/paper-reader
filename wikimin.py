import wikipedia


def get_summary(name, sen):
    try:
        return wikipedia.summary(name, sentences=sen)
    except wikipedia.exceptions.DisambiguationError as e:
        return get_summary(e.options[0], sen)