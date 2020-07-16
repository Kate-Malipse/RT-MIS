"""Demo mode feature tests."""

from src.pages.KvrachuPages import (MainPage, DemoPage)
from src.tests.regions_urls import *
from selenium.webdriver.support.wait import TimeoutException
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

REGISTER_ERROR_MESSAGE = "Запись в базу данных невозможна"


@scenario('demo_register_to_doctor.feature', 'Register to doctor from demo account')
def test_register_to_doctor_from_demo_account():
    """Register to doctor from demo account."""
    pass


@given('user entered demo mode')
def user_entered_demo_mode(driver):
    """user entered demo mode."""
    success = False
    main_page = MainPage(driver)

    for region, url in regions.items():
        try:
            # 1. поиск кнопки с демо режимомом
            main_page.go_to_site(url)

            # 2. вход в демо режим
            main_page.to_demo_page()

            # 3. проверяем что демо режим включен
            main_page.get_profile_element()

            # Регион найден
            success = True
            break
        # в случае ошибки на первых шагах -> повторить с шага 1
        except TimeoutException:
            print(f'В регионе {region} не доступен работающий демо режим')
            continue
        # в случае непредвиденной ошибки выходим и валим тест
        except BaseException as e:
            print(f'Ошибка при поиске региона с работающим демо режимом. {e}')
            break

    if success is False:
        assert False, 'Не найдены регионы с работающим демо режимом'


@when('user selects the registration service')
def user_selects_the_registration_service(driver):
    """user selects the registration service."""
    demo_page = DemoPage(driver)
    demo_page.register_to_doctor()


@then('appears error message')
def appears_error_message(driver):
    demo_page = DemoPage(driver)
    register_message = demo_page.get_register_message()
    assert register_message == REGISTER_ERROR_MESSAGE


@then('user logout')
def user_logout(driver):
    demo_page = DemoPage(driver)
    demo_page.logout()
