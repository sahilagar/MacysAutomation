Objective is to develop a program to validate the performance environment at component level. 
Performance environment comprise of multiple components highly likely some of the components may not work  after a deployment or an upgrade.
So, it’s a routine to validate the environment, though currently utilities being used for the same. 
However, planned to have an independent utility/one stop solution, as well a platform to add other useful functionalities which can be used for day to day activities.



Configuration File:

SAMPLE APPLICATION.......................................................

APPLICATIONNAME- BagApp_EWS
BagApp_EWS.SERVERNAME- p001xsbag003
BagApp_EWS.INSTANCE - macys_bagapp_ws1
BagApp_EWS.URL-http://lp001xsbag0003:84/bag/index.ognc?CategoryID=16958
BagApp_EWS.RESPONSE-status_code-404
BagApp_EWS.RESPONSE-status_code-404
BagApp_EWS.URL-http://lp001xsbag0003:84/bag/index.ognc?CategoryID=2910
BagApp_EWS.RESPONSE-status_code-200
BagApp_EWS.URL-http://lp001xsbag0003:84/bag/index.ognc?CategoryID=2921
BagApp_EWS.RESPONSE-status_code-200
BagApp_EWS.URL-http://lp001xsbag0003:84/bag/index.ognc?CategoryID=3865
BagApp_EWS.RESPONSE-status_code-200
BagApp_EWS.URL-http://lp001xsbag0003:84/bag/index.ognc?cm_sp=NAVIGATION-_-TOP_NAV-_-BAG-n-n
BagApp_EWS.RESPONSE-status_code-404
BagApp_EWS.RESPONSE-content-word

...........................................................................

To configure, application name, servername must be specified first. After that, put as manny instances, urls and responses as necessary with a dash seperating.

The application class is mainly a data container used to store all the data.

The logic is all in the requestApplication() function. The file io is all the code that is not in a function.

The dataToHTML() function takes the applications array and outputs all its data. Easy to manipulate if required.