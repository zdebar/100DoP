from selenium import webdriver

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")


# Closes only active tab
driver.close()

# Closes entire window
driver.quit(())