import requests


def intell_request(name, token):
    url = f'https://superheroapi.com/api/{token}/search/{name}'
    request = requests.get(url)
    item = request.json()
    intelligence = item['results'][0]['powerstats']['intelligence']
    return intelligence


if __name__ == '__main__':
    names = ['Hulk', 'Captain America', 'Thanos']
    list_intell = []
    for name in names:
        intelligence = intell_request(name, '2619421814940190')
        if not list_intell:
            list_intell.append([name, int(intelligence)])
        else:
            if int(intelligence) > list_intell[0][1]:
                list_intell.clear()
                list_intell.append([name, int(intelligence)])
            elif int(intelligence) == list_intell[0][1]:
                list_intell.append([name, int(intelligence)])
            else:
                pass
    if len(list_intell) == 1:
        print(f'Самый умный супергерой - {list_intell[0][0]}')
    elif len(list_intell) > 1:
        print('Умнейшие супергерои:')
        print(*[x[0] for x in list_intell], sep=', ', end='.')
