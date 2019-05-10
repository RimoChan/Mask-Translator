import requests
import json
import os
import re

if os.path.isfile('./資料/緩存詞典.json'):
    with open('./資料/緩存詞典.json', encoding='utf8') as f:
        緩存詞典 = json.load(f)
else:
    緩存詞典 = {}

s = requests.Session()

def 解釋(單詞):
    if 單詞 in 緩存詞典:
        return 緩存詞典[單詞]

    print(f'上網查找「{單詞}」')
    url = f'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?oncomplete=mycallback&appId=A4D660A48A6A97CCA791C34935E4C02BBB1BEC1C&from=zh-cn&to=en&text={單詞}'

    回應 = s.get(url=url)
    assert 回應.status_code == 200
    text = 回應.text
    結果 = re.findall('mycallback\("(.*?)"\)', text)
    assert len(結果) == 1
    緩存詞典[單詞] = 結果[0]
    return 結果[0]

def 回寫():
    with open('./資料/緩存詞典.json', 'w', encoding='utf8') as f:
        json.dump(緩存詞典, f, ensure_ascii=False)
