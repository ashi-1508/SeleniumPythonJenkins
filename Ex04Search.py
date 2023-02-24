import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_something(self):



        #self.assertEqual(True, False)  # add assertion here

        filePath = "chromedriver.exe"

        url = "https://www.google.com/"



        driver = webdriver.Chrome(filePath)
        time.sleep(1)

        driver.get(url)
        time.sleep(1)

        qTextBox = driver.find_element(By.NAME, "q")
        #if(qTextBox.is_displayed() == True and qTextBox.is_enabled() == True):
        qTextBox.send_keys("Data Science")
        time.sleep(1)

        qTextBox.clear()

        '''
        else:
          print("Textbox is not working")
          time.sleep(1)
          driver.quit()

            '''

        expectedResult = "Google"
        actualResult = driver.title
        print(actualResult)

        if (expectedResult == actualResult):
            print("Test is passed")

        else:
            print("Test is failed")

        assert expectedResult == actualResult

        time.sleep(1)




if __name__ == '__main__':
    unittest.main()

