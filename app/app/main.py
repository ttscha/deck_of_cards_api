from typing import Union

from fastapi import FastAPI
import redis
import app.app.deck as deck

app = FastAPI()

r = redis.Redis(host='redis', port=6379)

# later on move this to redis
# all decks can dissapier when it reloads



import debugpy
debugpy.listen(("0.0.0.0", 5678))

decks = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}
# test

@app.get("/deck/new")
def generate_and_get_deck():
    deck_created = deck.generate_deck()
    return {
        "deck_id" : deck_created["uuid"],
        "remaining" : len(deck_created["deck"])
    }



@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"Number of hits": r.get("hits")}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/get_decks")
def get_decks():
    list_of_keys = list(decks.keys())
    return list_of_keys

@app.get("/deck/{uuid}")
def get_deck(uuid):
    return decks[uuid]

@app.get("/deck/{uuid}/shuffle")
def get_deck_and_shuffle(uuid):
    return deck.deck_shuffle(decks[uuid])

@app.get("/deck/{uuid}/pop")
def get_deck_and_pop_card(uuid):
    return decks[uuid].pop()


# start up config

deck.generate_deck()