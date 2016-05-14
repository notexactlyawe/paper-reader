import urllib.request
import urllib.parse
import re

def get_youtube_url(query):

    text_file = open("KhanVids.txt", "r")
    lines = text_file.read().split(',')
    for x in range(0, len(lines)):
        if x % 2 != 0:
            lines[x] = lines[x].replace('-',' ')
            if query in lines[x]:
                return ("https://www.youtube.com/embed/" + lines[x-1])

    query_string = urllib.parse.urlencode({"search_query": query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return("https://www.youtube.com/embed/" + search_results[0])

print(get_youtube_url("measuring volume"))