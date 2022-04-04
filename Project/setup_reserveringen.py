from beheer_reserveringen import db, Huis, Soort, Gast, Boeking

#Maak de database en het bestand aan
db.create_all()

vier_personen = Soort(4, 100)
zes_personen = Soort(6, 150)
acht_personen = Soort(8, 250)

db.session.add_all([vier_personen, zes_personen, acht_personen])
db.session.commit()

alle_soorten = Soort.query.all()
print(*alle_soorten, sep='\n')

trekkershut = Huis("trekkershut", 1)
bungelow = Huis("bungelow", 2)
villa = Huis("villa", 3)

db.session.add_all([trekkershut, bungelow, villa])
db.session.commit()

alle_huizen = Huis.query.all()
print("--------------------------------------------------------------------------")
print(*alle_huizen, sep="\n")

marnix = Gast("Marnix", "geheimwachtwoord1")
joeke = Gast("Joeke", "geheimwachtwoord2")

db.session.add_all([marnix, joeke])
db.session.commit()

alle_gasten = Gast.query.all()
print("--------------------------------------------------------------------------")
print(*alle_gasten, sep="\n")

boeking1 = Boeking(1, 1, 1)
boeking2 = Boeking(1, 3, 2)
boeking3 = Boeking(2, 2, 2)

db.session.add_all([boeking1, boeking2, boeking3])
db.session.commit()

alle_boekingen = Boeking.query.all()
print("--------------------------------------------------------------------------")
print(*alle_boekingen, sep="\n")