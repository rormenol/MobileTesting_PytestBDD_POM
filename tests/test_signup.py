from pytest_bdd import scenario, given, when, then, parsers
from tests.pages.initial_page import InitialPage
from tests.pages.checkemail_page import CheckEmailPage
from tests.pages.setpassword_page import SetPasswordPage
from tests.pages.enteryourname_page import EnterYourNamePage
from tests.pages.smsverification_page import SMSVerificationPage

@scenario('../features/signup.feature','Successfully registering a new user')
def test_registering_new_user():
    pass

@given("the user is in initial screen")
def _(setup_driver):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user is in initial screen")
    pass

@when("the user tap 'Sign up' button")
def _(setup_driver):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user tap 'Sign up' button")
    initial_page = InitialPage(driver, logger)
    initial_page.tap_signup_button()

@when(parsers.parse("the user enters a new valid {email}"), target_fixture='checkemail_page')
def _(setup_driver, email):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user enters a new valid {email}")
    checkemail_page = CheckEmailPage(driver, logger)
    checkemail_page.enter_email(email)
    return checkemail_page
@when("the user tap 'Next' button on 'What's your email?' screen" )
def _(setup_driver, checkemail_page):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user tap 'Next' button")
    checkemail_page.tap_next_button()
    pass
@when(parsers.parse("the user enters a valid {password} and confirms it"), target_fixture='set_password_page')
def _(setup_driver, password):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user enters a valid {password} and confirms it")
    set_password_page = SetPasswordPage(driver, logger)
    
    set_password_page.enter_confirmation_password(password)
    set_password_page.enter_pasword(password)
    return set_password_page
    pass
@when("the user tap 'Next' button on 'Set your password' screen")
def _(setup_driver, set_password_page):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user tap 'Next' button on 'Set your password' screen")
    set_password_page.tap_next_button()
    pass
@when(parsers.parse("the user enters a valid {firstname}, {lastname}, and {dateofbirth}"), target_fixture='enter_your_name_page')
def _(setup_driver, firstname, lastname, dateofbirth):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user enters a valid {firstname}, {lastname}, and {dateofbirth}")
    enter_your_name_page = EnterYourNamePage(driver, logger)
    enter_your_name_page.enter_date_of_birth(dateofbirth)
    enter_your_name_page.enter_first_name_text(firstname)
    enter_your_name_page.enter_last_name_text(lastname)
    return enter_your_name_page
    
@when("the user taps 'Next' button on 'What's your name?' screen")
def _(setup_driver, enter_your_name_page):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user taps 'Next' button on 'What's your name?' screen")
    enter_your_name_page.tap_next_button()
    pass
@then("'SMS verification' screen is displayed")
def _(setup_driver):
    driver, logger = setup_driver
    logger.info(f":::Executing step - SMS verification screen is displayed")
    smsverification_page = SMSVerificationPage(driver, logger)
    smsverification_is_visible = smsverification_page.is_title_visible()
    assert smsverification_is_visible, "Cannot complete registration of the user - SMS verification page is not visible"
    pass

@scenario('../features/signup.feature','Displaying validation message for invalid email address')
def test_invalid_email_message():
    pass

@when(parsers.parse("the user enters an {invalid_email} address"), target_fixture='check_email_page')
def _(setup_driver, invalid_email):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the user enters an {invalid_email} address")
    check_email_page = CheckEmailPage(driver, logger)
    check_email_page.enter_email(invalid_email)
    return check_email_page

@then("the validation message 'Invalid email address' should be displayed")
def _(setup_driver, check_email_page):
    driver, logger = setup_driver
    logger.info(f":::Executing step - the validation message 'Invalid email address' shoudl be displayed")
    invalid_email = check_email_page.is_email_invalid()
    assert invalid_email, "Invalid email address message is not displayed!"

@scenario('../features/signup.feature','Displaying a bottom sheet when entering an already registered email address')
def test_registering_existed_user():
    pass

@when(parsers.parse("the user enters an already {registered_email}"), target_fixture='checkemail_page')
def _(setup_driver, registered_email):
    driver, logger = setup_driver
    check_email = CheckEmailPage(driver, logger)
    check_email.enter_email(registered_email)
    return check_email

@then("a bottom sheet screen is displayed showing 'We missed you!' message")
def _(setup_driver, checkemail_page):
    driver, logger = setup_driver
    logger.info(":::Executing step - Then a bottom sheet screen is displayed")
    user_exists = checkemail_page.is_miss_you_message_visible()
    assert  user_exists, "We missed you! bottom sheet is not displayed! check if user is new"
    pass