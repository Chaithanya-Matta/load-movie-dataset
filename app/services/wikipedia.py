import wikipediaapi

USER_AGENT = "MovieSearchBot/1.0 (m.manasmatta@gmail.com)"
wiki_wiki = wikipediaapi.Wikipedia(language="en", user_agent=USER_AGENT)

def wiki_search():
    page = wiki_wiki.page("Inception_(film)")

    if page.exists():
        return page.sections[0].text
    else:
        return ""