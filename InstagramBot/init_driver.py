""" This module contains the init_driver function."""

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager


def init_driver() -> webdriver.Firefox:
    """
    Creates a new instance of the Firefox driver.

    Returns:
        _type_: webdriver.Firefox
    """

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(1)
    driver.maximize_window()

    return driver