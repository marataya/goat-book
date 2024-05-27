import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
    def test_starting_a_new_todo_list(self):
        self.browser.get("http://localhost:8000")
        # browser.get("https://www.google.com")
        self.assertIn("To-Do", self.browser.title)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('To-Do', header.text)
        inputbox = self.browser.find_element(By.ID, 'id_new_element')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = self.browser.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(
            '1: Buy peacock feathers',
            [row.text for row in rows]
        )

        inputbox = self.browser.find_element(By.ID, 'id_new_element')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = self.browser.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )
        self.assertIn(
            '1: Buy peacock feathers',
            [row.text for row in rows]
        )

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()