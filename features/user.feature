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

  Scenario: Update a user
    Given the user "nikk" are in the system
    When I update the customer "nikk"
    Then the system performs the update
    And the following user details are returned:
      | name       |
      | Niki Lauda |

  Scenario: Remove an user
    Given the user 'goncho' are in the system
    When the system delete the customer 'goncho'
    Then the system informs the user was deleted

  Scenario: List all system users
    Given that I have users are in the system
    When I receive a request to show the users list
    Then the following user data is returned:
      | username | name           |
      | jasonb   | Jason Bourne   |
      | nikk     | Niki Lauda     |
      | goncho   | Gonzalo Banzas |
