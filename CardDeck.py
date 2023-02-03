import random

def MakeDeck():
    Sets = ["Heart", "Diamond", "Spade", "Club"]
    Ranks = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "K"]
    TheDeck = []
    for Set in Sets:
        for Rank in Ranks:
            TheDeck.append({Set:Rank})
    return TheDeck

def ShuffleDeck(Deck):
    ShuffledDeck = []
    for i in range(len(Deck)):
        Pick=random.randint(0,len(Deck)-1)
        ShuffledDeck.append(Deck[Pick])
        Deck.pop(Pick)
    return ShuffledDeck

def DealCard(Deck):
    Card=Deck[0]
    Deck.pop(0)
    return Card, Deck


