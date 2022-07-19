import requests, json

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "language_code=en;",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

iknow_courses = {
    '1k': [566921,566922,566924,566925,566926,566927,566928,566929,566930,566932],
    '2k': [594768,594770,594771,594772,594773,594774,594775,594777,594778,594780],
    '3k': [615865,615866,615867,615869,615871,615872,615873,615874,615876,615877],
    '4k': [615947,615949,615950,615951,615953,615954,615955,615957,615958,615959],
    '5k': [616077,616078,616079,616080,616081,616082,616083,616084,616085,616086],
    '6k': [598434,598432,598431,598430,598427,598426,598425,598424,598423,598422]
}

items_count, sentences_count = 0, 0
for k, vals in iknow_courses.items():
    for v in vals:
        resp = requests.get(f'https://iknow.jp/api/v2/goals/{v}', headers=headers)
        ret = json.loads(resp.content)

        pid = ret['id']
        title = ret['title'].replace(':', '').replace(' ', '')

        items_count += ret['items_count']
        sentences_count += ret['sentences_count']

        key = f'{title}_{pid}'
        print(f'>>>>> {key} {items_count} {sentences_count}')

        res = {}
        res[key] = ret
        with open('iknowJP.txt', 'a') as f:
            f.write(',')
            json.dump(res, f, indent=1)

print(f'Finish! items_count: {items_count} sentences_count:{sentences_count}')
