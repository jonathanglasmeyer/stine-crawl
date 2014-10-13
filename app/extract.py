from bs4 import BeautifulSoup
from collections import defaultdict
from collections import OrderedDict

def extract(html_raw):
    soup = BeautifulSoup(html_raw)
    result = []

    for item in soup.find_all('div', class_='tbMonthDay'):
        date_div = item.find('div', class_='tbsubhead')
        if date_div:
            date = date_div.a.get('title')
            events_formatted = []
            for event in item.find_all('div', class_='appMonth'):
                events_formatted.append(event.a.get('title').encode('utf8', 'replace'))
            result.append((date, events_formatted))


    return result
