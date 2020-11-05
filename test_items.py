import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestItems:
    def test_items(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        basket = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
        assert basket is not None, "Button not found"
