import pygame
from abc import ABC, abstractmethod, ABCMeta

class Entity(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, surface, clock, width, height, color):
        self.X = None
        self.Y = None
        self.gravity = None 

    @abstractmethod
    def update(self):
        pass
