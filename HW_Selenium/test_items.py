import pytest
import time
from selenium.common.exceptions import NoSuchElementException

#ссылка, по которой есть кнопка добавления в корзину
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#ссылка, по которой нет кнопки добавления в корзину
#link = "http://selenium1py.pythonanywhere.com/accounts/login/"

def test_add_button_existence(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    #добавила sleep только для того, чтобы визуально оценить выбор нужного языка, для ожидания прогрузки кнопки на странице реализован implicitly_wait
    time.sleep(5)
    elements = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(elements) == 1, f"Add to basket button is NOT on the page!"
