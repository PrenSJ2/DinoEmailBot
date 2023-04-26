import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Navigate to Gmail
driver.get("https://mail.google.com")

# Search for emails containing the word "sentry"
wait.until(EC.presence_of_element_located((By.NAME, "q"))).send_keys('sentry' + Keys.RETURN)

# Wait for search results to load
time.sleep(5)

email_index = 0
while True:
    try:
        # Re-query the email elements and get the current email by index
        emails = driver.find_elements(By.CSS_SELECTOR, 'div[role="main"] tr')
        if email_index >= len(emails):
            break

        email = emails[email_index]
        email.click()

        # Check if the email has a "View on Sentry" button
        try:
            sentry_button = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View on Sentry")))
            sentry_button.click()

            # Check if the <a class="app-6loic e1kml3iv1"> element has an href link
            app_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.app-6loic.e1kml3iv1")))
            if app_link.get_attribute("href"):
                # Switch to the Sentry tab and close it
                sentry_tab = driver.window_handles[-1]
                driver.switch_to.window(sentry_tab)
                driver.close()

                # Switch back to the Gmail tab
                gmail_tab = driver.window_handles[0]
                driver.switch_to.window(gmail_tab)

                # Delete the email
                delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I.J-J5-Ji.nX.T-I-ax7")))
                delete_button.click()

            # Go back to the search results
            driver.back()
            time.sleep(2)
        except:
            driver.back()
            time.sleep(2)

        # Increment the email index
        email_index += 1
    except:
        break

# Close the browser
driver.quit()
