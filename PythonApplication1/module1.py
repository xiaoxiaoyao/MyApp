# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(L):
    return L[0]

def by_score(L):
    return L[1]

L2 = sorted(L,key=by_name)
print(L2)

L2 = sorted(L,key=by_score,reverse=True)
print(L2)