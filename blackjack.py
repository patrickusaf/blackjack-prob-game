# BlackJack Probability Game
# by Patrick Svensson
# Started on: 12/06/2024
# Last update: v.0.0.0. 14/06/2024
# Blackjack basegame code by Code Coach: https://youtu.be/mpL0Y01v6tY?si=4JyCF--AdSqcY6Sj

import random
import pandas as pd
playerIn = True
dealerIn = True

# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []
probTable = pd.read_excel('probTable.xlsx')

# deal the cards
def dealCard(turn):
    '''Deal a card to the player or dealer and remove it from the deck.'''
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    '''Calculate the total of the player or dealer hand.'''
    total = 0
    face = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# check for winner
def revealDealerHand():
    '''Reveal the dealer's hand.'''
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
    
def checkForProbs(dealerHand, playerHand):
    '''Check for the probability of winning.'''
    # Calculate the probability of winning based of the total of the player and dealer hands for staying and hitting
    # 21 -- 100%
    # 20 -- 92%
    # 19 -- 85%
    # 18 -- 77%
    # 17 -- 69%
    # 16 -- 62%
    # 15 -- 58%
    # 14 -- 56%
    # 13 -- 39%
    # 12 -- 31%
    # 11 or less -- 0%

    # Natural 21 -- 4.8%
    # Hard Standing (17-20) -- 30.0%
    # Decision Hands (1-16) -- 38.7%
    # No Bust -- 26.5%
    #print(f"Probability of winning: {total(playerHand) - total(dealerHand)}")
    print(probTable)

    # Check if the player hand are equal
    if playerHand[0] == playerHand[1]:
        print("You have a pair!")
    elif playerHand[0] == 'A':
        print("You have an Ace!")
    else:
        pc1 = probTable["PC1"]
        #if total(playerHand) >= 5 and total(playerHand) <= 17:
            #action = probTable[pc1['7']]['5']
            #print(f"You should {action}")
            #print(total(playerHand), dealerHand[0])

# game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")

    # Show probability of winning
    checkForProbs(dealerHand, playerHand)

    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) < 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

# Outcome
if total(playerHand) == 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! You win!")
elif total(dealerHand) == 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! Dealer wins!")
elif total(playerHand) > 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You bust! Dealer wins!")
elif total(dealerHand) > 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer busts! You win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer wins!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand1_points = count_points(hand_1)
    hand2_points = count_points(hand_2)
    
    print(hand1_points)
    print(hand2_points)

    return hand1_points <= 21 and (hand1_points > hand2_points or hand2_points > 21)

def count_points(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            aces += 1
        else:
            total += int(card)
    if (total > 21 and aces > 0):
        total = total - (10*aces)
    return total