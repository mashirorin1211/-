import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSdA7zvkjA7c06EGgEgOioUj-NqAIw_B2vqYwJwF7giBUo0S8g/formResponse'
params = ['0天', '1~3天', '3天以上']
params_2 = ['讀書','討論報告','吃飯','休息聊天']
params_3 = ['茶水區', '討論室','化妝室','沙發區']
params_4 = ['整體照明不足，太昏暗','沙發區電燈設計不佳']
params_5 = ['1','2','3','4','5']
parmas_6 =['插座','廁所衛生紙']

payload = {
    'entry.1286125667' : '',
    'entry.1208597069' : '',
    'entry.1090418866' : '',
    'entry.860585977' : '',
    'entry.1118603301' : '',
    'entry.1696819481' : '',
    'fvv' : '0',
    'draftResponse' : '[]',
    'pageHistory' : '0',
    'fbzx' : '1431842163172551877'
}
num = 500
period = np.arange(0.5, 5.0, 0.1)
delay = 0
while num > 0:
    try:
        payload['entry.1286125667'] = random.choice(params)
        payload['entry.1208597069'] = random.choice(params_2)
        payload['entry.1090418866'] = random.choice(params_3)
        payload['entry.860585977'] = random.choice(params_4)
        payload['entry.1118603301'] = random.choice(params_5)
        payload['entry.1696819481'] = random.choice(parmas_6)
        res = rq.post(url, data=payload)
        res.raise_for_status()
        if res.status_code == 200:
            delay = round(random.choice(period), 2)
            print('Fill Out : ' + payload['entry.1286125667'] + payload['entry.1208597069'] + payload['entry.1090418866']+payload['entry.860585977']+ payload['entry.1118603301']+payload['entry.1696819481']+' delay : ' + str(delay) + ' sec')
            time.sleep(delay)
    except rq.HTTPError:
        print('HTTP Error!')

    num -= 1
