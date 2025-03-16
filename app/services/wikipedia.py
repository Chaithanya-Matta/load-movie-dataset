import wikipediaapi

USER_AGENT = "MovieSearchBot/1.0 (m.manasmatta@gmail.com)"
wiki_wiki = wikipediaapi.Wikipedia(language="en", user_agent=USER_AGENT)

def wiki_search(movie_name: str, movie_year: str):
    # page = wiki_wiki.page(f"{movie_name}_(film)")
    page = wiki_wiki.page(f"{movie_name}_({movie_year}_film)")

    # print(page)

    if page.exists():
        return page.sections[0].text
    else:
        return ""