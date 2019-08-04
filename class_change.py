from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = webdriver.ChromeOptions()

# Disable browser notifications
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# Disable images
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout("100")


class Class_change:
    def __init__(self, name, code, options):
        self.name = name
        self.code = code
        self.options = options

    def __repr__(self):
        return f"{self.code}: {self.name}, Option(s) {self.options}"

    def change(self):
        for option in self.options:
            print(time.time())
            driver.get(f"https://www.timetable.usyd.edu.au/personaltimetable/timetable/SID HERE/customise/chooseclass/edit/{self.code}/")
            driver.get(f"https://www.timetable.usyd.edu.au/personaltimetable/timetable/SID HERE/customise/chooseclass/edit/{self.code}/")  # Idk why it only works when this line is run twice
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class-choose")))
            class_options = driver.find_elements_by_class_name("class-choose")
            class_options[option-1].click()
            driver.find_element_by_xpath("//*[@id='confirm-setclass']/div/div[2]/form/input[2]").click()
            message = driver.find_element_by_xpath("/html/body/div[3]/h2").text
            submessage = driver.find_element_by_xpath("/html/body/div[3]/p").text
            if message != "Your request could not be completed":
                print("Class changed successfully.")
                exit()

            # If the class change request limit has been reached. This occurs after 21 successive requests.
            if "hour" in submessage:
                # Perform a successful class change to reset the limit
                driver.get("LINK_HERE")
                driver.get("LINK_HERE")
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class-choose")))
                class_options = driver.find_elements_by_class_name("class-choose")
                class_options[0].click()
                driver.find_element_by_xpath("//*[@id='confirm-setclass']/div/div[2]/form/input[2]").click()
                time.sleep(5)   # Required delay, system takes time to process new class change.
                driver.get("LINK_HERE")
                driver.get("LINK_HERE")
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class-choose")))
                class_options = driver.find_elements_by_class_name("class-choose")
                class_options[0].click()
                driver.find_element_by_xpath("//*[@id='confirm-setclass']/div/div[2]/form/input[2]").click()
                time.sleep(1)


def login():
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "unikey")))
    driver.find_element_by_id("unikey").send_keys("UNIKEY HERE")
    driver.find_element_by_id("password").send_keys("PASSWORD HERE")
    driver.find_element_by_class_name("button").click()


driver.get("https://www.timetable.usyd.edu.au/personaltimetable/")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-button"))).click()
login()

changes = []
with open("class_changes.txt", 'r') as f:
    for line in f:
        line_array = [s.strip() for s in line.split(",")]
        assert len(line_array) >= 3, "Each line in class_changes.txt must have at least 3 arguments."
        name = line_array[0]
        code = line_array[1]
        options = []
        for n in range(2, len(line_array)):
            options.append(int(line_array[n]))
        changes.append(Class_change(name, code, options))


while True:
    for c in changes:
        c.change()
    time.sleep(30)
