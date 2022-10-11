from pages.base_page import BasePage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.locators import ProductPageLocators
import pytest
import time

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()       # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    time.sleep(5)
    book_name = page.get_book_name()
    book_price = page.get_book_price()
    page.compare_book_name_in_basket_and_in_cataloge(book_name)
    #page.compare_price_in_basket_and_in_cataloge(book_price)
    time.sleep(5)
