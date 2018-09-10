class locator(object):
    # Landig page locators
    tenantalias ="/html/body/div[7]/div/div/div[2]/input"
    okButton="/html/body/div[7]/div/div/div[3]/div[2]/button"
    gotologinpage ='/html/body/div[3]/go-to-login/div[2]/div/div/button'
    logo ='/html/body/header/div/nav/div[1]/span/img'

    # Login Page
    loginname = 'loginUsername'
    password= 'loginPassword'
    loginbutton = "//button[@name='btnLogin']"
    invalidlogin = 'strong.ng-binding'
    companyinfo = 'div.panel-body.ng-binding'

    # Start test page

    tc = "//input[@type='checkbox']"
    starttestButton = 'btnStartTest'

    # Test Page
    # answeroption = '/html/body/div[2]/question-template/ng-include/div[1]/div[2]/div/div/div/div[2]/dl[2]/dt'
    answeroption = 'B'
    nextbutton = 'btnNext'
    submitbutton = 'btnSubmit'
    confirmationmessage = '/html/body/div[2]/question-template/ng-include/div[1]/div[2]/div/div/div/div[2]/dl[2]/d'
    okconfirmationbutton = 'okBtnModalNotification'
    submitresponse = 'submit-confirmation-text'

