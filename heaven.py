from havenondemand.hodclient import *

client = HODClient("8450e15b-c583-46c7-b25e-5ce758140646", version="v1")


def analysis(location, is_file):
    response = client.get_request({"url": location}, HODApps.EXTRACT_CONCEPTS, async=False) if not is_file else \
        client.post_request({"file": location}, HODApps.EXTRACT_CONCEPTS, async=False)
    return response["concepts"] if response is not None else "No results returned"


print analysis("http://www.gla.ac.uk/media/media_194538_en.pdf", False)
print analysis("/Users/joshuarichardson/Downloads/media_194538_en.pdf", True)
