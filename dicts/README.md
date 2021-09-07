# Dictonary

Et `dict` er en måte å lagre verdier i par av nøkkel og verdi.

Den klassiske telefonkatalogen er et eksempel på et dictonary: vi slår opp på et navn og får ut et telefonnummer. Telefonkatalogen består altså av flere par av navn og telefonnummer. Vi kaller navnet, verdien vi slår opp med, for `key`. Vi kaller telefonnummeret, verdien vi henter ut, for `value`. 

De fleste programmeringsspråk har denne datatypen, men den har ulike navn. I JavaScript heter den Object, og i Java heter den Map. 

Å opprette et dictonary i Python kan ligne litt på en liste. Mellom klammene, skriver vi parene etter hverandre.

```python
telefonkatalog = {
    "harry": "12345678",
    "ronny": "55512345",
    "hermine": "55543422"
}
```


Vi slår opp i katalogen ved å skrive inn `key` der vi i en liste ville skrevet `index`, og får tilbake `value`.
```python
>>> telefonkatalog["harry"]
'1234'
```