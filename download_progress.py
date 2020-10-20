from selenium import webdriver
import time
import sys
if __name__ == '__main__':
    chrome_browser = webdriver.Chrome('./chromedriver.exe')
    chrome_browser.maximize_window()
    chrome_browser.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
    download_btn = chrome_browser.find_element_by_id('downloadButton')
    progress_label = chrome_browser.find_element_by_class_name('progress-label')
    progress_bar = chrome_browser.find_element_by_id('progressbar')
    close_button = chrome_browser.find_element_by_css_selector('.ui-dialog-buttonset>button')
    download_btn.click()



