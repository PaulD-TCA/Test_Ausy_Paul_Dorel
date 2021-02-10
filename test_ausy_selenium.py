from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import unittest
import re


class RanstadSearchBaker(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox("/usr/local/bin/")
        self.driver.get("https://www.randstad.fr/")


    def test_baker_search(self):
        """
        That test go on the Ranstad page, does a basic search (a Boulanger in
        Bretagn), then click on the first job offer and finaly assert that
        the part "Informations complémentaires" is completed.
        """
        #In the search field the robot write "Boulanger".
        self.search = WebDriverWait(self.driver, 3).until(expected_conditions.
                    presence_of_element_located((By.ID, "id_What")))
        self.search.send_keys("Boulanger")
        time.sleep(3)
        #Accept cookies.
        self.cookies = WebDriverWait(self.driver, 3).until(expected_conditions.
                    element_to_be_clickable((By.CLASS_NAME,
                    'optanon-allow-all.accept-cookies-button'))).click()
        time.sleep(3)
        #Choose "Bretagne" in the scrooldown menu.
        self.region2 =  WebDriverWait(self.driver, 3).until(expected_conditions.
                    presence_of_element_located((By.CLASS_NAME, "selectric-scroll")))
        time.sleep(3)
        #Click on the search arrow
        self.search_arrow = WebDriverWait(self.driver, 3).until(expected_conditions.
                    presence_of_element_located((By.CLASS_NAME,
                    'icon.icon-arrow-right8'))).click()
        time.sleep(3)
        #Click on the first button to see the first job offer
        self.search = WebDriverWait(self.driver, 3).until(expected_conditions.
                    presence_of_element_located((By.ID, "Job-1"))).click()
        time.sleep(3)
        #Get "informations complémentaires".
        self.comp_info = WebDriverWait(self.driver, 3).until(expected_conditions.
                    element_to_be_clickable((By.XPATH,
                    '/html/body/div[4]/div[1]/div[3]/div/div[2]/div[1]/div/p[4]')))
        self.comp_info.get_attribute('innerHTML')
        self.comp_info_text = self.comp_info.text
        self.comp_info_list = re.split('\n| : ', self.comp_info_text)
        self.number_of_element = len(self.comp_info_list)
        """
        We have 6 items if the part is completed. Less than 6 items means that
        information is missing.
        """
        self.assertEqual(self.number_of_element, 6)
        if self.number_of_element == 6:
            print("All complementaries informations are here!")
            print("Niveau d'étude: " + self.comp_info_list[1])
            print("Salaire minimum: " + self.comp_info_list[3])
            print("Type de salaire: " + self.comp_info_list[5])
        else:
            print("Information(s) are missing")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
