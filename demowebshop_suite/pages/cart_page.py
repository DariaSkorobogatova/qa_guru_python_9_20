from selene import browser, have
from selenium.webdriver.common.by import By


class CartPage:
    def open(self):
        browser.open('/cart')
        return self

    def add_cookie(self, cookie: dict):
        browser.driver.add_cookie(cookie)
        return self

    def assert_quantity_items_in_header_cart(self, text):
        browser.element('#topcartlink .cart-qty').should(
            have.text(text)
        )
        return self

    def assert_cart_has_ordered_book(self, title):
        browser.element('.product-name').should(
            have.text(title)
        )
        return self

    def assert_cart_has_ordered_books(self, title1, title2, title3):
        browser.all('.product-name').should(
            have.texts(title1, title2, title3)
        )
        return self

    def assert_quantity_input(self, quantity):
        browser.element('.qty-input').should(have.attribute('value', quantity))
        return self

    def delete_from_cart(self):
        for element in browser.all('.remove-from-cart input'):
            element.click()
        browser.element('.update-cart-button').click()
        return self


cart = CartPage()

