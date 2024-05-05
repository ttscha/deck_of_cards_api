import random
import app.app.main as main
import uuid

def generate_deck():
    """"
        generate a single deck of cards
    """
    colors = ["clubs", "diamonds", "spades", "hearts"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A" ]

    deck = []

    for color in colors:
        for number in numbers:
            deck.append({"name": number, "suit": color})
    uuid_temp = uuid.uuid4()

    main.decks[uuid_temp.hex] =  deck
    
    return {"deck" : deck, "uuid" : uuid_temp.hex}

def deck_shuffle(deck):
    random.shuffle(deck)
    return deck

