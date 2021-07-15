@debug
Feature: karate ui automation test w3school log in 

  Scenario: w3school page and try log in  and select course if not create account
    Given driver 'https://www.w3schools.com/'
    And driver.maximize()
    And click('#w3loginbtn')
    And match driver.url =="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com"
    * delay(5000)
		And input('#modalusername','vidaa@sequoiaat.com')
    And input('#current-password','Lordganesh@96')
    And click('{^span}Log in')   
    * delay(5000)
		* def abortSetup = exists('_2NfeO _1Stji') == true ? karate.call('SecondTest.feature@tag1') : karate.call('SecondTest.feature@tag2')