# Keskustelusovellus

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuudet:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen pääsivulla listan keskustelualueista, alueen luoneen käyttäjän käyttäjänimen ja luomisen ajankohdan sekä luotujen alueiden määrän.
- Käyttäjä voi siirtyä keskustelualueille, joissa käyttäjä näkee alueille luodut ketjut ja ketjuihin lähetetyt viestit. Käyttäjä näkee myös ketjujen ja viestien lähettäjien käyttäjänimet, luomisajat sekä ketjujen ja viestien määrän.
- Käyttäjä voi luoda uusia keskustelualueita ja ketjuja, ja käyttäjä voi lähettää ketjuihin uusia viestejä.
- Käyttäjä voi etsiä kaikki keskustelualueet, joiden osana on annettu sana.
- Ylläpitäjä voi poistaa keskustelualueita.

Kyseessä on mukautettu versio ensimmäisestä kurssilla valmiiksi annetusta esimerkistä.

## Ohjeet sovelluksen testaamiseen

1 Kloonaa repositorio omalle koneellesi seuraavasti:
```
$ git clone https://github.com/choerubi/tsoha-forum
```

2 Lisää hakemiston juureen .env-tiedosto, josta löytyy seuraavat muuttujat:
```
SECRET_KEY=<salainen-avain>
DATABASE_URL=postgresql:///<tietokannan-nimi>
```

Voit luoda salaisen avaimen seuraavasti:
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```

Tietokannan nimi on käyttäjän tunnus, joka näkyy psql-tulkin rivien alussa, esim:
```
choerubi=# \dt
DATABASE_URL=postgresql:///choerubi
```

3 Aktivoi Pythonin virtuaaliympäristö hakemistossa seuraavasti:
```
$ cd tsoha-forum
$ python3 -m venv venv
$ source venv/bin/activate
```

4 Asenna tarvittavat kirjastot seuraavalla komennolla:
```
(venv) $ pip install -r requirements.txt
```
   
5 Määritä tietokanta seuraavalla komennolla:
```
(venv) $ psql < schema.sql
```

6 Käynnistä sovellus seuraavasti:
```
(venv) $ flask run
```
