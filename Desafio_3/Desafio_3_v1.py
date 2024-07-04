# Modelando o Sistema Bancário em POO com Python - PARTE 1

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.