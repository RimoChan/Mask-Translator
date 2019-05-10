import os
import 翻譯

def 文件夾翻譯(路徑):
    assert os.path.isdir(路徑)
    
    try:
        os.mkdir(f'{路徑}/_翻譯')
    except:
        None
        
    for i in os.listdir(路徑):
        if i.endswith('.py'):
            with open(f'{路徑}/{i}',encoding='utf8') as f:
                結果 = 翻譯.處理(f.read())
            with open(f'{路徑}/_翻譯/{翻譯.處理(i)}','w',encoding='utf8') as f:
                f.write(結果)
            
if __name__=='__main__':
    文件夾翻譯('.')