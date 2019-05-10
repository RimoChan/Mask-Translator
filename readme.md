# 胡說八道的人

將中文代碼翻譯成英文的工具。

嘛，就是那個嘛……經常要交作業什麼的，然後中文代碼直接交上去也不太好，手工翻譯又麻煩，就弄了這樣的東西。

會調用bing翻譯把中文標識符都翻譯成英文的，因爲有本地緩存所以不會太消耗api的使用次數。   
(不過api居然是別人的……)

雖然代碼一般可以運行，但顯然沒法保證翻譯的準確度。   
所以會不會被老闆打成SB……只能聽天由命啦。

## 樣例

翻譯前: 

```python
class 貓耳幼女:
    def __init__(self):
        self.喵喵喵()
    def 喵喵喵(self):
        print('貓耳幼女: "喵喵喵"！')
    def 啪啪啪(self, 别的人):
        raise Exception('不能啪！')
    def 摸摸(self, 部位):
        print(f'{部位}很舒服。')
```

翻譯後: 

```python
class cat_ear_girl:
    def __init__(self):
        self.meow_meow()
    def meow_meow(self):
        print('貓耳幼女: "喵喵喵"！')
    def pop_snapping(self, someone_else):
        raise Exception('不能啪！')
    def touch(self, parts):
        print(f'{parts}很舒服。')
```

嗯……

`貓耳幼女` 的 `幼` 哪去了啊！

`喵喵喵` 真的不是少了一個嗎！

還有 `pop_snapping` 是什麼玩意！

## 使用方法

1.  安裝python3.6及以上版本
2.  `pip3 install requests opencc`
3.  `python3 翻譯.py` 或者 `python3 文件夾翻譯.py`

嗯……參數是寫死在 `__main__` 裏的所以要改成你自己的。

## 注意

+ 如果bing將多個中文翻譯成了同一個英文，或者翻譯成了關鍵字——本地會報錯所以不用擔心。

+ 翻譯後的代碼全部是小寫而且全部使用下劃線分割。

+ 顯然帶有反射的代碼是要出錯的。


## 有的毛病

+ 中文在翻譯後可能會和代碼裏的英文重複。

+ 中文接英文的時候不會添加下劃線。

+ 因爲字符串分析是隨便寫的，所以沒法識別多行字符串。

## 贊助

如果你覺得「胡說八道的人」對你的工作或學習有幫助，歡迎給作者贊助一些 `貓耳幼女` 或者 `cat_ear_girl` 。

(沒有 `貓耳幼女` 的話就會失去編程的能力，非常可怕所以一定要注意！)
