import allure
from allure_commons._allure import step
from selene import browser, have
from allure_commons.types import AttachmentType
import requests

URL = 'https://demowebshop.tricentis.com/addproducttocart/'
CART_URL = 'https://demowebshop.tricentis.com/cart'


def test_add_notebook_to_cart(open_browser):
    with step("Add notebook to cart with API"):
        response = requests.post(url=f'{URL}catalog/31/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open(CART_URL)
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open(CART_URL)

    with step("Verify notebook in shopping cart"):
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))


def test_add_phone_to_cart(open_browser):
    with step("Add phone to cart with API"):
        response = requests.post(url=f'{URL}catalog/43/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open('/cart')

    with step("Verify Smartphone in shopping cart"):
        browser.element('.product-name').should(have.text('Smartphone'))


def test_add_book_to_cart(open_browser):
    with step("Add book to cart with API"):
        response = requests.post(url=f'{URL}catalog/45/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open(CART_URL)
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open(CART_URL)

    with step("Verify book in shopping cart"):
        browser.element('.product-name').should(have.text('Fiction'))


