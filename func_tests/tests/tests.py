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
        self.go_to_index_page()
        self.assertEqual(self.driver.title, "Pair Stair")

    @attr('functional_test')
    def test_should_see_table(self):
        self.go_to_index_page()
        table = self.driver.find_element_by_css_selector("table")
        self.assertIsNotNone(table)

    @attr('functional_test')
    def test_add_a_programmer(self):
        self.go_to_index_page()
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

    @attr('functional_test')
    def test_clear_stair(self):
        self.go_to_index_page()
        clear_stair_button = self.driver.find_element_by_css_selector("a.clear_stair")
        self.assertIsNotNone(clear_stair_button)

        clear_stair_button.click()

        table_body = self.driver.find_element_by_css_selector("tbody")
        self.assertEqual(table_body.text,'')

    def add_a_programmer(self, programmer_name):
        self.driver.get("http://127.0.0.1:8000/add_programmer")
        text_area = self.driver.find_element_by_css_selector("textarea.programmer_name")
        text_area.send_keys(programmer_name)
        submit_button = self.driver.find_element_by_css_selector("input.add_programmer")
        submit_button.click()

    def go_to_index_page(self):
        self.driver.get("http://127.0.0.1:8000/index")



if __name__ == '__main__':
    unittest.main()
