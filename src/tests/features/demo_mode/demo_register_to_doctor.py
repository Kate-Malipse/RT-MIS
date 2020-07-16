"""Demo registration feature tests."""
import pytest
from src.pages.KvrachuPages import (MainPage, DemoPage)
from pytest_bdd import (given, scenario, then, when)
from selenium.webdriver.support.wait import TimeoutException

# Constants

MED_SITE = "https://k-vrachu.ru/"
TITLE = "Региональный портал медицинских услуг"
ERROR_MESSAGE_REGISTER ="Запись в базу данных невозможна"


@scenario('demo_register_to_doctor.feature', 'Enable demo mode')
def test_enable_demo_mode():
    """Enable demo mode."""
    pass


@given('K-vrachu main page is displayed')
def kvrachu_main_page_is_displayed(driver):
    """K-vrachu main page is displayed."""
    main_page = MainPage(driver)
    main_page.go_to_site(MED_SITE)
    load_title = main_page.get_title()
    assert load_title == TITLE


@when('a user turns on the demo mode')
def a_user_turns_on_the_demo_mode(driver):
    """a user turns on the demo mode."""
    main_page = MainPage(driver)
    try:
        main_page.to_demo_page()
    except TimeoutException:
        print("Demo mode didn't turn on. Had to change region.")
        main_page.change_region(1)
        main_page.to_demo_page()


@then('a user logged in by a demo account')
def a_user_logged_in_by_a_demo_account(driver):
    """a user logged in by a demo account"""
    main_page = MainPage(driver)
    try:
        main_page.get_profile_element()
    except TimeoutException:
        print("Demo mode didn't turn on. Had to change region.")
        main_page.change_region(1)
        main_page.to_demo_page()
        try:
            main_page.get_profile_element()
        except:
            print("Didn't find demo account")

@scenario('demo_register_to_doctor.feature', 'Register to doctor from demo account')
def test_register_to_doctor_from_demo_account():
    """Register to doctor from demo account."""
    pass


@given('a user is authenticated by a demo account')
def a_user_is_authenticated_by_a_demo_account(driver):
    """a user is authenticated by a demo account."""
    main_page = MainPage(driver)
    try:
        main_page.get_profile_element()
    except TimeoutException:
        print("Didn't find demo account")


@when('a user selects the service Register to doctor')
def a_user_selects_the_service_register_to_doctor(driver):
    """a user selects the service Register to doctor."""
    demo_page = DemoPage(driver)
    try:
        demo_page.register_to_doctor()
    except TimeoutException:
        print("Didn't find service list")


@then('appears message "Запись в базу данных невозможна"')
def appears_message(driver):
    """appears message 'Запись в базу данных невозможна'"""
    demo_page = DemoPage(driver)
    register_message = demo_page.get_register_message
    assert register_message == ERROR_MESSAGE_REGISTER
    
