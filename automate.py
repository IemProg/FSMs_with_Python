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
            succElem = self.succElem(listStates[i], lettre)
            for se in succElem :
                if se not in list_succ:
                    list_succ.append(se)
                
        return list_succ




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto, mot):    #why are we using 2 args (auto ??) 
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        
        init_states = auto.getListInitialStates()
        final_states = auto.getListFinalStates()
        states = auto.listStates

        for m in mot:
            for state in states:
                succ_states = auto.succ(state, m)
            

        return True
                   

        
    @staticmethod
    def estComplet(auto,alphabet):
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        
        states= auto.listStates
        #alphabets = self.getAlphabetFromTransitions()
        
        for l in alphabet:
            for state in states:
                for transition in auto.getListTransitionsFrom(state):
                    if l != transition.etiquette:
                        return False
        return True
        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        states= auto.listStates
        #transitions = [auto.getListTransitionsFrom(state) for state in states)]
        etiquetes = auto.getAlphabetFromTransitions()       #List with no duplication
        
        for etiq in etiquetes:
            for state in states:
                cmpt = 0
                for transition in auto.getListTransitionsFrom(state):
                    if etiq == transition.etiquete:
                        cmpt+=1
                    if (cmpt >=2):
                        return False

        return True
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        auto_copy = copy.deepcopy(auto)
        states= auto.listStates
               
        if (estComplet(auto,alphabet) == True):
            print("Deja complet")
        else:
            puit = State("Puit", False, False)
            auto_copy.addState(puit)
            for l in alphabet:
                for state in states:
                    for transition in auto.getListTransitionsFrom(state):
                        if l != transition.etiquette:
                            transition = Transition(l, state, puit)
                            auto_copy.addTransition(state, l, puit)
                        etiquettes_puit =[transition.etiquette for transition in auto.getListTransitionsFrom(puit)]
                        if l not in etiquettes_puit:
                            auto_copy.addTransition(puit, l, puit)
        return auto_copy

       

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
#print(auto1)
auto1.show("A_Automate.pdf")

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
print("list of States: ",auto1.listStates)
#print("tye of list of States: ",type(auto1.listStates[0].id))
#print("Alphabets: ",auto1.getAlphabetFromTransitions)

#print("aaa:", auto1.accepte(auto1,"aaa"))
#print("aba:", auto1.accepte(auto1,"aba"))
#print("aabb:", auto1.accepte(auto1,"aabb"))
#print("baabaa:", auto1.accepte(auto1,"baabaa"))

#print("est Complet:",auto1.estComplet(auto1, "ab"))
