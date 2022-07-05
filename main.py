#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
# Projet : "Beginner : Guess The Number (user)
#  
#  Copyright 2022  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from os import system
from time import sleep
import random


def find_computer(x):
    rand_computer = 0
    c = 1 # compteur de coup
    while rand_computer != x:
        print(f"L'ordinateur n'a pas trouve, essai numero : {c}")
        c += 1
        rand_computer = int(random.randint(1, 10))
        sleep(2)

    print(f"L'ordianteur a trouve en {c} coup(s)")

if __name__ == '__main__':
    system("cls")
    num_user = int(input("Merci de Fournir un Chiffre : "))
    find_computer(num_user)