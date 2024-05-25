import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
    def test_starting_a_new_todo_list(self):
        self.browser.get("http://localhost:8000")
        # browser.get("https://www.google.com")
        self.assertIn("To-Do", self.browser.title)
        print("OK")

if __name__ == '__main__':
    unittest.main()