import re
import json
import opencc
import keyword

import 詞義

cc = opencc.OpenCC('t2s')

替換表 = {}
反向替換表 = {}
for i in keyword.kwlist:
    反向替換表[i] = '*關鍵字'

def 改變形態(單詞):
    單詞 = re.sub('[ \-\,\.]','_',單詞)
    單詞 = re.sub('(^_|_$)','',單詞)
    return 單詞.lower()

def 翻譯(單詞):
    return 改變形態(詞義.解釋(單詞))

def 替換(單詞):
    單詞=單詞.group(0)
    if 單詞[0] in ["'",'"']:
        return 單詞
    if 單詞 in 替換表: 
        return 替換表[單詞]
    結果 = 翻譯(cc.convert(單詞))
    替換表[單詞] = 結果
    if 結果 in 反向替換表:
        raise Exception(f'試圖把「{單詞}」翻譯爲「{結果}」，但是「{結果}」已經被「{反向替換表[結果]}」佔用了。')
    反向替換表[結果] = 單詞
    return 結果

def 處理(文): 
    結果 = re.sub(r'''".*?"|'.*?'|[\u4E00-\u9FFF]+''',替換,文)
    詞義.回寫()
    return 結果
    
if __name__=='__main__':
    print(處理('''
class 貓耳幼女:
    def __init__(self):
        self.喵喵喵()
    def 喵喵喵(self):
        print(f'貓耳幼女: "喵喵喵！"')
    '''))
