"""
Scrap first and second page of hacker news.
"""

import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
convert = BeautifulSoup(response.text, 'html.parser')
convert2 = BeautifulSoup(response2.text, 'html.parser')

links = convert.select('.storylink')
subtext = convert.select('.subtext')
links2 = convert2.select('.storylink')
subtext2 = convert2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['scores'], reverse=True)
    # Sorts the hacker-news list out with votes/points at the top


def custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = item.getText()  # title of the news article
        href = item.get('href', None)  # hyperlink of the article.
        up_scores = subtext[idx].select('.score')
        if len(up_scores):
            # checks that up_scores has a length
            points = int(up_scores[0].getText().replace(' points', ''))  # converts to an int and replaces the points text.
            if points > 49:
                # if an article has more than 49 points.
                hacker_news.append({'title': title, 'link': href, 'scores': points})  # put title and link into a dictionary.
    return sort_stories_by_votes(hacker_news)


pprint.pprint(custom_hacker_news(mega_links, mega_subtext))
