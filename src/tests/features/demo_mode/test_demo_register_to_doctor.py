"""Demo mode feature tests."""
from pytest_html import extras
from src.tests.regions_urls import *
from pytest_bdd import (given, scenario, then, when)
from src.pages.KvrachuPages import (MainPage, DemoPage)
from selenium.webdriver.support.wait import TimeoutException

# Константы
REGISTER_ERROR_MESSAGE = "Запись в базу данных невозможна"

# Сценарий

@scenario('demo_register_to_doctor.feature', 'Register to doctor from demo account')
def test_register_to_doctor_from_demo_account():
    """Register to doctor from demo account."""
    pass

# Шаги

@given('user entered demo mode')
def user_entered_demo_mode(driver):
    success = False
    main_page = MainPage(driver)

    for region, url in regions.items():
        try:
            # 1. Поиск кнопки с демо режимомом
            main_page.go_to_site(url)

            # 2. Вход в демо режим
            main_page.to_demo_page()

            # 3. Проверяем что демо режим включен
            main_page.get_profile_element()

            # Регион найден
            success = True
            break
        # В случае ошибки на первых шагах -> повторить с шага 1
        except TimeoutException:
            print('')
            print(f'В регионе {region} не доступен работающий демо режим')
            continue
        # В случае непредвиденной ошибки выходим и валим тест
        except BaseException as e:
            print('')
            print(f'Ошибка при поиске региона с работающим демо режимом. {e}')
            break

    if success is False:
        assert False, 'Не найдены регионы с работающим демо режимом'


@when('user selects the registration service')
def user_selects_the_registration_service(driver):
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
