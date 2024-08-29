'''  ITERATION 3

Module: MindMetrics: Transforming Data into Strategic Clarity

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this third iteration, I'll declare additional variables to show skills with different data types. '''

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis","Data Visualization","Machine Learning Models"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Boolean variable to indicate if the company is accepting new clients
accepting_new_clients: bool = True

# Integer variable showing the number of clients served
clients_served: int = 452

# List of strings representing the services offered by the company
services_offered: list = ["Predictive Analytics","Business Intelligence","Data Warehousing"]

# List of floats representing the accuracy percentages of predictive models
model_accuracy: list = [92.5, 88.3, 94.7, 90.2, 93.8]

###################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
MindMetrics: Transforming Data into Strategic Clarity
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Clients Served:             {clients_served}
Accepting New Clients:      {accepting_new_clients}
Model Accuracy:             {model_accuracy}
Services Offered:           {services_offered}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
