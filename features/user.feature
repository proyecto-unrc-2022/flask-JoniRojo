Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |

  Scenario: Add a new user
    Given the user "marty" doesnt exist
    When I store the custumer "marty"
    Then I should get a '201' response
    And "marty" is in the database

  #Scenario: Get operation to list all system users
   # Given that I have users are in the system
    #When I retrieve all the customers
    #Then I should get a '200' response
    #And the following user details are returned:
    #  | name        |
    #  | Jason Borne |  ... ??