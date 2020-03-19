import re
import json
import opencc
import keyword

import 詞法分析
import 詞義

cc = opencc.OpenCC('t2s')

替換表 = {}
反向替換表 = {}
for i in keyword.kwlist:
    反向替換表[i] = '*關鍵字'


def 改變形態(單詞):
    單詞 = re.sub("[ \-\,\.\']", '_', 單詞)
    單詞 = re.sub('(^_|_$)', '', 單詞)
    return 單詞.lower()


def 翻譯(單詞):
    return 改變形態(詞義.解釋(單詞))


def 字符串替換(字符串):
    if 字符串[0] == 'f':
        結果 = re.sub(r'(?<={).*?(?=})', lambda x: 處理(x.group(0)), 字符串)
        return 結果
    else:
        return 字符串


def 單詞替換(單詞):
    if all([ord(i)<128 for i in 單詞]):
        return 單詞
    if 單詞 in 替換表:
        return 替換表[單詞]
    結果 = 翻譯(cc.convert(單詞))
    替換表[單詞] = 結果
    if 結果 in 反向替換表:
        raise Exception(f'試圖把「{單詞}」翻譯爲「{結果}」，但是「{結果}」已經被「{反向替換表[結果]}」佔用了。')
    反向替換表[結果] = 單詞
    return 結果
    

def 光寫(詞法組):
    for 類型, x in 詞法組:
        if 類型 == '符號':
            print(f'\033[1;32m{x}\033[0m', end='')
        if 類型 == '字':
            print(f'\033[1;34m{x}\033[0m', end='')
        if 類型 == '字符串':
            print(x, end='')


def 處理(s): 
    新詞法組 = 詞法分析.分析(s)
    for 組 in 新詞法組:
        類型, x = 組
        if 類型 == '字': 
            組[1] = 單詞替換(x)
        if 類型 == '字符串': 
            組[1] = 字符串替換(x)
    # 光寫(詞法分析.分析(s))
    # 光寫(新詞法組)
    詞義.全部回寫()
    return ''.join([x for 類型, x in 新詞法組])
    

if __name__ == '__main__':
    with open('test.py', encoding='utf8') as f:
        s = f.read()
    處理(s)
