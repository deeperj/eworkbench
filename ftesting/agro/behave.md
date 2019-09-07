## Agro Business Application
Features of the application to include:

+ Agricultural programme/campaign
+ Farming activities
	+ Cultivation
	+ Harvest
+ Sales
+ Farm registration
+ Farm quality control
	+ Soil test and analysis
	+ Weather records
	+ Contamination
	+ Fertilizer usage

~~~gherkin
'''
All services follows the cycle: request => perform => respond.
The request are generally collated from the form posted
The perform/action is executed during processing
The response are various feedbacks sent via designated channels mainly: HTML web page, emails, SMS, electronic documents
'''

Feature: Agricultural programme
	'''
	A user may register/suggest a programme. 
	The programme approval cycle may be based on the user's office.
	If the user is a manager, then programme review and approval should be automatic.
	Other users should undergo an approval process which is finally approved by the manager user role	
	'''
	Scenario: Register a new programme
		Given a user wishes to register a new programme
		When the registration form is filled
		And the form is submitted
		And the form is validated
		Then the programme request is generated
		And the programme request marked as PENDING_REVIEW
		And the team for review are notified by channels
	
		Scenario: Review a pending programme request
			Given a programme request is available for review
			When the request is reviewed
			Then the request status is changed to REVIEWED
			And the review generated and assigned to the request
			And the review object is forwarded for approval
		
		Scenario: Review available for approval
			Given a valid review for request is available for approval
			When the review is approved
			Then the status of the review is set to APPROVED
			And the request status is updated to APPROVED
			And the original requester is notified
			And the reviewers are notified
			And the approved programme is published to the public
			
	Scenario Outline: Register a programme <event>
		'''
		The programme event follows a similar cycle to the programme application, however, only authorized officers can register an <event> under a programme
		'''
		Given an approved programme
		When the approved officer registers an <event> under that programme
		Then the <event> request is generated and set for review
		And the requested review is set for approval
		And the approved <event> is published under the programme
			
Feature: Agricultural programme activitis
	'''
	The programme activities such as measured kpi are reports captured by approved officers.
	These reports undergo similar request -> review -> approve cycle. However, the review does not need to be forwarded for approval as they are simply reports of what was observed.
	'''
	Scenario Outline: Register a programme <activity>
		Given a programme activity is being captured
		When the <activity> is recorded in specified form
		And the <activity> form is validated
		Then the <activity> record is set for review				
	
	Examples:
	|activity		|
	|performance	|
	|measured kpi	|
	|participation	|
			
	
Feature: Farming Activities
	'''
	The farming activities such as measured kpi are reports captured by approved officers.
	These reports undergo similar request -> review -> approve cycle. However, the review does not need to be forwarded for approval as they are simply reports of what was observed.
	'''
	Scenario Outline: Recording a farming <activity>
		Given a farming activity is being captured		
		When the <activity> is recorded in specified form
		And the <activity> form is validated
		Then the <activity> record is set for review				
		
		Examples:
		| activity |
		| cultivation |
		| harvest  |
		| weeding |
		| farm visit |
		| farm supplies |
		
Feature: Managing Sales 
	Scenario: Recording a sale
		Given a farm produce is offered for sale
		When the item is purchased
		Then a sale order request is generated
		And the order request is recorded with payment status set accordingly
		And the farm account is credited based on payment status and payment received
		And the farm store inventory is decreased based on ordered item
		And the order status is updated to CLOSED if sale was closed successfully
	
	Scenario: Farm Registration
		Given an unregistered farm is to be added to programme
		When the farm owner or representative fills farm registration form
		Then a registration request is generated
		And the registration request is forwarded for review
		And the review team is notified by channels
		
		Scenario: Registration request available for review
			Given a registration request is available for review
			When the review team makes recommendations
			Then the recommendations are assigned to request
			And the request status is updated to REVIEWED
			And the recommendation forwarded for approval
		
		Scenario Outline: Recommendation available for approval
			Given a recommendation is available for approval
			When the recommedation is received by assigned <user>
			Then the user can approve recommendation if authorised
			And the recommendation status is changed to APPROVED
			And the registration status is changed to APPROVED
			And the approval is recorded
			
			Examples:
			| user 		|
			| Consultant 	|
			| Manager 	|
			| Unit Head 	|
			| DGM	 	|
			| EGM 		|
			| DMD 		|
			| Other 		|
			
		
Feature: Farming Quality Control
	Scenario Outline: Recording a QA <activity>
		Given a QA <exercise> is performed on a farm
		When the <exercise> form is filled and submitted
		Then an activity request is generated
		And the request is forwarded for processing
		And the request is saved if valid
		And the concerned team for <exercise> are notified by channels
		
		Examples:
		| exercise 		|
		| soil test 		|
		| contamination  	|
		| fertilizer usage 	|
		| weather report 	|
		| irrigation 		|
		
Feature: Financial activities
	Scenario Outline: Performing a financial <activity>
		Given a financial <activity> being performed
		When the <activity> form is filled and submitted
		Then the financial task is forwarded to appropriate <gateway>
		And the <gateway> outcome is recorded
		
	Examples:
	| activity			| gateway |
	| expense 		| payu 	|
	| revenue (grant)	| payu 	|
	| revenue (sales) 	| payu 	|
	| expense 		| bank transfer 	|
	| revenue (grant)	| bank transfer 	|
	| revenue (sales) 	| bank transfer 	|
	| expense 		| bitcoin payment 	|
	| revenue (grant)	| bitcoin payment 	|
	| revenue (sales) 	| bitcoin payment 	|
	
	Scenario: Performing bank reconciliation
		Given a bank account with financial transactions
		When a bank reconciliation request is made
		And the reconcilliation form is submitted with attached transaction listings
		Then the system evaluates all credit transactions in listing against bank account total credit
		And the system evaluates all debit transactions in listing against bank account total debit
	
Feature: Health administration
	Scenario Outline: Administring treatment
		Given a prescribed <treatment> for an infected <patient>
		When the <treatment> procedure has been performed
		Then the <treatment> procedure outcome can be captured 
		And the <treatment> procedure observation can be recorded
		
	Examples:
	| treatment 			| patient 	|
	| drug administration 	| animal 	|
	| drug administration 	| crop 	|
	| surgery 			| animal 	|
	| pesticide/fumigation 	| crop 	|
				
	Scenario: Recording infection
		Given an observed infection
		When the infection report form is submitted
		Then a health request is generated
		And the request is set for review
		And the treatment action is assigned to review
		
	
~~~