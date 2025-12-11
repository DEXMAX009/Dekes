from heroes import Hero
import config
from enemy import Enemy
from log import Log
import random


def menu():
    print(config.listTextMenu, sep='\n')
    change_user = int(input("Введите число, своего класса"))
    battler(change_user)


def battler(change_user):
    hero_class = {}
    if change_user == 1:
        hero_class = config.mage
    elif change_user == 2:
        hero_class == config.tank
    elif change_user == 3:
        hero_class == config.warrior
    elif change_user == 4:
        hero_class == config.archer
    hero = Hero(hero_class)
    log = Log
    enemy = Enemy(config.slime)
    hero_damage_menu_battle(hero, enemy)