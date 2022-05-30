Feature: Verify the Pet in PetStore

  Scenario: Verify one New Pet is created, and image is uploaded and the Pet is fetched using status
    When A New Pet is added to the Store
    Then Pet is Successfully created
    And Add an image of the Pet
    And Verify the Pet using the Status



  Scenario Outline: Verify Pet using Form data , find using valid tag name and delete using pet id
    Given Pet <id> is created using form
    When find pet by tag name and validate the data
    Then Delete the pet by using pet id
      Examples:
        | id  |
        | 100 |
        | 200 |

    Scenario: Update an existing pet that doesnot exist

      When Update Pet Update url is accessed and invalid pet is passed
      Then Pet doesnot exist error 400 should be found

    Scenario: Find Pet by using invalid tag value
      When User finds invalid tag value to find the pet
      Then Give 400 Error Tag value doesnot exist



