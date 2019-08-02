from appium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
        'deviceName': "iphone simulator",
        'browserName': "safari",
        'platformVersion': "12.0",
        'platformName': "iOS",
        'appiumVersion': "1.9.1",
        'name': "iOS Sim Test Window Maximize"
}
try:
    driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
    ctx = driver.context
    print("current context: ", ctx)
    driver.maximize_window()
    driver.get("https://saucelabs.com")
    sauce_client.jobs.update_job(driver.session_id, passed=True)
    driver.quit()
except Exception as e:
    print("something went wrong!!")
    print("Error: \n", e, driver.session_id)
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    driver.quit()
