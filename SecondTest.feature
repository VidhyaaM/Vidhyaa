Feature: karate ui automation test w3school log in
@tag1
  Scenario: w3school create acc page	
  	* delay(5000)  
    And click('{^span}Sign up')
		When click('{^span}Sign up for free')
		And input("input[name='first_name']",'Vid')
		And input("input[name='last_name']",'mani')
		And click('{^span}Continue')
		* driver.back()
		Then click('#w3loginbtn')
    And match driver.url =="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com"
		And input('#modalusername','vidhyaa@sequoiaat.com')
    And input('#current-password','Lordganesh@96')
    And click('{^span}Log in')
    * delay(5000)
    And click('#htmltext')
    And match driver.url == "https://my-learning.w3schools.com/courses/?tut=html"
    * delay(5000)
@tag2
  Scenario: select course after log in 
    * delay(5000)
    And click('#htmltext')
    And match driver.url == "https://my-learning.w3schools.com/courses/?tut=html"
    * delay(5000)