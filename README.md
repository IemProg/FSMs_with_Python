# FSMs_with_Python
Finite State Machines with Python, a script implements FSMs 

<i><b>1\ What is FSM?</b><i/>

According to Wiki:
      A finite-state machine (FSM) or finite-state automaton (FSA, plural: automata), finite automaton, 
      or simply a state machine, is a mathematical model of computation. It is an abstract machine that can be in exactly one of 
      a finite number of states at any given time. The FSM can change from one state to another in response to some external inputs; 
      the change from one state to another is called a transition. An FSM is defined by a list of its states, its initial state, 
      and the conditions for each transition. Finite state machines are of two types – deterministic finite state machines and non-deterministic
      finite state machines.[1] A deterministic finite-state machine can be constructed equivalent to any non-deterministic one."


<i><b>2\ Scripting an FSM with Python:</b><i/>

<b>Automate.py</b>: by using this file you can create FSMs, here a simple code:</br>
      Where the previous variables are: <br/>
      
      # Creation of states
       s1 : State 
       s1 = State(1, True, False) 
       s2 = State(2, False, True) 
       # Creation of transitions 
       t1 = Transition(s1,"a",s1)
       # t2 : Transition 
       t2 = Transition(s1,"a",s2) 
       # t3 : Transition 
       t3 = Transition(s1,"b",s2) 
       # t4 : Transition 
       t4 = Transition(s2,"a",s2)
       # t5 : Transition 
       t5 = Transition(s2,"b",s2)
       auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
      
      print(auto)               #In order to show the FSM
      auto.show("A_ListeTrans") #In order to save it as a File "A_ListeTrans.pdf"


1 -  accepte(auto, mot):    <br/>

        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        
2 -   estComplet(auto,alphabet): <br/>

        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
3 - estDeterministe(auto) :<br/>

        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        
4 - completeAutomate(auto,alphabet) :<br/>

        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """    
        
5 - determinisation(auto): <br/>

        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        --Pour déterminiser auto, on construit un automat sur P(A),
        on part de l'ensemble des états initiaux.
        """
        
6 - complementaire(auto,alphabet): <br/>

        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
7 - intersection(auto0, auto1): <br/>

        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        
8 - union(auto0, auto1): <br/>

        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        
9 - concatenation (auto1, auto2): <br/>

        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        L1.L2 est d́efini par B = (S1 ∪ S2, T1 ∪ T2 ∪ Tˆ, I, F2)
        T = { s −→ i | i ∈ I 2 s ’ i l e x i s t e f ∈ F 1 t q s −→ f ∈ T 1 } .
        """
10 - etoile(auto): <br/>

        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a

        A partir d’un automate A = (S,T,I,F) acceptant M, on construit un automate qui
        accepte M+ :C=(S, T∪T, I, F) avec T={ s−→i|i∈I et ∃f∈F tq s−→f dans T}.
        """
