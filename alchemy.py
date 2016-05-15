from alchemyapi import AlchemyAPI


def extract_nouns(text):
    alchemyapi = AlchemyAPI()
    response = alchemyapi.concepts("text", text)
    return str(response)
