Feature: User Access Management
 Scenario: Admin logins and create , update, delete another user data which doesnot exist
      Given User is login with valid credentials
      When Admin update user using username that doesnot exist
      Then Assert error Response
      And Delete User that doesnot exist, validate the error


  Scenario: User logins using invalid credentials
      When User tries to login using invalid credentials
      Then Invalid username/password supplied message


  Scenario: Admin logins delete another user data which doesnot exist
      Given User is login with valid credentials
      When Delete User that doesnot exist, validate the error
      Then validate asserting message user doesnot exist





