from __future__ import annotations
from abc import ABC, abstractmethod
import random

class Ability(ABC):
    @abstractmethod
    def effect(self, state):
        pass

class Card(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def effect(self, state):
        pass

class Zone(ABC):
    @abstractmethod
    def addToTop(self, x: Card) -> None:
        pass

    @abstractmethod
    def addToBottom(self, x: Card) -> None:
        pass

    @abstractmethod
    def takeFromTop(self) -> Card:
        pass

    @abstractmethod
    def takeFromBottom(self) -> Card:
        pass

class Battlefield(Zone):
    def __init__(self, c):
       self.cardList = [x for x in c]


    def addToTop(self, x: Card) -> None:
        self.cardList.insert(0, x)

    def addToBottom(self, x: Card) -> None:
        self.cardList.append(x)

    def takeFromTop(self) -> Card:
        x = self.cardList[0]
        self.cardList = self.cardList[1:]
        return x

    def takeFromBottom(self) -> Card:
        x = self.cardList[-1]
        self.cardList = self.cardList[:-1]
        return x

class Graveyard(Zone):
    def __init__(self, c):
      self.cardList = [x for x in c]

    def addToTop(self, x: Card) -> None:
        self.cardList.insert(0,x)

    def addToBottom(self, x: Card) -> None:
        self.cardList.append(x)

    def takeFromTop(self) -> Card:
        x = self.cardList[0]
        self.cardList = self.cardList[1:]
        return x
    
    def takeFromBottom(self) -> Card:
        x = self.cardList[-1]
        self.cardList = self.cardList[:-1]
        return x

class Library(Zone):
    def __init__(self, c):
        self.cardList = [x for x in c]

    def addToTop(self, x: Card) -> None:
        self.cardList.insert(0,x)

    def addToBottom(self, x: Card) -> None:
        self.cardList.append(x)

    def takeFromTop(self) -> Card:
        x = self.cardList[0]
        self.cardList = self.cardList[1:]
        return x
    
    def takeFromBottom(self) -> Card:
        x = self.cardList[-1]
        self.cardList = self.cardList[:-1]
        return x

    def shuffle(self) -> None:
        size = len(self.cardList)

        temp = [0 for x in range(size)]

        for x in range(size):
            i = 0
            while True:
                i = random.randint(0,size-1)
                if temp[i] == 0:
                    break
            
            temp[i] = self.cardList[x]
        
        self.cardList = temp

class Hand(Zone):
    def __init__(self, c):
        self.cardList = [x for x in c]

    def addToTop(self, x: Card) -> None:
        self.cardList.insert(0,x)

    def addToBottom(self, x: Card) -> None:
        self.cardList.append(x)

    def takeFromTop(self) -> Card:
        x = self.cardList[0]
        self.cardList = self.cardList[1:]
        return x
    
    def takeFromBottom(self) -> Card:
        x = self.cardList[-1]
        self.cardList = self.cardList[:-1]
        return x

class Stack(Zone):
    def __init__(self, c):
        self.cardList = [x for x in c]

    def addToTop(self, x: Card) -> None:
        self.cardList.insert(0,x)

    def addToBottom(self, x: Card) -> None:
        self.cardList.append(x)

    def takeFromTop(self) -> Card:
        x = self.cardList[0]
        self.cardList = self.cardList[1:]
        return x
    
    def takeFromBottom(self) -> Card:
        x = self.cardList[-1]
        self.cardList = self.cardList[:-1]
        return x

