'''  ITERATION 4

Module: MindMetrics: Transforming Data into Strategic Clarity

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this fourth iteration, I introduce some basic statistics using Python.
     - min() is a built in function to find the smallest value passed in
     - max() is a built in function to find the largest value passed in
     - The statistics module offers methods to calculate mean and standard deviation.
'''

#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`: This gives us tools to calculate things like averages.
# Use command + F and type statistics to see where it is used in the code.

import statistics

#####################################
# Declare global variables
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Float variable for the average client satisfaction score
mean_score_value: float = 4.8

# Boolean variable to indicate if the company is accepting new clients
accepting_new_clients: bool = True

# Integer variable showing the number of clients served
clients_served: int = 452

# List of strings representing the services offered by the company
model_types: list = ["Predictive Analytics with Machine Learning", "Time Series Forecasting","Natural Language Processing",]

# List of floats representing the accuracy percentages of predictive models
model_accuracy: list = [92.5, 88.3, 94.7, 90.2, 93.8]

#Float variable for the average accuracy percentages of predictive models
average_model_accuracy: float = 91.9

#####################################
# Calculate Basic Statistics 
#   Do this BEFORE we declare the byline 
#   So the values have been calculated 
#   and are ready for use in the byline.
#####################################

# Calculate basic statistics using built-in functions and the statistics module
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_accuracy: float = min(model_accuracy)  
max_accuracy: float = max(model_accuracy)  
mean_accuracy: float = statistics.mean(model_accuracy)  
stdev_accuracy: float = statistics.stdev(model_accuracy)

###################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
MindMetrics: Transforming Data into Strategic Clarity
---------------------------------------------------------
Years in Operation:           {years_in_operation}
Clients Served:               {clients_served}
Has International Clients:    {has_international_clients}
Accepting New Clients:        {accepting_new_clients}
Skills Offered:               {skills_offered}
Model Types:                  {model_types}
Model Accuracy:               {model_accuracy}
Client Satisfaction Scores:   {client_satisfaction_scores}
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
