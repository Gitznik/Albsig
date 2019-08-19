#!/usr/bin/env python
# coding: utf-8

# In[4]:


class StudentIn():
    """
    Speichert die Daten einer Student*in.
    Attribute: ...
    Methoden: ...
    """
    arbeitsmoral = "Hervorragend"
    def __init__(self, vorname, nachname, noten):
        self.vorname = vorname
        self.nachname = nachname
        self.noten = noten
        
    def notenschnitt(self):
        notenschnitt = sum(self.noten) / len(self.noten)
        return notenschnitt


# In[5]:


print(StudentIn.__doc__)


# In[6]:


sabine = StudentIn(vorname = "sabine", nachname = "schusster", noten = [1,3,2,1,3])
type(sabine)


# In[7]:


print("Vorname: " + str(sabine.vorname))
print("Nachname: " + str(sabine.nachname))
print("Noten: " + str(sabine.noten))
print("Arbeitsmoral: " + str(sabine.arbeitsmoral))


# In[8]:


sabine.nachname = "schuster"
print(sabine.nachname)


# In[9]:


notenschnitt = sabine.notenschnitt()
print("Notenschnitt von " + str(sabine.vorname) + " " + str(sabine.nachname) + " ist: " + str(notenschnitt))


# In[10]:


stefan = StudentIn("stefan", "schmidt", [2,4,3,1,2])
stefan.arbeitsmoral = "Mittelmäßig"

print("Vorname: " + str(stefan.vorname))
print("Nachname: " + str(stefan.nachname))
print("Noten: " + str(stefan.noten))
print("Arbeitsmoral: " + str(stefan.arbeitsmoral))

print("Notenschnitt von " + str(stefan.vorname) + " " + str(stefan.nachname) + " ist: " + str(stefan.notenschnitt()))

