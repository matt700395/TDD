import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):#1

    def setUp(self): #2
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):#3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #4
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)#5
        self.fail('Finish the test!')#6


if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8



