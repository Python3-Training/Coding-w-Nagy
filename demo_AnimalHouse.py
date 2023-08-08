#! /usr/bin/env python3
# The Random Zookeep
# Code walk-thru @ https://www.youtube.com/watch?v=Nmg9sYGILb0
#
import enum

class Food(enum.Enum):
   BIRD_FOOD = 1
   CAT_FOOD  = 2

import abc

class AbsAnimal(abc.ABC):
   def __init__(self, name='wild'):
      self.name = name
      self.health = 0
      
   @abc.abstractmethod
   def do_eat(self, food):
      pass

class Bird(AbsAnimal):
   def __init__(self):
      super().__init__("Bird")
      
   def do_eat(self, food):
      if isinstance(food, Food):
         if food is Food.BIRD_FOOD:
            self.health += 5
            return True
      return False

class Cat(AbsAnimal):
   def __init__(self):
      super().__init__("Cat")
      
   def do_eat(self, food):
      if isinstance(food, Food):
         if food is Food.CAT_FOOD:
            self.health += 5
            return True
      return False

import random
zoo = [Bird() if random.randrange(2)
       else Cat() for _ in range(10)]

print(*zoo, sep='\n')

if not issubclass(Cat, AbsAnimal):
   raise Exception("Crazy Cat")
if not issubclass(Bird, AbsAnimal):
   raise Exception("Crazy Bird")   
if issubclass(Bird, Cat):
   raise Exception("Unloved Bird")   
if issubclass(Cat, Bird):
   raise Exception("Unloved Cat")   

done = False
while not done:
   for pet in zoo:
      if random.randrange(1,3) == 1:
         pet.do_eat(Food.BIRD_FOOD)
      else:
         pet.do_eat(Food.CAT_FOOD)
      if pet.health > 20:
         print(pet.name, "wins!")
         done = True
         break

