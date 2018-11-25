from google import google

"""Search on Google with given query argument

Returns:
    Array -- Query Results Array(Name, Link, Desc)
"""

def search_query(query, page):
    urls = []

    search_results = google.search(query, page)
    for result in search_results:
        name = result.name
        link = result.link
        desc = result.description
        
        urls.append([name, link, desc])
     
    return urls
