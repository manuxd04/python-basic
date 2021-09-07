# For-løkke

Vi bruker løkker for å gå gjennom en sekvens av verdier.

Dette kan være elementene i en liste:

```python
>>> for elev in elever:
...     elev
... 
'Harry'
'Hermine'
'Ronny'
```

Men også bokstavene i en tekststreng:

```python
>>> for bokstav in "abcde":
...     bokstav
... 
'a'
'b'
'c'
'd'
'e'
```

Vi kan også lage en sekvens av tall med funksjonen `range()`:
```python
>>> for tall in range(10):
...     tall
... 
0
1
2
3
4
5
6
7
8
9
```