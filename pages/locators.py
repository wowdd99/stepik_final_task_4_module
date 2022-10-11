from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR,".product_main > h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR,"#messages > div:nth-child(1) .alertinner strong")  
    BOOK_PRICE = (By.CSS_SELECTOR,".product_main .price_color")        
    BOOK_PRICE_IN_MSG =  (By.CSS_SELECTOR,".alert-info .alertinner strong")        

