"""This module contains the InstagramBot class."""


from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class InstagramBot:

    def __init__(self, webdriver):
        self.driver = webdriver


    def navigate_to_url(self, url: str):
        self.driver.get(url)


    def wait_for_cookie_window(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]')))


    def allow_essential_cookies(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]').click()


    def wait_for_login_window(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="_acan _acap _acas _aj1-"]')))
        sleep(1)


    def login(self, username: str, password: str):
        self._insert_username(username)
        self._insert_password(password)
        self._click_login_button()


    def wait_to_first_page_after_login(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'svg[aria-label="Instagram"]')))
         

    def save_login_info(self):
        # Not Now button
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _acao _acas _aj1-"]').click()

    
    def turn_off_notifications(self, value: bool):

        if value is False:
        # Turn On button
            self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]').click()

        else: 
        # Not Now button
            self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]').click()

    
    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aacl _aacp _aacu _aacx _aada"]').click()
    

    def execute_like_action(self, values: list, number_of_posts: int):

        for value in values:
            self.click_search()
            self._type_input_in_search_field(value)
            self._click_on_first_search_result()
            self._wait_until_hashtag_name_is_loaded()
            self._click_on_first_post()

            i = 0            
            while True:
                #value = self._check_if_post_is_liked()
                #if value == False:
                if not self._check_if_post_is_liked():
                    if i == number_of_posts:                        
                        break         

                    self._click_like_button()
                    i += 1
                    sleep(2)                    
                      
                self._next_post()
            
            sleep(1)
            self._close_post()
            sleep(1)
            self._click_home()


    def _type_input_in_search_field(self, value: str):
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]').send_keys(value)
        sleep(1)
        #self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]').send_keys('#bees')

    
    def _click_on_first_search_result(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[role="none"]').click()


    def _wait_until_hashtag_name_is_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]')))
        sleep(1)
    

    def _click_on_first_post(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]').click()


    def _check_if_post_is_liked(self) -> bool:

        element_heart = self.driver.find_element(By.CSS_SELECTOR, 'span[class="_aamw"]')

        try:
            element_heart.find_element(By.CSS_SELECTOR, 'svg[aria-label="Like"]')
            return False

        except NoSuchElementException:
            #print('No such element, post seems to be liked.')
            return True


    def _click_like_button(self):
        self.driver.find_element(By.CSS_SELECTOR, 'span[class="_aamw"]').click()
        #print('Post is liked.')


    def _next_post(self):
        actions = ActionChains(self.driver)
        button_right = self.driver.find_element(By.CSS_SELECTOR, 'div[class=" _aaqg _aaqh"]')
        actions.move_to_element(button_right).perform()
        actions.send_keys(Keys.RIGHT).perform()

    
    def _close_post(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="x10l6tqk x160vmok x1eu8d0j x1vjfegm"]').click()


    def _click_home(self):
        self.driver.find_element(By.CSS_SELECTOR, 
        'div[class="x9f619 x3nfvp2 x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x1xmf6yo x1e56ztr xz9dl7a xn6708d xsag5q8 x1ye3gou x1l895ks x159b3zp xdoji71 x1v9afh1 x1sxb60h x1ug36kh xubc8zo x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c"]').click()

    
    def _insert_username(self, username):
        self.driver.find_element(By.NAME, 'username').send_keys(username)

    
    def _insert_password(self, password):
        self.driver.find_element(By.NAME, 'password').send_keys(password)


    def _click_login_button(self):
        sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _acap _acas _aj1-"]').click()
        

        

