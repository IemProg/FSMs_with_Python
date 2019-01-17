#MAROUF Imad Eddine

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
    def accepte(auto, mot):    #Why are we using 2 args (auto ??) 
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        init_states = auto.getListInitialStates()
        final_states = auto.getListFinalStates()
        
        #Des fois on a plusieurs états initialles
        #succ = auto.succ(init_states, mot[0])
        succ = init_states
        for i in mot:
            succ = auto.succ(succ, i)
                    
        for state in succ:
            if state in final_states:
                return True
                
        return False
                    
    @staticmethod
    def estComplet(auto,alphabet):
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        
        states= auto.listStates
        #alphabets = self.getAlphabetFromTransitions()
        #issue concerning automates has puit state : automateA3
        for state in states:
            etiq = []
            for transition in auto.getListTransitionsFrom(state):
                etiq.append(transition.etiquette)
            for l in alphabet:
                if l not in etiq:
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
                    if etiq == transition.etiquette:
                        cmpt+=1
                    if (cmpt >=2):
                        return False
        return True
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """    
        if (auto.estComplet(auto,alphabet) == True):
            return auto
        else:
            auto_copy = copy.deepcopy(auto)
            states = auto_copy.listStates
            
            puit = State(len(states)+1, False, False, "Puit")
            
            for state in states:
                etiq = []
                for l in alphabet:
                    for transition in auto.getListTransitionsFrom(state):
                        etiq.append(transition.etiquette)
                        if l not in etiq:
                            transition = Transition(state, l, puit)
                            auto_copy.addTransition(transition)
            return auto_copy

    @staticmethod
    def determinisation(auto):
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto

        --Pour déterminiser auto, on construit un automat sur P(A),
        on part de l'ensemble des états initiaux.
        """
        alphabet = auto.getAlphabetFromTransitions()
        transitions = []
        Q = []
        E = [[auto.getListInitialStates()]]

        while len(E) > 0:
            S = E[0]
            E.remove(S)
            Q.append(S)
            for l in alphabet:
                temp = []
                for k in S:
                    for t in auto.getListTransitionsFrom(k):
                        if t.etiquette == l and not(t.stateDest in temp):
                            temp.append(t.stateDest)

                if not(temp in Q) and not(temp in E):
                        E.append(temp)
                transitions.append(Transition(S, l, temp))

        #print("E: ", E)
        #print("S: ", S)
        #print("Q ", Q)

        states = []
        i = 0
        for o in Q:
            flag = False
            for p in o:
                #print(p)
                if p[0].fin:
                    flag = True
            s = State(i, i == 0, flag)
            i += 1
            states.append(s)

        transitionsFinales = []
        for m in transitions:
            print(m)
            t = Transition(states[auto.indexOf(Q, m.stateSrc)], m.etiquette, states[auto.indexOf(Q, m.stateDest)])
            transitionsFinales.append(t)

        auto = Automate(transitionsFinales)
        return auto
    @staticmethod
    def complementaire(auto, alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
        auto1 = copy.deepcopy(auto)
        if (auto.estComplet(auto, alphabet) and auto.estDeterministe(auto)):
            for state in auto1.listStates:
                state.fin = not state.fin
            return auto1
        else:
            auto1 = auto.completeAutomate(auto, alphabet)
            auto1 = auto1.determinisation(auto1)
            for state in auto1.listStates:
                state.fin = not state.fin
            return auto1
        
   
    @staticmethod
    def def_help_inter(auto0, auto1, alphabet):
            a=auto0.getListInitialStates()
            b=auto1.getListInitialStates()
            index=1
            l=[]
            lt=[]
            t=[]
            l.append(State(str(index),True,False,"{"+a[0].label+";"+b[0].label+"}"))
            index+=1
            while len(l)>0:
                nouvel_etat=l[0]
                state0=None
                state1=None
                for etat in auto0.listStates:
                    if nouvel_etat.label[1] == etat.label:
                        state0=etat
                if "Etat puit" in nouvel_etat.label[:-2]:
                    for etat in auto0.listStates:
                        if etat.label == "Etat puit":
                            state0=etat
                for etat in auto1.listStates:
                    if nouvel_etat.label[3] == etat.label:
                        state1=etat
                if "Etat puit" in nouvel_etat.label[2:]:
                    for etat in auto1.listStates:
                        if etat.label =="Etat puit":
                            state1=etat
                if state0 == None or state1 == None:
                    print("Erreur")
                    exit()
                for lettre in alphabet:
                    nstate0=auto0.succElem(state0,lettre)
                    nstate1=auto1.succElem(state1,lettre)
                    s2="{"+nstate0[0].label+";"+nstate1[0].label+"}"
                    fait = False
                    etat_fin = None
                    if etat_fin == None :
                            for etat in lt:
                                if etat.label == s2 :
                                    etat_fin = etat
                                    fait=True
                    if etat_fin == None :
                            for etat in l:
                                if etat.label == s2 :
                                    etat_fin = etat
                                    fait=True
                    #Partie a changer pour Union
                    if etat_fin == None:
                        init_dst = False
                        final_dst = False
                        if nstate0[0].init == nstate1[0].init:
                            init_dst = nstate0[0].init
                        else:
                            init_dst= False
                        if nstate0[0].fin == nstate1[0].fin:
                            final_dst = nstate0[0].fin
                        else:
                            final_dst = False
                        etat_fin = State(s2,init_dst,final_dst,s2)
                    if fait==False:
                        l.append(etat_fin)
                    tmp=Transition(nouvel_etat , lettre , etat_fin)
                    t.append(tmp)
                lt.append(l.pop(0))
            return t, lt

    @staticmethod
    def intersection(auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        if not Automate.estDeterministe(auto0):
            auto0 = Automate.determinisation(auto0)

        if not Automate.estDeterministe(auto1):
            auto1 = Automate.determinisation(auto1)

        if not Automate.estComplet(auto0, auto0.getAlphabetFromTransitions()):
            auto0 = Automate.completeAutomate(auto0, auto0.getAlphabetFromTransitions())

        if not Automate.estComplet(auto1, auto0.getAlphabetFromTransitions()):
            auto1 = Automate.completeAutomate(auto1, auto1.getAlphabetFromTransitions())

        auto0.show("auto0.pdf")
        auto1.show("auto1.pdf")

        t, lt = Automate.def_help_inter(auto0, auto1, auto0.getAlphabetFromTransitions())
        a = Automate(t)
        return a

    @staticmethod
    def union(auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        # L1 ∪ L2 est defini par A = (S1 ∪ S2,T1 ∪ T2, I1 ∪ I2, F1 ∪ F2)
        #TODO: complete it
        i = 1
        for state in auto1.listStates:
            state.id = len(auto0.listStates)+i
            auto0.addState(state)
            for transition in auto1.getListTransitionsFrom(state):
                auto0.addTransition(transition)
            i +=1
            
        return auto0
               

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        L1.L2 est d́efini par B = (S1 ∪ S2, T1 ∪ T2 ∪ Tˆ, I, F2)
        
        T = { s −→ i | i ∈ I 2 s ’ i l e x i s t e f ∈ F 1 t q s −→ f ∈ T 1 } .
        """
        #Liste des états de auto2 sans les états initiaux
        liste_etats = [state for state in auto2.listStates if not state.init]

        #l'indice du dernier état d'auto1
        index_last = int(auto1.listStates[-1].id)

        #Changement des ids des états d'auto2
        for etat in liste_etats :
            label = str(int(etat.id) + index_last)
            etat.id = label
            etat.label = label

        liste_transitions_depart = auto2.listTransitions
        liste_transitions = auto1.listTransitions
        liste_etats_final_auto1 = auto1.getListFinalStates()

        #Changement des transitions d'auto2 car on supprime l'état initial
        for transition in liste_transitions_depart :
            if (transition.stateSrc.init) :
                for etat in liste_etats_final_auto1 :
                    liste_transitions.append(Transition(etat,transition.etiquette,transition.stateDest))
            if (transition.stateDest.init) :
                for etat in liste_etats_final_auto1 :
                    liste_transitions.append(Transition(transition.stateSrc,transition.etiquette,etat))

        for etat in auto1.getListFinalStates():
            etat.fin = False
        liste_transitions += auto2.listTransitions
        return Automate(liste_transitions)

    """

        #TO-DO: add transitions towards initial states of auto2
        for state in copy1.getListIntialStates():
            if state.fin == True:
                for init_state2 in auto2.getListIntialState():                  
                #If initial state of auto1 is final ==> initial state of auto2 is initial
                    init_state2.init = True
                    
                
        return
    """
    @staticmethod
    def etoile(auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a

        A partir d’un automate A = (S,T,I,F) acceptant M, on construit un automate qui
        accepte M+ :C=(S, T∪T, I, F) avec T={ s−→i|i∈I et ∃f∈F tq s−→f dans T}.
        """
        liste_transitions = auto.listTransitions
        liste_etats_init = auto.getListInitialStates()

        i = len(liste_transitions) -1

        while (i >= 0) :
            transition = liste_transitions[i]
            if (transition.stateDest.fin):
                for etat_init in liste_etats_init:
                    liste_transitions.append(Transition(transition.stateSrc,transition.etiquette,etat_init))
                liste_transitions.pop(i)
            i-=1

        for etat_init in liste_etats_init:
            etat_init.fin = True

        print(liste_transitions)

        return Automate(liste_transitions)

    def indexOf(self, T, S):
        i = 0
        for t in T:
            if t == S:
                return i
            i += 1
        return -1
## creation d’etats
# s1 : State
s0 = State(0, True, False)
# s1 : State
s1 = State(1, False, False)
# s2 : State
s2 = State(2, False, True)

#(0, a, 0), (0, b, 1), (1, a, 2), (1, b, 2), (2, a, 0) et (2, b, 1).
#t1 = Transition(s0, "a", s0)
#t2 = Transition(s0, "b", s1)
#t3 = Transition(s1, "a", s2)
#t4 = Transition(s1, "b", s2)
#t5 = Transition(s2, "a", s0)
#t6 = Transition(s2, "b", s1)

t1 = Transition(s0, "a", s0)
t2 = Transition(s0, "b", s1)
t3 = Transition(s1, "a", s2)
t4 = Transition(s1, "b", s1)
t5 = Transition(s2, "a", s2)
t6 = Transition(s2, "b", s2)
#t6 = Transition(s2, "a", s1)

t11 = Transition(s0, "a", s0)
t22 = Transition(s0, "b", s0)
t33 = Transition(s0, "a", s1)
t44 = Transition(s1, "b", s2)
t55 = Transition(s2, "a", s2)
t66 = Transition(s2, "b", s2)
t77 = Transition(s1, "a", s1)
#t6 = Transition(s2, "a", s1)


#auto = Automate([t1,t2,t3,t4,t5,t6])
#auto1 = Automate([t1,t2,t3,t4,t5,t6], (s0, s1, s2))
autoA1 = Automate([t1,t2,t3,t4,t5,t6], (s0, s1, s2))
autoA2 = Automate([t11,t22,t33,t44,t55,t66, t77], (s0, s1, s2))
#print(auto1)
#auto1.show("A_Automate.pdf")

#automate = Automate.creationAutomate("automate_text.txt")
#print(automate)

#print(auto.removeTransition(t1))
#print(auto)
#print(auto.addTransition(t1))

#print(auto.removeState(s1))     --True
#s2 = State(0, True, False)

#print(auto.addState(s1))        --True
#print(auto.addState(s2))        --False
#print(auto1.getListTransitionsFrom(s1))

#print(auto1.succ([s0,s1, s2], "a"))
#print("list of States: ", auto1.listStates)
#print("tye of list of States: ",type(auto1.listStates[0].id))
#print("Alphabets: ",auto1.getAlphabetFromTransitions)
"""
print("aaa:", auto1.accepte(auto1,"aaa"))
print("aba:",  auto1.accepte(auto1,"aba"))
print("ba:",  auto1.accepte(auto1,"ba"))
print("bb:",  auto1.accepte(auto1,"bb"))

print("auto1 est Complet 'ab': ", auto1.estComplet(auto1, "ab"))
print("auto1 est Desterministe:", auto1.estDeterministe(auto1))
#auto2.show("B_Automate.pdf")
#print("List of States:", auto1.listStates)
#auto1.show("A_Automate.pdf")
print("----------------")
print("Complete the automate auto1: ")
auto2 = auto1.completeAutomate(auto1, "ab")
print(auto2)
print("est Complet auto2:", auto2.estComplet(auto2, "ab"))
"""
"""
print("---------------------------------------------------------")
print("--------------------automateA1---------------------------")
print("list of States: ", autoA1.listStates)
#print("tye of list of States: ",type(auto1.listStates[0].id))
#print("Alphabets: ",auto1.getAlphabetFromTransitions)

print("aaa:", autoA1.accepte(autoA1,"aaa"))
print("aba:",  autoA1.accepte(autoA1,"aba"))
print("ba:",  autoA1.accepte(autoA1,"ba"))
print("bb:",  autoA1.accepte(autoA1,"bb"))
autoA1.show("A1_Automate.pdf")
print("autoA1 est Complet 'ab': ", autoA1.estComplet(autoA1, "ab"))
print("autoA1 est Desterministe:", autoA1.estDeterministe(autoA1))
print("autoA1 Desterminisation process: ", autoA1.determinisation(autoA1))
"""
print("---------------------------------------------------------")
print("---------------------automateA2--------------------------")
print("list of States: ", autoA2.listStates)
#print("tye of list of States: ",type(auto1.listStates[0].id))
#print("Alphabets: ",auto1.getAlphabetFromTransitions)

#print("aaa:", autoA2.accepte(autoA2,"aaa"))
#print("aba:",  autoA2.accepte(autoA2,"aba"))
#print("ba:",  autoA2.accepte(autoA2,"ba"))
#print("bb:",  autoA2.accepte(autoA2,"bb"))
#print("autoA2 est Complet 'ab': ", autoA2.estComplet(autoA2, "ab"))
autoA2.show("AutomateA2.pdf")
print("autoA2 est Desterministe:", autoA2.estDeterministe(autoA2))
autoA2Deter = autoA2.determinisation(autoA2)
autoA2Deter.show("AutoA2Deter.pdf")
print("autoA2 Desterminisation process: ", autoA2Deter)
print("autoA2Deter est Desterministe ? :", autoA2Deter.estDeterministe(autoA2Deter))


#print("autoA1 comlementaire", autoA1.complementaire(autoA1,"ab"))

A1_Union_A2 = autoA2.union(autoA2, autoA1)
#print("autoA2 Union autoA1: ", autoA2.union(autoA2, autoA1))
#autoA2.show("A1_Union_A2.pdf")

A2_etoile = autoA2.etoile(autoA2)
#print("autoA2 etoile autoA1: ", autoA2.etoile(autoA2))
#autoA2.show("A2_etoile.pdf")

A2_conct_A1 = autoA2.concatenation(autoA1, autoA2)
#print("autoA2 concatenation autoA1", autoA2.concatenation(autoA1, autoA2))
#autoA2.show("A2_conct_A1.pdf")


A2_inter_A1 = autoA2.intersection(autoA1, autoA2)
#print("autoA2 intersection autoA1", autoA2.intersection(autoA1, autoA2))
#autoA2.show("A2_inter_A1.pdf")

"""
print("---------------------------------------------------------")
print("---------------------automateA3--------------------------")
autoA3 = autoA2.completeAutomate(autoA2, "ab")
print("List of States: ", autoA3.listStates)
print(autoA3)
print("autoA3 est Complet 'ab': ", autoA2.estComplet(autoA3, "ab"))
print("autoA3 est Desterministe:", autoA3.estDeterministe(autoA3))
union = autoA1.union(autoA1, autoA2)
print("autoA1 union autoA2': ")
union.show("union.pdf")
#autoA3.show("A3_Automate.pdf")
print("---------------------------------------------------------")


print("---------------------automateA4--------------------------")
autoA4 = Automate.creationAutomate("examples\automateA4.txt")
print("autoA4 est Complet 'ab': ", autoA4.estComplet(autoA4, "ab"))
print("autoA4 est Desterministe:", autoA4.estDeterministe(autoA4))
autoA4.show("A4_Automate.pdf")
print("---------------------------------------------------------")

print("---------------------automateA5--------------------------")
autoA5 = Automate.creationAutomate("examples\automateA5.txt")
print("autoA5 est Complet 'ab': ", autoA5.estComplet(autoA4, "ab"))
print("autoA5 est Desterministe:", autoA5.estDeterministe(autoA4))
autoA5.show("A5_Automate.pdf")

print("---------------------------------------------------------")
print("---------------------automateA6--------------------------")
autoA6 = Automate.creationAutomate("examples\automateA6.txt")
print("autoA6 est Complet 'ab': ", autoA6.estComplet(autoA6, "ab"))
print("autoA6 est Desterministe:", autoA6.estDeterministe(autoA6))
autoA9.show("A6_Automate.pdf")
print("---------------------------------------------------------")

print("---------------------automateA7--------------------------")
autoA7 = Automate.creationAutomate("examples\automateA7.txt")
print("autoA7 est Complet 'ab': ", autoA7.estComplet(autoA7, "ab"))
print("autoA7 est Desterministe:", autoA7.estDeterministe(autoA7))
autoA7.show("A7_Automate.pdf")

print("---------------------------------------------------------")
print("---------------------automateA8--------------------------")
autoA8 = Automate.creationAutomate("examples\automateA8.txt")
print("autoA8 est Complet 'ab': ", autoA8.estComplet(autoA8, "ab"))
print("autoA8 est Desterministe:", autoA8.estDeterministe(autoA8))
autoA8.show("A8_Automate.pdf")
print("---------------------------------------------------------")

print("---------------------automateA9--------------------------")
autoA9 = Automate.creationAutomate("examples\automateA9.txt")
print("autoA9 est Complet 'ab': ", autoA5.estComplet(autoA9, "ab"))
print("autoA9 est Desterministe:", autoA5.estDeterministe(autoA9))
autoA9.show("A9_Automate.pdf")
print("---------------------------------------------------------")

print("---------------------automateA10-------------------------")
autoA10 = Automate.creationAutomate("examples\automateA10.txt")
print("autoA10 est Complet 'ab': ", autoA5.estComplet(autoA4, "ab"))
print("autoA10 est Desterministe:", autoA5.estDeterministe(autoA4))
autoA10.show("A10_Automate.pdf")
"""

