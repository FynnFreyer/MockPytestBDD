Feature: Output
    As a user I want to be able to process text with the app.

Scenario: Output naming convention
    Given the file "xyz" with content "FooBar" exists
    When I pass "xyz" as an argument to the app
    Then the file "xyz_out" should exist

Scenario: Naming convention with suffix
    Given the file "xyz.txt" with content "FooBar" exists
    When I pass "xyz.txt" as an argument to the app
    Then the file "xyz_out.txt" should exist

Scenario: Uppercase output
    Given the file "xyz" with content "FooBar" exists
    When I pass "xyz" as an argument to the app
    Then the content of "xyz_out" should be "FOOBAR"


