import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import by

class demowebshop(unittest.TestCase)

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install)

    def register(self)
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")

    def Login(self)
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")


if __name__ == '__main__':
    unittest.main()