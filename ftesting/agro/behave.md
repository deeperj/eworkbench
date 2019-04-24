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
	Scenario: Register a new programme
		Given a user wishes to register a new programme
		When the registration form is filled
		And the form is submitted
		And the form is validated
		Then the programme request is generated
		And the programme request marked as under review
		And the team for review are notified by channels

	Scenario: Review a programme for review
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
	
Feature: Farming Activities
	Scenario Outline: Recording a farming <activity>
		Given an activity is performed on a farm
		When the activity form is filled and submitted
		Then an activity request is generated
		And the request is forwarded for processing
		And the request is saved if valid
		
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
			| user |
			| Consultant |
			| Manager |
			| Unit Head |
			| DGM |
			| EGM |
			| DMD |
			| Other |
			
		
Feature: Farming Quality Control
	Scenario Outline: Recording a QA <activity>
		Given a QA <exercise> is performed on a farm
		When the <exercise> form is filled and submitted
		Then an activity request is generated
		And the request is forwarded for processing
		And the request is saved if valid
		And the concerned team for <exercise> are notified by channels
		
		Examples:
		| exercise |
		| soil test |
		| contamination  |
		| fertilizer usage |
		| weather report |
		| irrigation |

~~~