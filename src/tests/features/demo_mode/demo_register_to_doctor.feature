Feature: Demo mode

    Scenario: Register to doctor from demo account
        Given user entered demo mode
        When user selects the registration service
        Then appears error message 
        And user logout
