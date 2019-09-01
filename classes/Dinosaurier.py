#!/usr/bin/env python
# coding: utf-8

# # Uebungsaufgabe Klassenprogrammierung

# ## Klassendefinition

# In[2]:


import pandas as pd


# In[29]:


class Dinosaurier():
    """
    Speichert die Daten eines Dinosauriers.
    Attribute: 
        name: Name des Dinosauriers
        alter: Alter des Dinosauriers in millionen Jahren
        gewicht: Gewicht des Dinosauriers in t
        hoehe: Hoehe bzw. Laenge des Dinosauriers in m, je nachdem was groeßer ist
    Methoden:
        BMI: Errechnet den BMI des Dinosauriers. Gibt einen String der den BMI beschreibt zurück
    """
    
    def __init__(self, name, alter, gewicht, hoehe):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.hoehe = hoehe
        
    def bmi(self):
        bmi = ((self.gewicht * 1000) / (self.hoehe * self.hoehe))
        bmi = round(bmi, 2)
        print("Der BMI von " + self.name + " beträgt " + str(bmi) + 
              ". Fuer " + str(self.alter) + " millionen Jahre gar nicht so schlecht!")
        


# ## Definition der Objekte

# In[30]:


bronto = ["Brontosaurus", 157, 38, 27]
trex = ["T-Rex", 68, 14, 12]
trice = ["Triceratops", 66, 12, 9]

brontosaurus = Dinosaurier(bronto[0], bronto[1], bronto[2], bronto[3])
tyrannosaurus = Dinosaurier(trex[0], trex[1], trex[2], trex[3])
triceratops = Dinosaurier(trice[0], trice[1], trice[2], trice[3])


# In[31]:


brontosaurus.bmi()


# In[32]:


tyrannosaurus.bmi()


# In[33]:


triceratops.bmi()

