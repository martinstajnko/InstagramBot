""" This module contains the init_driver function."""


from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager


def init_driver() -> webdriver.Firefox:
    """
    Initialize and configure a Firefox webdriver.

    Returns:
        webdriver.Firefox: The initialized and configured Firefox webdriver
    """
    
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(1)
    driver.maximize_window()

    return driver