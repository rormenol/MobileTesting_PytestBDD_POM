Feature: Sign up
Bree app should be already installed in user device

Scenario: Successfully registering a new user
Given the user is in initial screen
When the user tap 'Sign up' button
And the user enters a new valid <email>
And the user tap 'Next' button on 'What's your email?' screen
And the user enters a valid <password> and confirms it
And the user tap 'Next' button on 'Set your password' screen
And the user enters a valid <firstname>, <lastname>, and <dateofbirth>
And the user taps 'Next' button on 'What's your name?' screen 
Then 'SMS verification' screen is displayed

Examples:
| email                | password   | firstname | lastname | dateofbirth |
| testing006@gmail.com | Password@1 | Test006  | Testing  | 07/05/1995  |



Scenario: Displaying validation message for invalid email address
Given the user is in initial screen
When the user tap 'Sign up' button
And the user enters an <invalid_email> address
Then the validation message 'Invalid email address' should be displayed

Examples:
| invalid_email |
| testing03 |
| testing03@gmail.c |

Scenario: Displaying a bottom sheet when entering an already registered email address
Given the user is in initial screen
When the user tap 'Sign up' button
And the user enters an already <registered_email>
And the user tap 'Next' button on 'What's your email?' screen
Then a bottom sheet screen is displayed showing 'We missed you!' message

Examples:
| registered_email |
| testing001@gmail.com |
| testing002@gmail.com |
