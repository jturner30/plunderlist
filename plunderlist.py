import requests
import json
import os
from collections import defaultdict

access_token = os.environ.get('WUNDERLIST_ACCESS_TOKEN')
client_id = os.environ.get('WUNDERLIST_CLIENT_ID')
headers = {'X-Access-Token': access_token, 'X-Client-ID': client_id}
sep = u'\u2502'
last_bar = u'\u2514\u2500\u2500'
bar = u'\u251c\u2500\u2500'

lists_url = 'http://a.wunderlist.com/api/v1/lists'
tasks_url = 'https://a.wunderlist.com/api/v1/tasks'

def get_lists():
    response = requests.get(lists_url, headers=headers)
    return response.json()


def get_tasks_for_list(list_id):
    response = requests.get(tasks_url, headers=headers, params={'list_id': list_id})
    return response.json()


def get_list_id_title_pairs(lists):
    return map(lambda x: (x.get('id'), x.get('title')), lists)


def get_tasks_titles(tasks):
    return map(lambda x: x.get('title'), tasks)


def build_task_list():
    lists = get_lists()
    pairs = get_list_id_title_pairs(lists)
    d = defaultdict(list)
    for _id, title in pairs:
        tasks = get_tasks_for_list(_id)
        d[title] = get_tasks_titles(tasks)
    return d


def print_task_list():
    d = build_task_list()
    i = 0
    for key, value in d.iteritems():
        pc = last_bar if i == len(d) - 1 else bar
        print pc + key
        for index, v in enumerate(value):
            pcc = last_bar if index == len(value) - 1 else bar
            _sep = '' if i == len(d) - 1 else sep
            print _sep + ' ' * 4 + pcc + v
        i += 1


def add_task_to_list(list_id, task_title):
    headers['Content-Type'] = 'application/json'
    r = requests.post(tasks_url, headers=headers, data=json.dumps({'list_id': list_id, 'title': task_title}))
    headers.pop('Content-Type')
    return r


if __name__ == '__main__':
    main()
