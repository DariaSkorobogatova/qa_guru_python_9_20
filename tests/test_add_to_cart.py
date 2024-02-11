import os

from selene import browser
from allure import step
from demowebshop_suite.utils import post_query
from demowebshop_suite.pages.cart_page import cart
from dotenv import load_dotenv

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


def test_add_to_cart_from_catalog(base_url):
    with step("Authorize via API and get the cookie"):
        response = post_query(f'{base_url}/login', json={"Email": login, "Password": password}, allow_redirects=False)
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Add to cart"):
        post_query(f'{base_url}/addproducttocart/catalog/13/1/1', cookies={'NOPCOMMERCE.AUTH': cookies})

    with step("Open cart page"):
        cart.open()
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})
        cart.open()

    with step("Assert items in the cart"):
        cart.assert_quantity_items_in_header_cart('1')
        cart.assert_cart_has_ordered_book('Computing and Internet')
        cart.delete_from_cart()


def test_add_to_cart_from_product_card(base_url):
    with step("Authorize via API and get the cookie"):
        response = post_query(f'{base_url}/login', json={"Email": login, "Password": password}, allow_redirects=False)
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Add to cart"):
        post_query(f'{base_url}/addproducttocart/details/45/1', cookies={'NOPCOMMERCE.AUTH': cookies})

    with step("Open cart page"):
        cart.open()
        cart.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
        cart.open()

    with step("Assert items in the cart"):
        cart.assert_quantity_items_in_header_cart('1')
        cart.assert_cart_has_ordered_book('Fiction')
        cart.delete_from_cart()


def test_add_3_items_to_cart_from_catalog(base_url):
    with step("Authorize via API and get the cookie"):
        response = post_query(f'{base_url}/login', json={"Email": login, "Password": password}, allow_redirects=False)
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Add to cart"):
        post_query(f'{base_url}/addproducttocart/catalog/13/1/1', cookies={'NOPCOMMERCE.AUTH': cookies})
        post_query(f'{base_url}/addproducttocart/catalog/45/1/1', cookies={'NOPCOMMERCE.AUTH': cookies})
        post_query(f'{base_url}/addproducttocart/catalog/22/1/1', cookies={'NOPCOMMERCE.AUTH': cookies})

    with step("Open cart page"):
        cart.open()
        cart.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
        cart.open()

    with step("Assert items in the cart"):
        cart.assert_quantity_items_in_header_cart('3')
        cart.assert_cart_has_ordered_books('Computing and Internet', 'Fiction', 'Health Book')
        cart.delete_from_cart()


def test_same_items_to_cart_from_product_card(base_url):
    with step("Authorize via API and get the cookie"):
        response = post_query(f'{base_url}/login', json={"Email": login, "Password": password}, allow_redirects=False)
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Add to cart"):
        post_query(f'{base_url}/addproducttocart/details/22/1', cookies={'NOPCOMMERCE.AUTH': cookies})
        post_query(f'{base_url}/addproducttocart/details/22/1', cookies={'NOPCOMMERCE.AUTH': cookies})

    with step("Open cart page"):
        cart.open()
        cart.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
        cart.open()

    with step("Assert items in the cart"):
        cart.assert_quantity_items_in_header_cart('2')
        cart.assert_cart_has_ordered_book('Health Book')
        cart.assert_quantity_input('2')
        cart.delete_from_cart()

