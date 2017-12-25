#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime

#browser = webdriver.Firefox()
#browser = webdriver.Chrome()

# HEADLESSブラウザに接続
browser = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

# スクリーンショットのファイル名用に日付を取得
dt = datetime.datetime.today()
dtstr = dt.strftime("%Y%m%d%H%M%S")

# Googleにアクセス
browser.get('https://www.google.co.jp/')

# スクリーンショット
browser.save_screenshot('images/' + dtstr + '.png');

# 終了
browser.close()

