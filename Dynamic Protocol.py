from dataclasses import dataclass
from itertools import product
from random import random


@dataclass()
class PlayingCards:
    suit: str
    rank: str

    def __post_init__(self):
        self.suit = self.suit.lower()
        self.rank = self.rank.lower()

class CardDeck:
    SUITS = ['spades','diamonds','clubs','hearts']
    RANKS = list('ajkq') + list(str(n) for n in range(2,11))

    def __init__(self, cards = None):
        playing_cards = None

        if type(cards) == list and len(cards) > 0:
            playing_cards = list(filter(lambda a: type(a) == PlayingCards, cards))

        if playing_cards:
            self._cards = playing_cards
        else:
            self._cards = [PlayingCards(*args) for args in product(self.SUITS, self.RANKS)]

    def __getitem__(self, item):
        if type(item) == slice:
            return CardDeck(self._cards[item])
        else:
            return self._cards[item]
    
    def __len__(self):
        return len(self._cards)
    
    def __add__(self, other):
        if type(other) == PlayingCards:
            return CardDeck([*self._cards, other])
        elif type(other) == CardDeck:
            return CardDeck([*self._cards, *other._cards])
        
    def __radd__(self, other):
        return self+other
    
    def draw(self, n=1):
        drawn_cards = list()

        for i in range(n):
            idx = random.randrange(len(self))
            drawn_cards.append(self._cards.pop(idx))

        if n == 1:
            return drawn_cards[0]
        else:
            return CardDeck(drawn_cards)
