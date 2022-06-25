from tkinter import LEFT, RIGHT
import pygame
from pygame.locals import *
import random
import os

# Variáveis
largura = 600
altura = 600
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

clock = pygame.time.Clock()
direcao = UP
pontos = 0


def inicioAleatorio():
    x = random.randint(30, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def limparTela():
    os.system('cls')
