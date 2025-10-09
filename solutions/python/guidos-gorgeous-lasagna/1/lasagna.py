"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40;
PREPARATION_TIME = 2;
print(EXPECTED_BAKE_TIME);

def bake_time_remaining(elapsed_bake_time):
    """
    Return time of baking
    Parametes : 
        elapsed_bake_time (int) : minutes of time baking

    Return :
        int : minutes remain
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time;
    

    


def preparation_time_in_minutes(numbre_layer):
    """
    Return the time of prepare
    
    Parametes : 
        numbre_layers(int) : number of layers
    Return : 
        int : total time of prepare
    """
    return PREPARATION_TIME * numbre_layer;



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return the time of total
    
    Parametes : 
        number_of_layers(int) : number layers
        elapsed_bake_time(int) : elapsed bake time 

    Return : 
        total time of baking
    """
    prepa = number_of_layers * PREPARATION_TIME;
    return prepa + elapsed_bake_time;
elapsed_time_in_minutes(3, 20)


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
