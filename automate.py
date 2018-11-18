# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from parser import *
from itertools import product
from automateBase import AutomateBase



class Automate(AutomateBase):
        
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ(self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        list_succ = []
        for i in range(len(listStates)):
            list_succ.append(self.succElem(listStates[i], lettre))
        #Duplicated items in the list sometimes !!!
        return my_set




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        alphabets = list(mot)
        init_states = self.getListInitialStates()
        final_states = self.getListFinalStates()
        for l in mot:
            for i in init_states:
                for
        return


    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        return 


        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        return
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        return

       

    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        return
        
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
              
   
    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return
        

   
       

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return

## creation d’etats
# s1 : State
s0 = State(0, True, False)
# s1 : State
s1 = State(1, False, False)
# s2 : State
s2 = State(2, False, True)

#(0, a, 0), (0, b, 1), (1, a, 2), (1, b, 2), (2, a, 0) et (2, b, 1).
t1 = Transition(s0, "a", s0)
t2 = Transition(s0, "b", s1)
t3 = Transition(s1, "a", s2)
t4 = Transition(s1, "b", s2)
t5 = Transition(s2, "a", s0)
t6 = Transition(s2, "b", s1)


auto = Automate([t1,t2,t3,t4,t5,t6])
auto1 = Automate([t1,t2,t3,t4,t5,t6], (s0, s1, s2))
print(auto1)
#auto1.show("A_Automate.pdf")

#automate = Automate.creationAutomate("automate_text.txt")
#print(automate)

#print(auto.removeTransition(t1))
#print(auto)
#print(auto.addTransition(t1))

#print(auto.removeState(s1))     --True
s2 = State(0, True, False)       
#print(auto.addState(s1))        --True
#print(auto.addState(s2))        --False
#print(auto1.getListTransitionsFrom(s1))

print(auto1.succ([s0,s1, s2], "a"))
