#!/usr/bin/python

import random

four = ['Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson', 'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin', 'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth', 'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj', 'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward', 'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina']
eight = ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki', 'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda', 'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent', 'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel', 'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio', 'Kelly', 'William', 'Jordan', 'Haley', 'Henry']
nine = ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C', 'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha', 'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry', 'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine', 'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L', 'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']

def randomPd(period):
    if period == 4:
        return four[random.randrange(0, len(four))]
    elif period == 8:
        return eight[random.randrange(0, len(eight))]
    elif period == 9:
        return nine[random.randrange(0, len(nine))]
    else:
        return "not a valid period"

print randomPd(9)
