"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    # Number : premier élément , number + 1 : deuxième élément, number + 2 = troisième élément
    return [number, number + 1, number +2]

    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    # Check if the list is empty or no , if yes => false
    if rounds == [] :
        return False
    # Loop for to find the same number in the list round
    for i in rounds : 
        # Check if the number is the same value one of the number in list => True
        if number == i : 
            return True
    return False 


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    somme = 0
    # Loop for to get the total of all card value in the list
    for i in hand :
        somme += i
    # Get the avg by using total addition divise by number of elements in the list
    return somme / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    # Use the older function to get the avg of all card
    card = card_average(hand)
    # Get the postion of middle card by using len(hand) // 2 
    # Exemple : if the hand have 5 elements : len(hand) = 5 // 2 = 2 => hand[2] : is the position of middle card
    middle_card = hand[len(hand) // 2]
    # Get the avg of first and last card values
    avg_card = (hand[0] + hand[-1]) / 2
    # Check if the avg of first and last card values equality avg of total card or middle card equality avg of         total card
    if avg_card == card or middle_card == card :
        # If 1 of 2 operation is correct : True
        return True
    else : 
        return False
    


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # Get the number of card in the list
    total_card = len(hand)
    total_even = []
    total_odd = []
    # Use loop for to get the number in the position even
    for i in hand[::2] :
        # Take all number in index even to the same list
        total_even.append(i)
     # Use loop for to get the number in the position odd
    for i in hand[1::2] :
        # Take all number in index odd to the same list
        total_odd.append(i)
    # Use the older function to get the avg of all card in list even and all card in list odd
    avg_even = card_average(total_even)
    avg_odd = card_average(total_odd)
    # Check if the avg of list index even equality avg of list index odd => True
    if avg_odd == avg_even :
        return True
    return False
    

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    # Check if the last card in list is = 11
    if hand[-1] == 11 :
        # Remove the last card
        del hand[-1]
        # Add 22 in the dernier list (because if the last card is Jack(11) => we double it and add in the list)
        hand.append(22)
    else :
        # If the last card != Jack(11) => return the list without double 
        return hand
    # Return the final list
    return hand

    
