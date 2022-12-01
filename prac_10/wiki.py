"""
CP1404 Practical - Wikipedia API
by: Rory Reid
"""

import wikipedia

page_search = input(">>> ")
while page_search != "":
    try:
        page = wikipedia.page(page_search, auto_suggest=False)
        print(page.title)
        print()
        print("Summary:")
        print(page.summary)
        print()
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Too generic, too many pages returned, please be more specific")
        print(e.options)
    page_search = input(">>> ")
