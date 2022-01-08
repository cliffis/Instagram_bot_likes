from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import username_ins, password_ins
import time
import random


class InstagramBot():

    def __init__(self, username_ins, password_ins):

        # options
        self.options = webdriver.ChromeOptions()
        # user-agent
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

        self.username = username_ins
        self.password = password_ins
        self.browser = webdriver.Chrome('chromedriver', options=self.options)

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '//button[text()="Accept All"]').click()
        time.sleep(2)

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username_ins)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password_ins)

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(5, 7))

        browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
        time.sleep(random.randrange(5, 10))

        browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
        time.sleep(random.randrange(3, 6))

    def find_elements_in_explore(self):
        browser = self.browser
        browser.get(f'https://www.instagram.com/explore/')
        time.sleep(5)

        hrefs = browser.find_elements(By.TAG_NAME, 'a')
        posts_urls = [item.get_attribute("href") for item in hrefs if "/p/" in item.get_attribute("href")]
        print(posts_urls)

        for url in posts_urls:
            try:
                browser.get(url)
                time.sleep(3)
                like_button = browser.find_element(By.XPATH,
                    # '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    # '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
                    "/ html / body / div[1] / section / main / div / div[1] / article / div / div[2] / div / div[2] / section[1] / span[1] / button").click()
                time.sleep(random.randrange(8, 10))
            except Exception as ex:
                print(ex)
                self.close_browser()














    # def login(self):
    #     browser = webdriver.Chrome('chromedriver', options=options)
    #     # browser.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    #
    #     try:
    #         browser.get('https://www.instagram.com')
    #         time.sleep(random.randrange(3, 5))
    #         browser.find_element(By.XPATH, '//button[text()="Accept All"]').click()
    #         time.sleep(2)
    #
    #         username_input = browser.find_element(By.NAME, 'username')
    #         username_input.clear()
    #         username_input.send_keys(username_ins)
    #         time.sleep(2)
    #
    #         password_input = browser.find_element(By.NAME, 'password')
    #         password_input.clear()
    #         password_input.send_keys(password_ins)
    #         password_input.send_keys(Keys.ENTER)
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
    #         time.sleep(10)
    #
    #         browser.close()
    #         browser.quit()
    #     except Exception as ex:
    #         print(ex)
    #         browser.close()
    #         browser.quit()


# login(username_ins, password_ins)

my_bot = InstagramBot(username_ins, password_ins)
my_bot.login()
my_bot.find_elements_in_explore()
# my_bot.put_many_likes("https://www.instagram.com/username/")