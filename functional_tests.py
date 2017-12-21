from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Go to a cool new todo app
        self.browser.get('http://127.0.0.1:1234')

        # See that To-Do is in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # see that you can enter a to-do item

        # Type "buy peacock feathers" into a text box

        # on enter we should have 1 todo

        # there is still a text box to enter more items
        # enter "use peacock feathers"

        # page shows both items

        # there is a unique url and explanation how to access your to-do's later

        # see that this url opens the existing to-dos

if __name__ == '__main__':
    unittest.main()
