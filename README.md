# Gartic 自定義題庫

在Gartic.io之中，自動選擇create theme，自動輸入已經準備好的題目。

## 環境設置

Python 3.8.5
selenium 3.141.0
[ChromeDriver 87.0.4280.20 linux 64](https://chromedriver.chromium.org/)

## 題目

範例：

* [神奇寶貝圖鑑](https://github.com/patrick0314/Gartic_auto_create_theme/blob/main/pokemon.txt)
* [華語流行歌曲](https://github.com/patrick0314/Gartic_auto_create_theme/blob/main/song.txt)

並非一定要只有題目，可以有其他多餘資訊，方便大家從其他地方直接複製過來。唯一要注意的點是每行一個題目，並且題目都是在其行的固定位置。

下圖神奇寶貝圖鑑中，題目是神奇寶貝的名稱，就固定是在每一行的第二個項目；流行音樂中，題目是歌曲名稱，就固定是在每一行的第五個項目。

| 神奇寶貝圖鑑 | 華語流行歌曲|
| -------- | -------- |
| ![](https://i.imgur.com/TpJ8qVw.png) | ![](https://i.imgur.com/NQaTlqW.png) |

## 執行程式

[source code](https://github.com/patrick0314/Gartic_auto_create_theme/blob/main/gartic.py)

執行檔案須有附加的參數，如下圖。

![](https://i.imgur.com/xM5KqeE.png)

* email: 登入facebook時所需要的email
* password: 登入facebook時所需要的password
* classification: 創建主題時，需要定義題目類型，詳情見下圖
* file: 放置題目的檔案，最好是txt檔
* idx: 題目檔案中，題目的位置。舉例像是神奇寶貝圖鑑檔案中，題目是在第二個項目，因為python是從0開始，因此輸入1；流行音樂中，題目是在第五個項目， 因此輸入4

題目類型的value：

![](https://i.imgur.com/ILPahEN.png)

## Demo

用神奇寶貝圖鑑舉例

```Vim
python3 gartic.py test@gmail.com password 7 pokemon.txt 1
```

執行後會出現一個chrome視窗，會先自動登入FB，然後登入Gartic，開始創建主題，然後關閉視窗。

之後自行登入Gartic，即可看見創建主題。

[demo video](https://www.youtube.com/watch?v=3N0nraxgUNI&ab_channel=%E9%BB%83%E7%85%9C%E5%A0%AF)
