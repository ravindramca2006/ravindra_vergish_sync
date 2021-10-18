import builtins
from os import DirEntry
import time
#from libs.robot_config.config_reader import get_variables
#from robot.libraries.BuiltIn import BuiltIn
#from robot.libraries.BuiltIn import _Misc
#import robot.api.logger as logger
from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import SeleniumLibrary
import time
from pathlib import Path
 
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mobile_worksapce(regcode):
    try: 
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['deviceName'] = 'RZ8NA28FJ2H'
        #desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
        desired_cap['appPackage'] = 'net.pulsesecure.pulsesecure'
        desired_cap['appActivity'] = 'net.juniper.junos.pulse.android.ui.LaunchActivity'
        desired_cap['autoGrantPermissions'] = True
        
        
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
        driver.implicitly_wait(5)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/input').send_keys("1742-pws.pulseonestaging.io")
        time.sleep(5)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/submit_input').click()
        time.sleep(5)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/email').send_keys('ravindra.mallikarjun@ivanti.com')
        time.sleep(5)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/pin').send_keys(regcode)
        time.sleep(5)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/authButton').click()
        time.sleep(20)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/agreeEula').click()
        time.sleep(20)
        driver.find_element_by_id('com.android.managedprovisioning:id/btn_continue').click()

        time.sleep(15)
        driver.find_element_by_id('android:id/button1').click()

        time.sleep(20)
        driver.swipe(50, 50,600,600, 1000)
        time.sleep(3)
        driver.swipe(500, 700, 500, 700, 1000)
        time.sleep(3)

        driver.find_element_by_id('android:id/action0').click()
    except AssertionError as msg:
            return(msg)
def app_install_check():
    try: 
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['deviceName'] = 'R5CR201KDDL'
        #desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
        #desired_cap['appPackage'] = 'com.google.android.gm'
        #desired_cap['appActivity'] = '.welcome.WelcomeTourActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
        driver.implicitly_wait(5)

        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=800)
        time.sleep(5)
        driver.find_element_by_xpath('//androidx.appcompat.app.ActionBar.Tab[@content-desc="Work"]/android.widget.RelativeLayout/android.widget.TextView').click()
        time.sleep(5)

        print(driver.is_app_installed('com.flipkart.android'))
        if(driver.is_app_installed('com.flipkart.android')):
            print("app is not deleted")
        else:
            print("app is deleted")
    except AssertionError as msg:
            return(msg)
def app_verification(apps_list):
    try: 
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['deviceName'] = 'R5CR201KDDL'
        #desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
        #desired_cap['appPackage'] = 'com.google.android.gm'
        #desired_cap['appActivity'] = '.welcome.WelcomeTourActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
        driver.implicitly_wait(5)

        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=800)
        time.sleep(5)
        driver.find_element_by_xpath('//androidx.appcompat.app.ActionBar.Tab[@content-desc="Work"]/android.widget.RelativeLayout/android.widget.TextView').click()
        time.sleep(5)
        for i in apps_list:
            print(driver.is_app_installed(i))
            if(driver.is_app_installed(1)):
                print("app is installed")
                print(i)
            
    except AssertionError as msg:
            return(msg)
def gmail_app_open():
    try: 
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['deviceName'] = 'R5CR201KDDL'
        #desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
        #desired_cap['appPackage'] = 'com.google.android.gm'
        #desired_cap['appActivity'] = '.welcome.WelcomeTourActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
        driver.implicitly_wait(5)

        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=800)
        time.sleep(5)
        driver.find_element_by_xpath('//androidx.appcompat.app.ActionBar.Tab[@content-desc="Work"]/android.widget.RelativeLayout/android.widget.TextView').click()
        time.sleep(5)
        driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Work Gmail"]').click()
        time.sleep(3)
        driver.find_element_by_id('com.google.android.gm:id/welcome_tour_got_it').click()
        time.sleep(3)
        driver.find_element_by_id('com.android.chrome:id/terms_accept').click()
        time.sleep(10)
        driver.find_element_by_id('com.android.chrome:id/next_button').click()
        time.sleep(5)
        driver.find_element_by_id('com.android.chrome:id/negative_button').click()
        time.sleep(120)
        driver.find_element_by_xpath('//*[@id="i0118"]').send_keys('Ramadevi@061982')
    except AssertionError as msg:
            print(msg)


def mobile_vpn_push():
    try: 
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['deviceName'] = 'R5CR201KDDL'
        #desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
        #desired_cap['appPackage'] = 'com.google.android.gm'
        #desired_cap['appActivity'] = '.welcome.WelcomeTourActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
        driver.implicitly_wait(5)

        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=800)
        time.sleep(5)
        driver.find_element_by_xpath('//androidx.appcompat.app.ActionBar.Tab[@content-desc="Work"]/android.widget.RelativeLayout/android.widget.TextView').click()
        time.sleep(5)
        driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Work Pulse Secure"]').click()
        time.sleep(20)
        driver.find_element_by_id('net.pulsesecure.pulsesecure:id/button_1').click()
        time.sleep(15)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText').clear()
        time.sleep(5)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText').send_keys('tester')
        time.sleep(5)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText').send_keys('juniper')
        time.sleep(10)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[6]/android.widget.Button').click()
        time.sleep(15)
        driver.find_element_by_id('android:id/button1').click()
    except AssertionError as msg:
            return(msg)