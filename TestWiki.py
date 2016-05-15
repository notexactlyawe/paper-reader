from havenondemand.hodclient import *
import wikipedia

client = HODClient("8450e15b-c583-46c7-b25e-5ce758140646", version="v1")

def get_filtered_analysis(title, location, is_file):
    a = analysis(location, is_file)
    bPage = wikipedia.page(wikipedia.search(title)[0])
    b = analysis(bPage.url, False)
    return filter (a,b)


def analysis(location, is_file):
    response = client.get_request({"url": location}, HODApps.EXTRACT_CONCEPTS, async=False) if not is_file else \
        client.post_request({"file": location}, HODApps.EXTRACT_CONCEPTS, async=False)
    return response["concepts"] if response is not None else "No results returned"

def similar(location, is_file):
    response = client.get_request({"url": location}, HODApps.FIND_SIMILAR, async=False) if not is_file else \
        client.post_request({"file": location}, HODApps.FIND_SIMILAR, async=False)
    return response["documents"] if response is not None else "No results returned"

def filter(a, b):
    temp_concepts = []
    for x in range (0, len(a)):
        for y in range (0, len(b)):
            if(a[x]['concept'] == b[y]['concept'] or a[x]['occurrences'] > 5):
                if(len(a[x]['concept']) > 3):
                    temp_concepts.append(a[x]['concept'])
    return list(set(temp_concepts))

#print(get_filtered_analysis("An Industrial-Strength Audio Search Algorithm", "http://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf", False))
#print(similar("http://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf", False))