import unittest
from searchInGoogleNews import search_in_google_news

# ユニットテスト
class TestSearchGoogleNews(unittest.TestCase):

    _result_path = 'result.json'

    def test_search_in_google_news_for_debug(self):
        print('Chrome表示状態でテスト')
        keyword = 'iOS'
        search_in_google_news(keyword, self._result_path, False)


if __name__ == '__main__':
    unittest.main()