from selenium import webdriver

if __name__ == '__main__':
    chrome_browser = webdriver.Chrome('chromedriver.exe')
    chrome_browser.maximize_window()
    # chrome_browser.get_screenshot_as_png()
    # print(chrome_browser)
    chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    # print('Selenium Easy Demo' in chrome_browser.title)
    # assert 'Selenium Easy Demo' in chrome_browser.title #this stops the code execution if result is false.
    show_message_button = chrome_browser.find_element_by_class_name('btn-default')
    button_text = show_message_button.get_attribute('innerHTML')
    print(button_text)
    assert 'Show Message' in chrome_browser.page_source
    user_message_input = chrome_browser.find_element_by_id('user-message')
    user_message_input.clear()
    user_message_input.send_keys('My name is Nihar')
    show_message_button.click()

    user_message_output = chrome_browser.find_element_by_id('display')
    output_text = user_message_output.get_attribute('innerHTML')
    print(output_text)
    assert 'My name is Nihar' in user_message_output.text

    user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
    print(user_button2)
    # chrome_browser.close()
    chrome_browser.quit()