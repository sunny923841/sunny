from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("Eric_guodongliang")
browser.find_element_by_id("su").submit()