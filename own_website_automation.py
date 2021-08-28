from selenium import webdriver

if __name__ == '__main__':
    chrome_browser = webdriver.Chrome('chromedriver.exe')
    chrome_browser.maximize_window()
    for item in range(100):
        chrome_browser.get('http://nihark.pythonanywhere.com/contact.html')
        # chrome_browser.implicitly_wait(5)
        email_input = chrome_browser.find_element_by_id('email')
        subject_input = chrome_browser.find_element_by_id('subject')
        message_input = chrome_browser.find_element_by_tag_name('textarea')
        button = chrome_browser.find_element_by_class_name('btn-default')
        email_input.send_keys(f'email{item}@gmail.in')
        subject_input.send_keys(f'{item} >testing the selenium script')
        message_input.send_keys(f'{item} >message body: nothing to write in this, just a simple test for selenium')
        button.click()
    chrome_browser.quit()

