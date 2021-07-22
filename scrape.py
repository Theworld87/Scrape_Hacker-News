"""
Scrapes hacker-news website with article links and sorts the articles out by a votes/points system on their site.
For example, only articles over 49 points will be displayed.
"""
import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
convert = BeautifulSoup(response.text, 'html.parser')
links = convert.select('.storylink')
subtext = convert.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['scores'], reverse=True)
    # Sorts the hacker-news list out with votes/points at the top


def custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        up_scores = subtext[idx].select('.score')
        if len(up_scores):
            # checks that up_scores has a length
            points = int(up_scores[0].getText().replace(' points', ''))
            if points > 49:
                # if an article has more than 49 points.
                hacker_news.append({'title': title, 'link': href, 'scores': points})
                # put title and link into a dictionary to combine the data.
    return sort_stories_by_votes(hacker_news)


pprint.pprint(custom_hacker_news(links, subtext))
