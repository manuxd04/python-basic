# List

En `List` er en liste av andre verdier. Det kan foreksempel være en liste over navn på elever i en klasse. Vi oppretter en liste ved å skrive verdiene mellom to klammer `[]`

```python
elever = ["Harry", "Hermine", "Ronny"]
```

Som med andre datatyper kan vi bruke noen, men ikke alle operatorer på lister. Vi kan legge sammen to lister:
```python
>>> ["Harry"] + ["Ronny"]
['Harry', 'Ronny']
```

Men vi kan ikke trekke dem fra hverandre:

```python
>>> ["Harry", "Ronny"] - ["Ronny"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'list'
```

**Forsøk i en interaktiv seksjon, hva gjør ulike operasjoner med en liste?**

## Hente ut

Vi kan hente ut verdier fra listen på `index`, hvilken plassering det har i listen:
```python
>>> elever[0]
'Harry'
```

Merk at den første verdien i listen har plasseringen `0`, ikke `1`. Datamaskiner liker å telle fra null.


## Innebygde metoder i Lister

Lister har mange nyttige innebygde metoder, som List.sort() som sorterer en liste. Hvis listen inneholder strenger, blir listen sortert alfabetisk:
```python
>>> elever
['Harry', 'Ronny', 'Hermine', 'Draco']
>>> elever.sort()
>>> elever
['Draco', 'Harry', 'Hermine', 'Ronny']
```

Fullstending oversikt over innebygde metoder i lister finner du i Python-dokumentasjonen [her](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).




