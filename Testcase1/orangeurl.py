#Test case
#open web browser(chrome,firefox,edge)
#open url (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
#enter username and password
#click on login
#capture title of the home page(Actual title)
#verify title of the page: orangeHRM(expected)
#close browser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time  # Import the time module

# Set up the ChromeDriver with WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH, "username").send_keys("Admin")
driver.find_element(By.XPATH, "password").send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")



# Keep the browser open for 10 seconds
time.sleep(20)

# Close the browser (optional, you can comment this out if you want to keep it open)
driver.quit()


