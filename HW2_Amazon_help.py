
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path= 'C:\\Users\\Luttge\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088')

search = driver.find_element(By.ID, 'helpsearch')
search.send_keys('Cancel Items or Orders')
search.send_keys(Keys.RETURN)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text

assert expected_result == actual_result, f'Expected text {expected_result} did not match {actual_result}'
print("test case passed")
driver.quit()

