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
   # Create User     ${varghese}     {varghese.jose@ivanti.com}
    #Create Workspace 
    #Add App Catalog
    #Push App
    #Push VPN Connection
    #Check whether Worklocation exists
    #Wipe Workspace
    #Delete Workspace
    #VPN Profile Push

regression Test Cases   
    #Add User    
    #Add Workspace
    #Add App Catalog
    #Sleep   50
    #Push space
    #Wipe workspace
    #Delete workspace
    #APP_Upload
    #App_deletion
    #Sleep   40
    apps_verify
    #App_Sync
    #Delete workspace    
    #App_Sync_upn
    #Sleep   50
    #VPN_PUSH    
#01_Testing
   # Log    ${pwsconsole["console_url"]}
    #Log    ${test_variables["newuser"]["Username"]}

#02_LoginConsole
    #login_console