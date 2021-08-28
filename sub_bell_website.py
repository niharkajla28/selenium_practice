from selenium import webdriver

if __name__ == '__main__':
    chrome_browser = webdriver.Chrome('chromedriver.exe')
    chrome_browser.maximize_window()
    for item in range(500):
        chrome_browser.get('https://www.jennifersunbell.com/contact')
        # chrome_browser.implicitly_wait(5)
        name_input = chrome_browser.find_element_by_id('input_comp-kekdygeh')
        email_input = chrome_browser.find_element_by_id('input_comp-kekdyges1')
        message_input = chrome_browser.find_element_by_id('textarea_comp-kekdygev')
        button = chrome_browser.find_element_by_class_name('_1fbEI')
        email_input.send_keys(f'webdeveloper{item}@gmail.com')
        name_input.send_keys(f'{item} Give me a hint')
        message_input.send_keys(f'{item} I can make this website more secure against spam like this')
        button.click()
    chrome_browser.quit()

