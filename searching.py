from search_engine_parser import GoogleSearch

def google( query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    for every in gresults:
        print(every)

print(google('Is it illegal to scrape google results'))

