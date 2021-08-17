#functional_test.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):#1

    def setUp(self): #2
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):#3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #4
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)#5
        #여기부터 4장 코드
        #self.fail('Finish the test!')#6
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #그녀는 바로 작업을 추가하기로 한다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
                         )

        #공작깃털 사기라고 텍스트 상자에 입력한다
        #에디스의 취미는 날치잡이용 그물을 만드는 것이다
        inputbox.send_keys('공작깃털 사기')


        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
            "신규 작업이 테이블에 표시되지 않는다"
                        )

        self.fail("Finish the test!")

        #browser.quit()

if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8



