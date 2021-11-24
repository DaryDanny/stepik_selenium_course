from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    picture_element = browser.find_element_by_css_selector("img#treasure")
    print("findpicture")
    x = picture_element.get_attribute("valuex")
    print ("findx")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    opt1 = browser.find_element_by_id("robotCheckbox")
    opt1.click()
    opt2 = browser.find_element_by_id("robotsRule")
    opt2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
