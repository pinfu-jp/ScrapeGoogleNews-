# ScrapeGoogleNews:Google News スクレイピング

- Webスクレイピングの学習用コードです
- [Google News](https://news.google.com/home) で検索した記事の「タイトル」とURLをJSONファイルに一覧表として出力します

# サンプルコード

## 実行コード

```python
from searchInGoogleNews import search_in_google_news

keyword = 'Android'
result_path = 'result.json'

# スクレイピング
search_in_google_news(keyword, result_path)

# 結果は 'result.json' に出力されます
```

## 出力結果

```json
{
  "ITmedia Mobile人気記事より：Androidスマホの弱点は「サポート期間」 改善は進むのか？（ITmedia Mobile） - Yahoo!ニュース": "https://news.google.com/articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy9lZjliYjU5YjMwNmE2NjdlNjU3OTRjODYwNzFhOWRmMmFkNzkyOTli0gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "今売れてるAndroidスマートフォンTOP10、au版Pixel 6aが8週連続首位 2022/11/5（BCN） - Yahoo!ニュース": "https://news.google.com/articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy8zYTY5ZGY4YThmOTU0ZDQwZTM3Y2Y4ZmU5NDBmNGY0OWIxNDhjYTFi0gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "BlackBerryみたい。Androidスマホの原型「Google G1」画像が明らかに（GetNavi web） - Yahoo!ニュース": "https://news.google.com/articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy9iYmZmOTQ2MzUxZmNjNjE3NzJmYTYxMGU5OWVhYmUzZDQ0YzBlZjkz0gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "「スマホは3年以上使う」時代だからこそ知っておきたい、AndroidスマホのOSアップデート事情（マイナビニュース） - Yahoo!ニュース": "https://news.google.com/articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy81NTZjNzBkNTJjNjljNDlhMTU5NjRmYzRjYzVkMjdmMjMwMTE2NGRh0gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "要注意！ Androidがハッキングされている5つの兆候（ライフハッカー［日本版］） - Yahoo!ニュース": "https://news.google.com/articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy83ZGJhNDY0NDY3ODFkMTcxY2Y3ZjdlYTRiNTY0ZWU0N2JhYjJmZTVj0gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "カーナビAndroid化。挿すだけでスマホ機能、進化したCarDongle2.0": "https://news.google.com/articles/CBMiKWh0dHBzOi8vY2FtcC1maXJlLmpwL3Byb2plY3RzL3ZpZXcvNjM1MjI50gEA?hl=ja&gl=JP&ceid=JP%3Aja",
  "Android 12搭載の10.1型タブレットがAmazonで2万円切り": "https://news.google.com/articles/CAIiEI6pROmKPoAEcWSlTfEKl9UqGQgEKhAIACoHCAowoaPwCjCL47cCMJfUhwM?uo=CAUiQmh0dHBzOi8vcGMud2F0Y2guaW1wcmVzcy5jby5qcC9kb2NzL25ld3MvdG9kYXlzX3NhbGVzLzE0NTA4ODIuaHRtbNIBAA&hl=ja&gl=JP&ceid=JP%3Aja",
  ...
}
```


# 実行環境

- Python Ver.3.9.7 で動作確認
- selenium, bs4(BeautifulSoup) が必要です

- Chrome Driver が必要です
  - https://chromedriver.chromium.org/downloads からダウンロードして以下に配置してください
    - C:\\devtool\\chromedriver_win32\\chromedriver.exe
     
