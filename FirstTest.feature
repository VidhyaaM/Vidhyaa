Feature: karate ui automation test 

  Scenario: Sample ui automation test 
    Given driver 'https://www.google.com/'
    And waitFor("input[title='Search']")
    And input("input[title='Search']",'python.org ')
    When click(".FPdoLc input[value='Google Search']")