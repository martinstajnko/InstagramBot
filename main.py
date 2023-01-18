from InstagramBot import init_driver, prerequisite
from InstagramBot.bot import InstagramBot


def main():

    prerequests = prerequisite.define_prerequisites()

    driver = init_driver.init_driver()

    bot = InstagramBot(driver)
    bot.navigate_to_url('https://www.instagram.com/')
    bot.wait_for_cookie_window()
    bot.allow_essential_cookies()
    bot.wait_for_login_window()
    bot.login(prerequests.username, prerequests.password)
    bot.wait_to_first_page_after_login()
    bot.save_login_info()
    bot.turn_off_notifications(True)
    bot.execute_like_action(prerequests.values, prerequests.number_of_posts) #(['#nature', '#dogs', '#wolfs'], 3)

    driver.quit()

if __name__ == "__main__":
    main()





