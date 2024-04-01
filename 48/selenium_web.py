from selenium import webdriver

# Import specifické metody
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Set up Selenium
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")


price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_elements(By.CLASS_NAME, value="a")


# Closes only active tab
driver.close()


# Closes entire window
driver.quit(())