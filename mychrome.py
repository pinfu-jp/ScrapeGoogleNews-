from selenium import webdriver
import os

class MyChrome:

    _driver: webdriver.Chrome = None
    _options = webdriver.ChromeOptions()

    LOCAL_CHROME_DRIVER_EXE = "C:\\devtool\\chromedriver_win32\\chromedriver.exe"
    # chromedriver.exe は事前にインストールが必要です
    # https://chromedriver.chromium.org/downloads から取得してください

    def __init__(self, headlessMode = True) -> None:

        if headlessMode:
            self._options.add_argument('--headless')
            self._options.add_argument('--no-sandboc')
            self._options.add_argument('--disable-dev-shm-usage')

        assert os.path.isfile(self.LOCAL_CHROME_DRIVER_EXE)

        super().__init__()

    # Chrome起動
    def launch(self, wait_sec:int = 30) -> webdriver:
        self._driver = webdriver.Chrome(MyChrome.LOCAL_CHROME_DRIVER_EXE, options=self._options)

        # ロードのタイムアウトを長めにしておく
        self._driver.implicitly_wait(wait_sec)

        return self._driver
