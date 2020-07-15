Feature: Demo registration

    Scenario: Enable demo mode
        Given K-vrachu main page is displayed
        When a user turns on the demo mode
        Then a user logged in by a demo account

    Scenario: Register to doctor from demo account
        Given a user is authenticated by a demo account
        When a user selects the service Register to doctor
        Then appears message "Запись в базу данных невозможна"