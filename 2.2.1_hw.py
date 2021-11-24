from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element_by_css_selector("span#num1")
    num2_element = browser.find_element_by_css_selector("span#num2")
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    print(num1)
    print(num2)
    sum_final = str(num1 + num2)
    print(sum_final)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{sum_final}']").click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    