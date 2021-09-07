# Betingelser (If og sånt)

Programmene våre kan ikke få til så mye hvis det samme skjer hver gang. Derfor bruker vi "conditionals", eller betingelser, for å styre hva som skal skje i ulike tilfeller.

Vi kan skrive dette som en `if`. Som navnet antyder betyr dette bare "hvis noe er sant". Så i Python kan vi si:

```python
if True:
    print("Dette er alltid sant!")
```

Vi kan sjekke om ulike ting er sant. På tall kan vi sjekke om noe er større eller mindre med krokodillen (som alltid spiser det største tallet) `>`. Ofte vil vi gjøre enten en ting eller en annen, da bruker vi `if` og `else`, altså hvis-ellers.

```python
if alder >= 18:
    print("Du kan ta lappen!")
else:
    print("Du er for ung for lappen.")
```

Hvis vi vil legge til støtte for moped også kan vi sjekke flere ting etter hverandre med `elif` som er kort for "else if", altså ellers hvis.

```python
if alder >= 18: 
    print("Du kan ta lappen for bil")
elif alder >= 16:
    print("Du kan ta lappen for moped")
else:
    print("Du kan i det minste sykle")
```
