# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from parser import *
from itertools import product
from automateBase import AutomateBase
from automate import Automate

show = True # Mettre à True pour afficher graphiquement les tests de construction d'automates 

def equalList (l, m) :
    l1 = copy.deepcopy(l)
    l2 = copy.deepcopy(m)
    if len(l1) == 0 and len(l2) == 0:
        return True
    elif len(l1) == 0 or len(l2) == 0:
        return False
    else:
        e = l1[0]
        if e in l2:
            l1.remove(e)
            l2.remove(e)
            return equalList(l1,l2)
        else:
            return False

#####
# Définition des différents automates de test
#####

# auto1 reconnait les mots sur {a,b} ayant un nombre impair de a 
# Déterministe/Complet

s01 = State(0,True,False)
s11 = State(1,False,True)
auto1 = Automate([Transition(s01,'b',s01),Transition(s01,'a',s11),Transition(s11,'b',s11),Transition(s11,'a',s01)])

# auto2 reconnait les mots de la forme a*b*
# Déterministe/Non Complet

s02 = State(0,True,True)
s12 = State(1,False,True)
auto2 = Automate([Transition(s02,'a',s02),Transition(s02,'b',s12),Transition(s12,'b',s12)])

# auto3 (exemple dans le sujet) reconnait les mots avec 3 a consécutifs
# ND/NC

s03 = State(0,True,False)
s13 = State(1,False,False)
s23 = State(2,False,False)
s33 = State(3,False,True)
auto3 = Automate([Transition(s03,'a',s03),Transition(s03,'b',s03),Transition(s03,'a',s13),Transition(s13,'a',s23),Transition(s23,'a',s33),Transition(s33,'a',s33),Transition(s33,'b',s33)])

# auto4 reconnait les mots contenant (au moins) un a
# ND/C

s04 = State(0,True,False)
s14 = State(1,False,True)
auto4 = Automate([Transition(s04,'a',s04),Transition(s04,'b',s04),Transition(s04,'a',s14),Transition(s14,'a',s14),Transition(s14,'b',s14)])

# auto5 reconnait les mots commençant par un b (avec deux états initiaux)
# ND/C

s05 = State(0,True,False)
s15 = State(1,True,False)
s25 = State(2,False,True)
s35 = State(3,False,False)
auto5 = Automate([Transition(s05,'a',s35),Transition(s15,'a',s35),Transition(s05,'b',s25),Transition(s15,'b',s35),Transition(s25,'a',s25),Transition(s25,'b',s25),Transition(s35,'a',s35),Transition(s35,'b',s35)])

"""
auto1.show("auto1")
auto2.show("auto2")
auto3.show("auto3")
auto4.show("auto4")
auto5.show("auto5")
"""

#####
# Tests des fonctions
#####

print("Début des tests :")

# Fonction succ

if (auto1.succ([s01],'a') == None):
    print("Succ non définie")
else:
    print("Tests fonction succ:")
    cpt = 0
    test = auto1.succ([s01],'a')
    target = [s11]
    if equalList(test, target):
        cpt = cpt+1
    else:
        print("- Fail test 1 : renvoie", test, "au lieu de", target)
    test = auto4.succ([s04],'a')
    target = [s04,s14]
    if equalList(test, target):
        cpt = cpt+1
    else:
        print("- Fail test 2 : renvoie", test, "au lieu de", target)
    test = auto3.succ([s03,s13],'b')
    target = [s03]
    if equalList(test, target):
        cpt = cpt+1
    else:
        print("- Fail test 3 : renvoie", test, "au lieu de", target)
    test = auto5.succ([s05,s15],'a')
    target = [s35]
    if equalList(test, target):
        cpt = cpt+1
    else:
        print("- Fail test 4 : renvoie", test, "au lieu de", target)
    test = auto3.succ([s13,s23],'b')
    target = []
    if equalList(test, target):
        cpt = cpt+1
    else:
        print("- Fail test 5 : renvoie", test, "au lieu de", target)
    print(cpt, "tests sur 5 réussis.")

# Fonction accepte

if auto1.accepte(auto1,"a") == None:
    print("Accepte non définie")
else:
    print("Tests fonction accepte:")
    cpt = 0
    test = auto1.accepte(auto1,"ababab")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 1 : renvoie", test, "au lieu de", target)
    test = auto2.accepte(auto2,"")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 2 : renvoie", test, "au lieu de", target)
    test = auto1.accepte(auto1,"abba")
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 3 : renvoie", test, "au lieu de", target)
    test = auto3.accepte(auto3,"abaaab")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 4 : renvoie", test, "au lieu de", target)
    test = auto3.accepte(auto3,"abaab")
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 5 : renvoie", test, "au lieu de", target)
    test = auto5.accepte(auto5,"ba")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 6 : renvoie", test, "au lieu de", target)
    print(cpt, "tests sur 6 réussis.")

# Fonction estComplet

if auto1.estComplet(auto1,"ab") == None:
    print("estComplet non définie")
