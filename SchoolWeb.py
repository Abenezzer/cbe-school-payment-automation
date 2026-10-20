from pathlib import Path
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SchoolWebExtraction:

    def __init__(self,student_id):
        print("🚀 Launching the browser...")
        self.url = (
            "https://www.appsheet.com/start/"
            "908366bb-f4fd-485f-8a9e-07c1657135ce"
            "?platform=desktop"
            "#appName=26_27_STUDENT_DATA-925731409"
            "&view=DASHBOARD"
        )

        self.student_id = student_id

        profile_dir = Path(__file__).resolve().parent / "chrome_profile"
        profile_dir.mkdir(exist_ok=True)

        options = uc.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,800")

        # Do not force a Chrome version during testing.
        # Do not reuse a persistent profile yet.
        
        self.driver = uc.Chrome(
                version_main=153,
                user_data_dir=str(profile_dir),
                options=options,
                use_subprocess=True
            )

        self.wait = WebDriverWait(self.driver, 20)


    #Navigate to student Tab

    def __navigateToStudentTab(self):
        
        try:
            print("🌐 Opening AppSheet ...")
            # navigate to the appsheet
            self.driver.get(self.url)

            #click the side menu
            toggle_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Toggle menu']"))
            )
            toggle_button.click()
            

            #click the student tab
            print("📂 Locating the 'STUDENTS' navigation button...")
            students_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and .//span[normalize-space()='STUDENTS']]"))
            )
            students_button.click()
            
            
            
    
            
        except Exception as e:
            print(f"Navigation to Student Tab Filed \n {e}")

    def __search_student(self):
        
        print("⌨️ Locating the search input box...")

        #Search Student by ID
        search_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search STUDENTS']"))
        )

        search_box.clear()
        search_box.send_keys(self.student_id)
        
        

    def __extract_student_data(self):

        time.sleep(1)
        #click to see student detail
         # Construct a dynamic XPath using the student_id variable
        xpath_selector = f"//span[@data-testid='text-type-display-span' and text()='{self.student_id}']"
        student_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_selector))
        )
        student_element.click()

        
        student_data = {
        "STUDENT_ID": self.student_id,
        "FIRST_NAME": "",
        "MIDDLE_NAME": "",
        "LAST_NAME": "",
        "GRADE": "",
        "PHONE_NO": "",
        "BRANCH": "",
        "IS_SPECIAL_NEED": "",
        "FEE_TYPE": ""
        }

        field_mapping = {
        "FIRST_NAME": "FIRST_NAME",
        "MIDDLE_NAME": "MIDDLE_NAME",
        "LAST_NAME": "LAST_NAME",
        "GRADE": "GRADE",
        "PHONE_NO": "PHONE_NO",
        "BRANCH": "BRANCH",
        "IS_SPECIAL_NEED": "IS_SPECIAL_NEED",
        "FEE_TYPE": "FEE_TYPE(CURRICULUM)"
        }

        for dict_key, test_id in field_mapping.items():
            try:
                # XPath strategy: Locate the span with the field label, 
                # then traverse to the value element in the DOM tree.
                # In AppSheet lists, values often sit within the same container block.
                xpath = f"//div[@data-testid='{test_id}']//span[@data-testid='text-type-display-span'] | //div[@data-testid='{test_id}']//span[contains(@class, 'BooleanTypeDisplay')]"
                
                element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                student_data[dict_key] = element.text.strip()
                
            except Exception as inner_e:
                print(f"⚠️ Warning: Could not extract field '{dict_key}': {inner_e}")

        print("\n✅ Successfully Extracted Student Dictionary:")
       
        return student_data

    def action(self):
        self.__navigateToStudentTab()
        self.__search_student()
        student_data  = self.__extract_student_data()
        self.driver.quit()
        return student_data
    







