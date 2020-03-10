import os
import re
import requests
import logging

import yaml
from pathlib import Path


此處 = os.path.dirname(os.path.abspath(__file__))


緩存詞典 = {}
if os.path.isfile(Path(此處) / '_詞典緩存.yaml'):
    with open(Path(此處) / '_詞典緩存.yaml', encoding='utf8') as f:
        緩存詞典 = yaml.safe_load(f)

鎖定詞典 = {}
if os.path.isfile('translator.lock.yaml'):
    with open('translator.lock.yaml', encoding='utf8') as f:
        鎖定詞典 = yaml.safe_load(f)

自定詞典 = {}
if os.path.isfile('translator.custom.yaml'):
    with open('translator.custom.yaml', encoding='utf8') as f:
        自定詞典 = yaml.safe_load(f)


s = requests.Session()


def 解釋(單詞):
    if 單詞 in 自定詞典:
        return 自定詞典[單詞]
    if 單詞 in 鎖定詞典:
        return 鎖定詞典[單詞]
    if 單詞 in 緩存詞典:
        鎖定詞典[單詞] = 緩存詞典[單詞]
        return 緩存詞典[單詞]

    logging.info(f'上網查找「{單詞}」')
    url = f'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?oncomplete=mycallback&appId=A4D660A48A6A97CCA791C34935E4C02BBB1BEC1C&from=zh-cn&to=en&text={單詞}'

    回應 = s.get(url=url)
    assert 回應.status_code == 200
    text = 回應.text
    結果 = re.findall('mycallback\("(.*?)"\)', text)
    if len(結果) != 1:
        raise Exception(f'上網的回應爲「{text}」')

    緩存詞典[單詞] = 結果[0]
    鎖定詞典[單詞] = 結果[0]
    return 結果[0]


def 全部回寫():
    with open(Path(此處) / '_詞典緩存.yaml', 'w', encoding='utf8') as f:
        yaml.dump(緩存詞典, f, allow_unicode=True)
    with open('translator.lock.yaml', 'w', encoding='utf8') as f:
        yaml.dump(鎖定詞典, f, allow_unicode=True)
