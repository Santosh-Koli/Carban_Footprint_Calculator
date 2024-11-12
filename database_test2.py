from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

# Set up Chrome options for headless browsing (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Specify the path to your ChromeDriver
service = Service('chromedriver.exe')  # Replace with your ChromeDriver path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the URL
driver.get('http://smmydomain.infinityfreeapp.com/database_api.php?operation=read&table=login_table')

# Get page source or response content
content = driver.page_source

# Extract the JSON part from the content
start = content.find('[')
end = content.rfind(']') + 1

if start != -1 and end != -1:
    json_data = content[start:end]
    try:
        parsed_data = json.loads(json_data)  # Parse the JSON string into Python data
        print(parsed_data)  # Print or use the parsed data
        # print(type(parsed_data))
    except json.JSONDecodeError:
        print("Failed to parse JSON data")
else:
    print("JSON data not found in the response")

# Close the browser
driver.quit()
