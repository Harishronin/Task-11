"""
 Name : Harish kumar
 Date : 05-Oct-2024
 Program 1 : Using python selenium and action chains visit the URL and do a drag and drop operations of the white rectangular box in the yellow rectangular box. 
 """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class JQueryDragAndDrop:
    def __init__(self, driver_path, url):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.wait = WebDriverWait(self.driver, 10)  
        self.url = url

    def open_page(self):
        # Open the URL
        self.driver.get(self.url)

    def perform_drag_and_drop(self):
        iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))
        self.driver.switch_to.frame(iframe)

        # Locate the draggable and droppable elements
        draggable = self.wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        droppable = self.wait.until(EC.presence_of_element_located((By.ID, "droppable")))

        # Perform drag and drop operation using ActionChains
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

        print("Drag and drop operation completed")

    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Main function
if __name__ == "__main__":
    driver_path = '/path/to/chromedriver'  # Replace with the actual path to your chromedriver
    url = 'https://jqueryui.com/droppable/'
    
    
    automation = JQueryDragAndDrop(driver_path, url)
    
    # perform the drag-and-drop
    automation.open_page()
    automation.perform_drag_and_drop()

    # Close the browser
    automation.close_browser()
