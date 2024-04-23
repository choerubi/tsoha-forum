# Keskustelusovellus

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.

Kyseessä on ensimmäinen kurssilla valmiiksi annetuista esimerkeistä.

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

## Välipalautukset

Välipalautus 2:

Käyttäjä voi tarkastella sovelluksen kirjautumis- ja rekisteröintisivua, mutta ei pääse vielä luomaan tunnuksia tai kirjautumaan sisään.

Välipalautus 3:

Käyttäjä voi luoda tunnukset ja kirjautua sisään. Jos käyttäjä on kirjautuneena sisään, hänet ohjataan foorumisivulle.