else:
    print("Tests fonction estComplet:")
    cpt = 0
    test = auto1.estComplet(auto1,"ab")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 1 : renvoie", test, "au lieu de", target)
    test = auto1.estComplet(auto2,"ab")
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 2 : renvoie", test, "au lieu de", target)
    test = auto1.estComplet(auto3,"ab")
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 3 : renvoie", test, "au lieu de", target)
    test = auto1.estComplet(auto4,"ab")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 4 : renvoie", test, "au lieu de", target)
    test = auto1.estComplet(auto5,"ab")
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 5 : renvoie", test, "au lieu de", target)
    print(cpt, "tests sur 5 réussis.")

# fonction estDeterministe

if auto1.estDeterministe(auto1) == None:
    print("estDeterministe non définie")
else:
    print("Tests fonction estDeterministe:")
    cpt = 0
    test = auto1.estDeterministe(auto1)
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 1 : renvoie", test, "au lieu de", target)
    test = auto1.estDeterministe(auto2)
    target = True
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 2 : renvoie", test, "au lieu de", target)
    test = auto1.estDeterministe(auto3)
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 3 : renvoie", test, "au lieu de", target)
    test = auto1.estDeterministe(auto4)
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 4 : renvoie", test, "au lieu de", target)
    test = auto1.estDeterministe(auto5)
    target = False
    if test == target:
        cpt = cpt+1
    else:
        print("- Fail test 5 : renvoie", test, "au lieu de", target)
    print(cpt, "tests sur 5 réussis.")

# fonction completeAutomate

if auto1.completeAutomate(auto1,"ab") == None:
    print("completeAutomate non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de completeAutomate")
    test = auto1.completeAutomate(auto1,"ab")
    if show:
        auto1.show("cA1_auto1")
        test.show("cA1_auto1_complet")
    else:
        print(auto1)
        print(test)
    val = input("Appuyer sur une touche pour test 2 de completeAutomate")
    test = auto1.completeAutomate(auto3,"ab")
    if show:
        auto3.show("cA2_auto3")
        test.show("cA2_auto3_complet")
    else:
        print(auto3)
        print(test)
        
# fonction determinisation

if auto1.determinisation(auto1) == None:
    print("determinisation non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de determinisation")
    test = auto1.determinisation(auto1)
    if show:
        auto1.show("d1_auto1")
        test.show("d1_auto1_deterministe")
    else:
        print(auto1)
        print(test)
    val = input("Appuyer sur une touche pour test 2 de determinisation")
    test = auto1.determinisation(auto3)
    if show:
        auto3.show("d2_auto3")
        test.show("d2_auto3_deterministe")
    else:
        print(auto3)
        print(test)
    
    
# fonction complementaire

if auto1.complementaire(auto1,"ab") == None:
    print("complementaire non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de complementaire")
    test = auto1.complementaire(auto1,"ab")
    if show:
        auto1.show("c1_auto1")
        test.show("c1_auto1_complementaire")
    else:
        print(auto1)
        print(test)
    val = input("Appuyer sur une touche pour test 2 de complementaire")
    test = auto1.complementaire(auto2,"ab")
    if show:
        auto2.show("c2_auto2")
        test.show("c2_auto2_complementaire")
    else:
        print(auto2)
        print(test)
    

# fonction intersection

if auto1.intersection(auto1,auto2) == None:
    print("intersection non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de intersection")
    test = auto1.intersection(auto1,auto2)
    if show:
        auto1.show("i1_auto1")
        auto2.show("i1_auto2")
        test.show("i1_intersection")
    else:
        print(auto1)
        print(auto2)
        print(test)

# fonction union (facultative)

if auto1.union(auto1,auto2) == None:
    print("union non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de union")
    test = auto1.union(auto1,auto2)
    if show:
        auto1.show("u1_auto1")
        auto2.show("u1_auto2")
        test.show("u1_union")
    else:
        print(auto1)
        print(auto2)
        print(test)

# fonction concatenation

if auto1.concatenation(auto1,auto2) == None:
    print("concatenation non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de concatenation")
    test = auto1.concatenation(auto1,auto2)
    if show:
        auto1.show("conc1_auto1")
        auto2.show("conc1_auto2")
        test.show("conc1_concatenation")
    else:
        print(auto1)
        print(auto2)
        print(test)
    val = input("Appuyer sur une touche pour test 2 de concatenation")
    test = auto1.concatenation(auto2,auto5)
    if show:
        auto2.show("conc2_auto2")
        auto5.show("conc2_auto5")
        test.show("conc2_concatenation")
    else:
        print(auto2)
        print(auto5)
        print(test)

# fonction etoile

if auto1.etoile(auto1) == None:
    print("etoile non définie")
else:
    val = input("Appuyer sur une touche pour test 1 de etoile")
    test = auto1.etoile(auto5)
    if show:
        auto5.show("e1_auto5")
        test.show("e1_etoile")
    else:
        print(auto5)
        print(test)










