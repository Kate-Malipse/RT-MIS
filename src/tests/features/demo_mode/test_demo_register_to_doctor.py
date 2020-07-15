"""Demo registration feature tests."""
import pytest
from src.pages.KvrachuPages import (MainPage, DemoPage)
from pytest_bdd import (given, scenario, then, when)
from selenium.webdriver.support.wait import TimeoutException

# Constants

MED_SITE = "https://k-vrachu.ru/"
TITLE = "Региональный портал медицинских услуг"


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
        main_page.change_region(1)
        main_page.to_demo_page()


@then('a user logged in by a demo account')
def a_user_logged_in_by_a_demo_account(driver):
    """a user logged in by a demo account"""
    main_page = MainPage(driver)
    try:
        main_page.check_demo_mode_on()
    except TimeoutException:
        main_page.change_region(1)
        main_page.to_demo_page()
        try:
            main_page.check_demo_mode_on()
        except:
            print("Error")

# @scenario('demo_register_to_doctor.feature', 'Register to doctor from demo account')
# def test_register_to_doctor_from_demo_account():
#     """Register to doctor from demo account."""
#     pytest.skip("Skip")


# @given('a user is authenticated by a demo account')
# def a_user_is_authenticated_by_a_demo_account():
#     """a user is authenticated by a demo account."""
#     raise NotImplementedError


# @when('a user selects the service Register to doctor')
# def a_user_selects_the_service_register_to_doctor():
#     """a user selects the service Register to doctor."""
#     raise NotImplementedError


# @then('appears message "Запись в базу данных невозможна"')
# def appears_message():
#     """appears message "Запись в базу данных невозможна"."""
#     raise NotImplementedError
