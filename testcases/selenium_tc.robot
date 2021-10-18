*** Settings ***
Resource          ../resources/keywords.robot
Resource          ../libs/PWS/GUI/Keywords/GUI_Common_Keywords.robot
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome    # Browser on which the test suite is executed
${console_url}    https://1834-pws.pulseonestaging.io/admin#/login
${HEADLESS_MODE}    False

*** Test Cases ***
#Sanity Test Cases
TC00-login_console
    Login to PWS    ${pwsconsole["console_url_username"]}    ${pwsconsole["console_url_password"]}
    Close Browser
TC01-Create_User
    Add User    ${test_variables["newuser"]["Username"]}    ${test_variables["newuser"]["Full Name"]}    ${test_variables["newuser"]["Workspace Email"]}    ${test_variables["newuser"]["Phone Number"]}
    Close Browser
TC02-Add_App_Catalog
    Add App Catalog    ios    onedrive 
    Close Browser

Test
    #Log    "testing"
    #Create Webdriver    Chrome    executable_path=/usr/local/lib/python3.8/site-packages/chromedriver
    ##Open Browser    ${console_url}    ${BROWSER}
    #Go To    ${console_url}
    #Close All Browsers
    #Open PWS    ${console_url}    ${BROWSER}    alias
    # Open PWS    ${console_url}    ${BROWSER}    alias
    #pulselogin    sathiya    pulse1234
    #Login to PWS    ${pwsconsole["console_url_username"]}    ${pwsconsole["console_url_password"]}    alias=Check
    Add User    ${test_variables["newuser"]["Username"]}    ${test_variables["newuser"]["Full Name"]}    ${test_variables["newuser"]["Workspace Email"]}    ${test_variables["newuser"]["Phone Number"]}
    #Add App Catalog    ios    onedrive    
    Sleep    10
    Log    pass
