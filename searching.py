from search_engine_parser import GoogleSearch
import sys
input1 = sys.argv[1]
def google( query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    for every in gresults:
        print(every)

#print(google('python program for fibonacci series'))
print(google(input1))


