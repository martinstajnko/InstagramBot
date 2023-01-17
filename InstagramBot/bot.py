"""This module contains the InstagramBot class."""
from time import sleep

import constants

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class InstagramBot:

    def __init__(self, webdriver):
        self.driver = webdriver


    def navigate_to_url(self, url):
        self.driver.get(url)


    def wait_for_cookie_window(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]')))


    def allow_essential_cookies(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]').click()


    def wait_for_login_window(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="_acan _aiit _acap _aijb _acas _aj1-"]')))
        sleep(1)


    def login(self):
        self._insert_username(constants.USERNAME)
        self._insert_password(constants.PASSWORD)
        self._click_login_button()


    def wait_to_first_page_after_login(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'svg[aria-label="Instagram"]')))
         

    def save_login_info(self):

        # Not Now button
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _aiit _acao _aija _acas _aj1-"]').click()

    
    def turn_off_notifications(self):

        # Turn On button
        #self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]').click()

        # Not Now button
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]').click()

    
    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aacl _aacp _aacu _aacx _aada"]').click()

    
    def type_input_in_search_field(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]').send_keys('#bees')

    
    def click_on_first_search_result(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[role="none"]').click()


    def wait_until_hashtag_name_is_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]')))
        sleep(1)
    

    def click_on_first_post(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]').click()


    def check_if_post_is_liked(self) -> bool:

        element_heart = self.driver.find_element(By.CSS_SELECTOR, 'span[class="_aamw"]')

        try:
            element_heart.find_element(By.CSS_SELECTOR, 'svg[aria-label="Like"]')
            return False
            
        except NoSuchElementException:
            print('No such element, post seems to be liked.')
            return True


    def click_like_button(self):
        self.driver.find_element(By.CSS_SELECTOR, 'span[class="_aamw"]').click()


    def next_post(self):
        actions = ActionChains(self.driver)
        button_right = self.driver.find_element(By.CSS_SELECTOR, 'div[class=" _aaqg _aaqh"]')
        actions.move_to_element(button_right).perform()
        actions.send_keys(Keys.RIGHT).perform()

    
    def _insert_username(self, username):
        self.driver.find_element(By.NAME, 'username').send_keys(username)

    
    def _insert_password(self, password):
        self.driver.find_element(By.NAME, 'password').send_keys(password)


    def _click_login_button(self):
        sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _aiit _acap _aijb _acas _aj1-"]').click()
        

        

