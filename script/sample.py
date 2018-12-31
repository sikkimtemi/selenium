#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime

def execSearch(browser: webdriver):
    """
    Googleで検索を実行する
    :param browser: webdriver
    """
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # Googleにアクセス
    browser.get('https://www.google.co.jp/')
    sleep(1)

   # キーワードの入力
    search_box = browser.find_element_by_name("q")
    search_box.send_keys('docker selenium')

    # 検索実行
    search_box.submit()
    sleep(1)

    # スクリーンショット
    browser.save_screenshot('images/' + dtstr + '.png')


if __name__ == '__main__':
    try:
        #browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        #browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Googleで検索実行
        execSearch(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()

