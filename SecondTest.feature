@debug
Feature: karate ui automation test w3school log in

  Scenario: w3school create acc page
    Given driver 'https://www.w3schools.com/'
    And driver.maximize()
    And click('#w3loginbtn')
    And match driver.url =="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com"
    And click('{^span}Sign up')
    #And match driver.url =="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F"
    And input('#modalusername','vidhyaamanikumar.96@gmail.com')
    And input('#new-password','Newuser@1')
		When click('{^span}Sign up for free')
		And input("input[name='first_name']",'Vid')
		And input("input[name='last_name']",'mani')
		And click('{^span}Continue')
    * delay(5000)