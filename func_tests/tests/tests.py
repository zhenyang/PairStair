import unittest
from nose.plugins.attrib import attr
from selenium import webdriver

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    @attr('functional_test')
    def test_should_see_title(self):
        self.driver.get("http://127.0.0.1:8000/index")
        self.assertEqual(self.driver.title, "Pair Stair")

    @attr('functional_test')
    def test_should_see_table(self):
        self.driver.get("http://127.0.0.1:8000/index")
        table = self.driver.find_element_by_css_selector("table")
        self.assertIsNotNone(table)

    def test_add_a_programmer(self):
        self.driver.get("http://127.0.0.1:8000/index")
        add_programmer_button = self.driver.find_element_by_css_selector("a.add_programmer")
        self.assertIsNotNone(add_programmer_button)

        add_programmer_button.click()
        self.assertEqual(self.driver.title, "Add A Programmer")

        text_area = self.driver.find_element_by_css_selector("textarea.programmer_name")
        self.assertIsNotNone(text_area)

        text_area.send_keys("Good")
        submit_button = self.driver.find_element_by_css_selector("input.add_programmer")
        submit_button.click()

        self.assertEqual(self.driver.title, "Pair Stair")
        table_body = self.driver.find_element_by_css_selector("tbody")
        self.assertIn('Good',table_body.text)

    def test_clear_stair(self):
        self.driver.get("http://127.0.0.1:8000/index")
        clear_stair_button = self.driver.find_element_by_css_selector("a.clear_stair")
        self.assertIsNotNone(clear_stair_button)

        clear_stair_button.click()

        table_body = self.driver.find_element_by_css_selector("tbody")
        self.assertEqual(table_body.text,'')

if __name__ == '__main__':
    unittest.main()
