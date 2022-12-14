from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstagramBot:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)
        self.user_name = "tupac.shakur.1997"
        self.password = "PeackyBlinders111"
        self.counter = 0
        self.quantity = 0
        self.my_number = 0

    def login_instagram(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        # ----------------------- Enter UserName ----------------------- #
        login = self.driver.find_element(By.NAME, "username")
        login.click()
        sleep(1)
        login.send_keys(self.user_name)
        # ----------------------- Enter Password ----------------------- #
        password = self.driver.find_element(By.NAME, "password")
        password.click()
        sleep(1)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

    def search_page(self, user_name):
        sleep(10)
        search_bar = self.driver.find_elements(By.CSS_SELECTOR, ".x1n2onr6 a")
        search_bar[2].click()
        sleep(2)
        entry = self.driver.find_element(By.TAG_NAME, "input")
        entry.click()
        sleep(1)
        entry.send_keys(f"{user_name}")
        sleep(2)
        entry.send_keys(Keys.ENTER)
        sleep(2)
        entry.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(10)
        followers = self.driver.find_element(By.CSS_SELECTOR, "section ul li:nth-of-type(2)")
        followers_quantity = int(followers.text.split()[0])
        followers.click()
        sleep(3)
        # ---------------------- click follow buttons - first step --------------------------------- #
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div:nth-of-type(1) div button")
        sleep(2)
        for button in follow_buttons:
            if button.text == "Follow":
                button.click()
                self.counter += 1
                sleep(2)
            else:
                pass
        # ---------------------- click follow buttons - second step --------------------------------- #
        length = int(followers_quantity / self.counter)
        for i in range(length):
            sleep(5)
            new_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div:nth-of-type(1) div button")
            sleep(3)
            self.my_number = self.my_number + self.counter + self.quantity
            self.quantity = 0
            for button in new_buttons[self.my_number:]:
                if button.text == "Follow":
                    button.click()
                    sleep(2)
                else:
                    pass
                self.quantity += 1
            self.counter = 0
        self.driver.quit()
        return followers_quantity
