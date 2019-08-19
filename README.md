
# Class-Tutorial Albsig


```python
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
```


```python
print(StudentIn.__doc__)
```

    
        Speichert die Daten einer Student*in.
        Attribute: ...
        Methoden: ...
        
    


```python
sabine = StudentIn(vorname = "sabine", nachname = "schusster", noten = [1,3,2,1,3])
type(sabine)
```




    __main__.StudentIn




```python
print("Vorname: " + str(sabine.vorname))
print("Nachname: " + str(sabine.nachname))
print("Noten: " + str(sabine.noten))
print("Arbeitsmoral: " + str(sabine.arbeitsmoral))
```

    Vorname: sabine
    Nachname: schusster
    Noten: [1, 3, 2, 1, 3]
    Arbeitsmoral: Hervorragend
    


```python
sabine.nachname = "schuster"
print(sabine.nachname)
```

    schuster
    


```python
notenschnitt = sabine.notenschnitt()
print("Notenschnitt von " + str(sabine.vorname) + " " + str(sabine.nachname) + " ist: " + str(notenschnitt))
```

    Notenschnitt von sabine schuster ist: 2.0
    


```python
stefan = StudentIn("stefan", "schmidt", [2,4,3,1,2])
stefan.arbeitsmoral = "Mittelmäßig"

print("Vorname: " + str(stefan.vorname))
print("Nachname: " + str(stefan.nachname))
print("Noten: " + str(stefan.noten))
print("Arbeitsmoral: " + str(stefan.arbeitsmoral))

print("Notenschnitt von " + str(stefan.vorname) + " " + str(stefan.nachname) + " ist: " + str(stefan.notenschnitt()))
```

    Vorname: stefan
    Nachname: schmidt
    Noten: [2, 4, 3, 1, 2]
    Arbeitsmoral: Mittelmäßig
    Notenschnitt von stefan schmidt ist: 2.4
    
