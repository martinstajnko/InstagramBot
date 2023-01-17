from InstagramBot import init_driver
from InstagramBot.bot import InstagramBot

def main():

    driver = init_driver.init_driver()

    bot = InstagramBot(driver)
    bot.navigate_to_url('https://www.instagram.com/')
    bot.wait_for_cookie_window()
    bot.allow_essential_cookies()
    bot.wait_for_login_window()
    bot.login()
    bot.wait_to_first_page_after_login()
    bot.save_login_info()
    bot.turn_off_notifications()
    bot.click_search()
    bot.type_input_in_search_field()
    bot.click_on_first_search_result()
    bot.wait_until_hashtag_name_is_loaded()
    bot.click_on_first_post()

    for i in range(10):
        value = bot.check_if_post_is_liked()
        if value == False:
            bot.click_like_button()
        bot.next_post()

    driver.quit()

if __name__ == "__main__":
    # print('Which action do you want to do: 1.Like 2.Follow')
    # x = input()
    main()





