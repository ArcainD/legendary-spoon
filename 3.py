import requests
import time
from pprint import pprint


def request(page_num, fromdate, todate, tag):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'fromdate': fromdate,
        'todate': todate,
        'sort': 'creation',
        'order': 'desc',
        'tagged': tag,
        'site': 'stackoverflow',
        'page': page_num
    }
    response = requests.get(url=url, params=params)
    data = response.json()
    return data


def questions(data, list_responses):
    for i in range(len(data['items'])):
        creation_date = data['items'][i]['creation_date']
        title = data['items'][i]['title']
        list_responses.append([creation_date, title])
    has_more = data['has_more']
    return has_more


if __name__ == '__main__':
    page_num = 1
    fromdate = '2021-11-01'      # в формате yyyy-mm-dd hh:mm:ss время сервера -03:00 относительно МСК
    todate = '2021-11-03'        # в формате yyyy-mm-dd hh:mm:ss
    tag = 'python'
    has_more = True
    list_responses = [['creation_date', 'title']]
    while has_more:
        data = request(page_num, fromdate, todate, tag)
        has_more = questions(data, list_responses)
        time.sleep(0.2)
        page_num += 1
    pprint(list_responses)


