# Mask-Translator: 假面翻譯！

將中文代碼翻譯成英文的工具。

嘛，就是那個嘛……經常要交作業什麼的，然後中文代碼直接交上去也不太好，手工翻譯又麻煩，就弄了這樣的東西。

會調用Bing翻譯把中文標識符都翻譯成英文的，因爲有本地緩存所以不會太消耗api的使用次數。   
(不過api居然是別人的……)


## 樣例

翻譯前: 

```python
class 貓耳幼女:
    def 推倒(self):
        print(f'推倒: {self.推倒}！')

貓耳幼女().推倒()
```

翻譯後: 

```python
class cat_eared_baby_girl:
    def down(self):
        print(f'推倒: {self.down}！')

cat_eared_baby_girl().down()
```

Mask Translator 真是太棒了！


## 使用方法

先在要翻譯的文件夾放置 `translator.config.yaml` ，決定哪些文件怎麼要處理。   
它應該像這樣——

```yaml
list_of_files_to_translate:
    - mask_change.py
    - 詞義.py
    - 翻譯.py
list_of_files_to_copy:
    - readme.md
    - LICENSE
```

然後——

1.  python3.6+
2.  pip install -r requirements.txt
3.  cd 要翻譯的文件夾
4.  python mask_change.py -o 輸出文件夾

這樣就會全部翻譯過去啦！


## 自定義

在翻譯之後，輸入文件夾的目錄下會生成文件 `translator.lock.yaml` ，這是翻譯記錄，保證下次翻譯的結果是一樣的。

如果你對某些翻譯的結果不滿，可以按同樣的格式寫一個 `translator.custom.yaml` ，他會覆蓋原本的翻譯。

比如像這樣——

```yaml
# translator.lock.yaml
猫耳幼女: Cat-eared baby girl
推倒: Down
```

```yaml
# translator.custom.yaml
推倒: Push down
```

之後 `推倒` 就會被翻譯成 `push_down` 。


## 注意

顯然用反射的代碼是要出錯的。


## 毛病

+ 中文在翻譯後可能會和代碼裏的英文重複。

+ 中文接英文的時候不會添加下劃線。

+ 因爲字符串分析是隨便寫的，所以沒法識別多行字符串。


## 贊助

如果你覺得 Mask Translator 對你的工作或學習有幫助，歡迎給作者贊助一些 `貓耳幼女` 。

(沒有 `貓耳幼女` 的話就會失去編程的能力，非常可怕所以一定要注意！)
