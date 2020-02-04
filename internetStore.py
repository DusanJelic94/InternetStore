import os
import datetime

pozdravna_poruka = """\
       Dobrodosli u prodavnicu gaming racunara! :)
	   Adresa: Momcila Tapavice 8, Novi Sad
	   Zelimo vam ugodnu kupovinu, pcg team! 
		  
"""

Ulogovan = []

def Citanje_iz_baze():
	korisnici = open('zaposleni.txt', 'r')
	korisnike_koji_ce_se_logovati = []
	for linija_teksta in korisnici.readlines():
		l = linija_teksta.strip().split('-')
		korisnik = {'KorisnickoIme': l[0], 'Lozinka': l[1], 'Ime': l[2], 'Prezime': l[3], 'Uloga': l[4] }
		korisnike_koji_ce_se_logovati.append(korisnik)
	korisnici.close()
	return korisnike_koji_ce_se_logovati
	
def Logovanje():
	global Ulogovan
	os.system('cls')
	print(pozdravna_poruka)
	print("Molim vas, ulogujte se!")
	print('-  -  -  -  -  -  -  -  -  - ')
	ListaKorisnika = Citanje_iz_baze()
	Ulogovan = []
	while True:
		usser = input("Vase korisnicko ime je:")
		for korisnik in range(len(ListaKorisnika)):
			korisnik = ListaKorisnika[korisnik]
			if korisnik['KorisnickoIme'] == usser:
				passw = input('Vasa lozinka je:')
				if korisnik['Lozinka'] == passw:
					Ulogovan.append(korisnik['Ime'])
					Ulogovan.append(korisnik['Prezime'])
					Ulogovan.append(korisnik['Uloga'])
					return Ulogovan

def Podaci_za_menadzere():
	a = ['Unos', 'Uklanjanje', 'Promena','Biranje']
	print("Opcije za menadzere",'.'*50)
	for i in range(len(a)): 
		print ('\t'+str(i+1)+'....'+a[i])
	odg = int(input("Unesi odgovor: "))
	if odg == 1:	
		Unos()
	elif odg == 2:
		print("U toku je Uklanjanje..")
		Uklanjanje()
	elif odg == 3:
		print("U toku je Promena..")
		Promena()
	elif odg == 4:
		Biranje()
	else:
		print("Odgovarajuca opcija nije uneta. ")
			
		
def Podaci_za_prodavce():
	a = ['Unos', 'Uklanjanje', 'Promena','Biranje', 'Sastavljanje uredjaja','Izdavanje racuna']
	for i in range(len(a)): 
		print (i+1, a[i])
	odg = int(input("Unesi odgovor: "))
	if odg == 1:	
		Unos()
	elif odg == 2:
		print("Uklanjanje... ")
		Uklanjanje()
	elif odg == 3:
		print("Promena....")
		Promena()
	elif odg == 4:
		Biranje()
	elif odg == 5:
		PromenaUredjaja()
	elif odg == 6:
		prodato=Lista_prodatih_proizvoda()
		racun, suma=Racun(prodato)
		PrintRacuna(Ulogovan, racun, suma)
	else:
		print("Odgovarajuca opcija nije uneta. ")

def Uklanjanje():
	os.system('cls')
	global Ulogovan
	print ('     --++   Opcije za uklanjanje.Ukloni:   --++ ')
	print ('     --++   1 - Komponentu               --++ ')
	print ('     --++   2 - Kategoriju               --++ ')
	print ('     --++   3 - Uredjaj                  --++ ')
	print ('     --++   0 - Vracanje u meni          --++ ')
	opcija = input('Unesite opciju:')
	while opcija != '0':
		if opcija == '1':
			Uklanjanje_komponenata()
		elif opcija == '2':
			Uklanjanje_kategorije()
		elif opcija == '3':
			Uklanjanje_uredjaja()
		else:
			opcija = input('Morate izabrati ponudjene opcije.')
	if opcija == '0':
		if Ulogovan[2] == 'prodavac':
			Podaci_za_prodavce()
		if Ulogovan[2] == 'menadzer':
			Podaci_za_menadzere()
			
			
def Ucitaj(a):		
	if a == 'komp':
		komponente = open('komponente.txt', 'r')
		L=[]
		for red in komponente.readlines():
			l = red.strip().split('|')
			komponenta={'Naziv': l[0], 'Cena': l[1], 'Raspoloziva kolicina': l[2], 'Opis': l[3], 'Kategorija': l[4], 'Obrisano': l[5]}
			L.append(komponenta)
		komponente.close()   
		return L		
	else:
		kategorije = open('kategorije.txt', 'r')
		L=[]
		for red in kategorije.readlines():
			l=red.strip().split('|')
			kategorija={'Naziv': l[0], 'Opis': l[1] }
			L.append(kategorija)
		return L
		kategorije.close()
		
def Promena():
	os.system('cls')
	print ('     --++  Opcije za promenu.Promeni:    --++ ')
	print ('     --++   1 - Komponentu               --++ ')
	print ('     --++   2 - Kategoriju               --++ ')
	print ('     --++   3 - Uredjaj                  --++ ')
	print ('     --++   0 - Vracanje u meni          --++ ')
	opcija = input('Unesite opciju:') 
	while opcija != '0':
		if opcija == '1':
			Promena_komponenata()
		elif opcija == '2':
			Izmenjivanje_kategorija()
		elif opcija == '3':
			PromenaUredjaja()
		else:
			opcija=input('Niste izabrali ponudjenu opciju. Odaberite opciju iz menija.')
	if opcija == '0':
		if Ulogovan[2] == 'prodavac':
			Podaci_za_prodavce()
		if Ulogovan[2] == 'menadzer':
			Podaci_za_menadzere()
def Biranje():
	os.system('cls')
	global Ulogovan
	print ('     --++  Opcije za biranje.Izaberite:    --++ ')
	print ('     --++                                  --++ ')
	print ('     --++   1 - Komponentu                 --++ ')
	print ('     --++   2 - Kategoriju                 --++ ')
	print ('     --++   3 - Uredjaj                    --++ ')
	print ('     --++   0 - Vracanje u meni            --++ ')
	opcija = input('Unesite opciju:')
	while opcija!='0':
		if opcija=='1':
			Biranje_komponenata()
		elif opcija=='2':
			Biranje_kategorija()
		elif opcija=='3':
			print ('Pretraga uredjaja')
			Biranje_uredjaja()
		else:
			opcija=input('Niste izabrali ponudjenu opciju. Odaberite opciju iz menija.')
	if opcija=='0':
		if Ulogovan[2]=='prodavac':
			Podaci_za_prodavce()
		if Ulogovan[2]=='menadzer':
			Podaci_za_menadzere()
def PromenaUredjaja():
	Lista = Ucitavanje_komp_za_listu()
	naziv = input('Naziv novog uredjaja je: ')
	opis = input('Opis novog uredjaja je: ')
	Komponente = []
	komponente = ''
	Stampanje_komp_iz_liste()
	dodaj = input('Unesite naziv komponente iz date liste komponenata, u suprotnom za kraj pritisnite x: ')
	while dodaj != 'x':
		Komponente.append(dodaj)
		dodaj = input('Unesite naziv komponente iz date liste komponenata, u suprotnom za kraj pritisnite x: ')
	if dodaj == 'x':
		opcija = input('Da sacuvate novo uredjaj odaberite s, za vracanje u meni x: ')
	for kompon in Lista:
		for komponenta in Komponente:
			if komponenta == kompon['Naziv']:
				komponente += komponenta+'-'                            
	uredjaj=naziv+'|'+opis+'|'+komponente+'|'+'False\n'
	while opcija != 's':
		if opcija == 'x':
			Podaci_za_prodavce()
		else:
			opcija=input('Odgovarajuca opcija nije uneta. Odaberite s za snimanje, u suprotnom x za nazad u meni. Odaberite opciju: ')
	uredjaji = open('uredjaji.txt', 'a')
	uredjaji.write(uredjaj)
	uredjaji.close()
	komand = input('Snimili ste novi uredjaj. Za sastavljanje novog uredjaja odaberite n, u suprotnom za povratak u meni x. Unesite novu opciju: ')
	while komand != 'n':
		if komand == 'x':
			Podaci_za_prodavce()
		else:
			komand = input('Odgovarajuca opcija nije uneta - odaberite n za sastavljanje novog uredjaja, u suprotnom x za povratak. Odaberite opciju: ')
	if komand == 'n':
		PromenaUredjaja()    

	

def VremeIDatum():
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datum	
def Pocetak(ko_je_ulogovan):
	if ko_je_ulogovan != []:
		print(ko_je_ulogovan)
		if str(ko_je_ulogovan[2]) == 'menadzer' :
			print ("Menadzer je uspesno ulogovan.")
			Podaci_za_menadzere()
		elif str(ko_je_ulogovan[2]) == 'prodavac' :
			print ("Prodavac je uspesno ulogovan.")
			Podaci_za_prodavce()
		else:
			print ("Niste uneli odgovarajuce podatke.Pokusajte ponovo.")
	else:
		print("Doslo je do greske. Korisnik nije prepoznatljiv. Pokusajte ponovo. ")
		Pocetak(Logovanje())
	
def Unos():
	os.system('cls')
	global Ulogovan
	print ('     --++   Odaberite opciju:  --++     ')
	Menu = ['Nazad u meni', 'Komponente', 'Kategorije']
	for i in range(len(Menu)): 
		print (i, Menu[i])
	opcija = int(input('Unesite opciju:'))
	while opcija != 0:
		if opcija == 1:
			Unosenje_komp()
		elif opcija == 2:
			Unos_kategorije()
		else:
			opcija = int(input('Odgovarajuca opcija nije uneta. Odaberite opciju iz menija.'))
	if opcija == 0:
		if Ulogovan[2] == 'prodavac':
			print(" ")
			Podaci_za_prodavce()
		if Ulogovan [2] == 'menadzer':
			print(" ")
			Podaci_za_menadzere()
# Komponente krecu odavde..:
def Uklanjanje_komponenata():
    os.system('cls')
    Stampanje_komp_iz_liste()
    naziv = input('Za Uklanjanje komponente unesite njen naziv, u suprotnom za nazad x: ')
    ListaKomponenata = Ucitaj('komp')
    while naziv != 'x':
        for i in range(len(ListaKomponenata)):
            m = ListaKomponenata[i]
            if m['Naziv']==naziv:
                opcija=input('Morate potvrditi, da biste obrisali.Odaberite o za Uklanjanje, u suprotnom x za nazad: ')
                if opcija == 'o':
                    ListaKomponenata[i]={'Naziv': m['Naziv'], 'Cena': m['Cena'], 'Raspoloziva kolicina': m['Raspoloziva kolicina'], 'Opis': m['Opis'], 'Kategorija': m['Kategorija'], 'Obrisano': 'True' } 
                    Lista_komponenata(ListaKomponenata)
                    komand = input('Operacija izvrsena. Uspesno ste obrisali komponentu. Za Uklanjanje nove komponente odaberite n, u suprotnom za nazad x: ')
                    while komand != 'x':
                        if komand == 'n':
                            Uklanjanje_komponenata()
                        else:
                            komand = input('Uneta je pogresna opcija, Unesite n za Uklanjanje nove komponente, u suprotnom x za nazad! Unesite novu : ')
                    if komand == 'x':
                        Uklanjanje()
                elif opcija == 'x':
                    Uklanjanje()
                else:
                    opcija = input('Uneli ste pogresnu opciju. Unesite o za uklanjanje, u suprotnom x za nazad! Unesite novu opciju: ')
        else: naziv=input('Naziv komponente koju ste uneli ne postoji. Unesite tacan naziv komponente! Unesite x za kraj: ')
    if naziv == 'x':
        Uklanjanje()	
def Promena_komponenata():
    Stampanje_komp_iz_liste()
    naziv = input('Unesite tacan naziv komponente koju zelite da promenite, u suprotnom za kraj x: ')
    ListaKomponenata = Ucitavanje_komp_za_listu()
    while naziv != 'x':
        for p in range(len(ListaKomponenata)):
            m = ListaKomponenata[i]
            if m['Naziv']==naziv:
                opcija = input('Morate potvrditi za promenu komponente. Odaberite p za promenu, u suprotnom x za nazad: ')
                if opcija == 'p':
                    cena = input('Nova cena komponente je:')
                    kolicina = input('Nova kolicina komponente je:')
                    opis = input('Novi opis komponente je:')
                    kategorija = input('Nova kategorija komponente je:')
                    ListaKomponenata[i]={'Naziv': naziv, 'Cena': cena, 'Raspoloziva kolicina': kolicina, 'Opis': opis, 'Kategorija': kategorija, 'Obrisano': 'False' } 
                    Lista_komponenata(ListaKomponenata)
                    komand = input('Uspesno ste promenili komponentu. Za promenu nove komponente odaberite n, u suprotnom za nazad x: ')
                    while komand != 'x':
                        if komand == 'n':
                            Promena_komponenata()
                        else:
                            komand = input('Pogresna opcija. Odaberite n za Uklanjanje nove komponente, u suprotnom x za nazad! Unesite novu opciju: ')
                    if komand == 'x':
                        Promena()
                elif opcija == 'x':
                    Promena()
                else:
                    opcija = input('Uneli ste pogresnu opciju. Odaberite o za uklanjanje, u suprotnom x za nazad! Unesite novu opciju: ')
        else: naziv = input('Izvinjavamo se, naziv komponente koju ste uneli ne postoji. Pokusajte opet sa novim nazivom ili unesite x za kraj: ')
    if naziv == 'x':
        Promena()
def Lista_komponenata(ListaKomponenata):
	komponet = open('kom_backup.txt','w')
	komp=open('komponente.txt', 'r')
	Lista_stari_fajl = Ucitavanje_komp_za_listu()
	for m in Lista_stari_fajl:
		komponet.write(m['Naziv']+'|'+m['Cena']+'|'+m['Raspoloziva kolicina']+'|'+m['Opis']+'|'+m['Kategorija']+'|'+m['Obrisano']+'\n')
	komp.close()
	komponet.close()
	komponente = open('komponente.txt', 'w')
	for m in ListaKomponenata:
		komponente.write(m['Naziv']+'|'+m['Cena']+'|'+m['Raspoloziva kolicina']+'|'+m['Opis']+'|'+m['Kategorija']+'|'+m['Obrisano']+'\n')
	komponente.close()
def Biranje_komponenata():
    os.system('clear')
    print ('   	Opcije za biranje komponenata. Odaberite, biranje komponente po:        ')
	
    print ('     --++                      1 Nazivu                          --++ ')
    print ('     --++                      2 Opsegu cene                     --++ ')
    print ('     --++                      3 Raspolozivoj kolicini           --++ ')
    print ('     --++                      4 Opisu                           --++ ')
    print ('     --++                      5 Kategoriji                      --++ ')
    print ('     --++                      0 Nazad                           --++ ')
    opcija = input('Unesite opciju:') 
    while opcija != '0':
        if opcija == '1':
            key = input('Glavna rec po kojoj zelite da izvrsite biranje je: ')
            IzbaciIzPretrage=Biranje_komp_po_nazivu(key)
            Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage)
        elif opcija == '2':
            key1 = input('Minimalna cena po kojoj zelite biranje je: ')
            key2 = input('Maximalna cena po kojoj zelite biranje je: ')
            IzbaciIzPretrage=komp_po_ceni(key1, key2)
            Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage)
        elif opcija == '3':
            key1 = input('Minimalna kolicina po kojoj zelite biranje je: ')
            key2 = input('Maximalna kolicina po kojoj zelite biranje je: ')
            IzbaciIzPretrage=komp_po_kolicini(key1, key2)
            Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage)
        elif opcija == '4':
            key = input('Glavna rec po kojoj zelite biranje opisa je: ')
            IzbaciIzPretrage=komp_po_opisu(key)
            Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage)
        elif opcija == '5':
            key = input('Kategorija po kojoj zelite biranje je: ')
            IzbaciIzPretrage = komp_po_kategoriji(key)
            Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage)
        else:
            opcija = input('Opcija koju ste uneli je pogresna. Odaberite opciju iz menija.')
    if opcija == '0':
        Biranje()
def komp_po_ceni(key1, key2):
    ListaKomponenata=Ucitavanje_komp_za_listu()
    IzbaciIzPretrage=[]
    for komponenta in ListaKomponenata:
        if int(komponenta['Cena'])>=int(key1) and int(komponenta['Cena'])<=int(key2):    
            IzbaciIzPretrage.append(komponenta)
    return IzbaciIzPretrage
	
def komp_po_kolicini(key1, key2):
    ListaKomponenata=Ucitavanje_komp_za_listu()
    IzbaciIzPretrage=[]
    for komponenta in ListaKomponenata:
        if int(komponenta['Raspoloziva kolicina'])>=int(key1) and int(komponenta['Raspoloziva kolicina'])<=int(key2):
            IzbaciIzPretrage.append(komponenta)
    return IzbaciIzPretrage

def komp_po_opisu(key):
    ListaKomponenata=Ucitavanje_komp_za_listu()
    IzbaciIzPretrage=[]
    for komponenta in ListaKomponenata:
        opis=komponenta['Opis'].strip().split(' ')
        for rec in opis:
            if key==rec:
                IzbaciIzPretrage.append(komponenta)
    return IzbaciIzPretrage	
	
def komp_po_kategoriji(key):
    ListaKomponenata=Ucitavanje_komp_za_listu()
    IzbaciIzPretrage=[]
    for komponenta in ListaKomponenata:
        if komponenta['Kategorija']==key:
            IzbaciIzPretrage.append(komponenta)
    return IzbaciIzPretrage
def Izbacivanje_komp_iz_pretrage(IzbaciIzPretrage):
    if IzbaciIzPretrage==[]:
        print ('Ne postoji komponenta sa unetim podatkom!')
    else:
        for izbacen in IzbaciIzPretrage:
            print ('   --++ '+izbacen['Naziv'].ljust(13)+'--++ '+izbacen['Cena'].ljust(6)+'--++ '+izbacen['Raspoloziva kolicina'].ljust(6)+'--++ '+izbacen['Opis'].ljust(30)+'--++ '+izbacen['Kategorija'].ljust(12))
            print ('--++--++--++--++--++--++--++--++--++--++--++--++--++--++--+')
    opcija=input('Za novo biranje komponenata odaberite n, u suprotnom za nazad x: ')
    while opcija!='x':
        if opcija=='n':
            Biranje_komponenata()
        else:
            opcija=input('Pogresna opcija! Za novu biranje komponenata odaberite u a za povratak x: ')
    if opcija=='x':
        Biranje()
		
def Biranje_komp_po_nazivu(key):
    ListaKomponenata=Ucitavanje_komp_za_listu()
    IzbaciIzPretrage=[]
    for komponenta in ListaKomponenata:
        if komponenta['Naziv']==key:
            IzbaciIzPretrage.append(komponenta)
    return IzbaciIzPretrage
	
def Stampanje_komp_iz_liste():   # print component
    ListaKomponenata=Ucitavanje_komp_za_listu()
    for m in ListaKomponenata:
        if m['Obrisano']=='False':
            print ('    '+m['Naziv'].ljust(12)+' --++   '+m['Cena'].ljust(6)+' --++   '+m['Raspoloziva kolicina'].ljust(4)+' --++   '+m['Kategorija'].ljust(15))
            print ('--++--++--++--++--++--++--++--++--++--++--++-'	)
def Unosenje_komp():
    komponente = open('komponente.txt', 'a')
    naziv = str(input('Naziv komponente je: '))
    lista = Ucitavanje_komp_za_listu()
    for l in lista:
        if naziv == l['Naziv']:
            print ('Pojavila se greska.Vec postoji taj naziv komponente.')
            Unosenje_komp()
    cena = input('Cena komponente je: ')
    kolicina = input('Raspoloziva kolicina komponente je: ')
    opis = input('Opis komponente je: ')
    kategorija = input('Kategorija komponente je: ')
    opcija = str(input('Save/Cancel- s/x: '))
    Lista = Ucitavanje_kategorije()
    while opcija != 's':
        if opcija == 'x':
            komponente.close()
            Unos()
        else:
            opcija= input('Uneli ste pogresnu opciju. Odaberite s ako zelite da snimite, u suprotnom x za nazad!')
    if opcija == 's':
        komponente.write(naziv+'|'+cena+'|'+kolicina+'|'+opis+'|'+kategorija+'|False'+'\n')
        komand = input('Za snimanje nove komponente pritisnite n, za povratak x : ')
        while komand != 'n':
            if komand == 'x':
                komponente.close()
                Unos()
            else:
                komand = input('Uneli ste pogresnu opciju.Opcije koje su dostupne su s ili n. Pokusajte ponovo. ')
        if komand == 'n':
            Unosenje_komp()	
def Ucitavanje_komp_za_listu():
    komponente = open('komponente.txt', 'r')
    L=[]
    for red in komponente.readlines():
        l = red.strip().split('|')
        komponenta={'Naziv': l[0], 'Cena': l[1], 'Raspoloziva kolicina': l[2], 'Opis': l[3], 'Kategorija': l[4], 'Obrisano': l[5]}
        L.append(komponenta)
    komponente.close()   
    return L
def Uklanjanje_kategorije():
    Ispisivanje_liste_kategorija()
    ListaKategorija=Ucitaj('k')
    naziv=input('Unesite tacan naziv kategorije koju zelite da obrisete, a za kraj x: ')
    while naziv!='x':
        for i in range(len(ListaKategorija)):
            m=ListaKategorija[i]
            if m['Naziv']==naziv:
                opcija=input('Da li ste sigurni da zelite da obrisete kategoriju. Odaberite o za uklanjanje, x za nazad: ')
                if opcija=='o':
                    ListaKategorija[i]={'Naziv': '', 'Opis': ''}
                    Unosenje_liste_kategorija(ListaKategorija)
                    komand=input('Kategorija je uspesno obrisana. Za Uklanjanje nove kategorije odaberite n za povratak x: ')
                    while komand!='x':
                        if komand=='n':
                            Uklanjanje_kategorije()
                        else:
                            komand=input('Pogresna opcija! n za Uklanjanje nove kategorije, x za nazad! Unesite novu opciju: ')
                    if komand=='x':
                        Uklanjanje()
                elif opcija=='x':
                    Uklanjanje()
                else:
                    opcija=input('Uneli ste pogresnu opciju! o za Uklanjanje, x za nazad! Unesite novu opciju: ')
        else: naziv=input('Naziv kategorije koju ste uneli ne postoji. Unesite tacan naziv kategorije! x za kraj: ')
    if naziv=='x':
        Uklanjanje()
def Unosenje_liste_kategorija(ListaKategorija):
    kategorije=open('kategorije.txt', 'w')
    for i in range(len(ListaKategorija)):
        m=ListaKategorija[i]
        if m['Naziv']!='':
            kategorije.write(m['Naziv']+'|'+m['Opis']+'\n')
    kategorije.close()
	
def Ispisivanje_liste_kategorija():
    ListaKategorija=Ucitavanje_kategorije()
    os.system('clear')
    for m in ListaKategorija:
        print ('    '+m['Naziv'].ljust(12)+' --++   '+m['Opis'].ljust(40))
        print ('--++--++--++--++--++--++--++--++--++--++--++')
def Izmenjivanje_kategorija():
    Ispisivanje_liste_kategorija()

    ListaKategorija=Ucitavanje_kategorije()

    naziv=input('Unesite tacan naziv kategorije koju zelite da promenite, a za kraj x: ')
    while naziv!='x':
        for p in range(len(ListaKategorija)):
            m=ListaKategorija[p]
            if m['Naziv']==naziv:
                opcija=input('Da li ste sigurni da zelite da promenite kategoriju? Odaberite i za promenu, u suprotnom x za nazad: ')
                if opcija=='i':
                    opis=input('Unesite novi opis kategorije '+naziv+' :')
                    ListaKategorija[p]={'Naziv': naziv, 'Opis': opis} 
                    Unosenje_liste_kategorija(ListaKategorija)
                    komand=input('Kategorija je uspesno izmenjena. Za promenu nove kategorije odaberite p, u suprotnom za nazad x: ')
                    while komand!='x':
                        if komand=='p':
                            Izmenjivanje_kategorija()
                        else:
                            komand=input('Pogresna opcija! Odaberite p za promenu nove kategorije, x za nazad! Unesite novu opciju: ')
                    if komand=='x':
                        Promena()
                elif opcija=='x':
                    Promena()
                else:
                    opcija=input('Uneli ste pogresnu opciju! Odaberite p za promenu,u suprotnom x za nazad! Unesite novu opciju: ')
        else: naziv=input('Naziv kategorije koju ste uneli ne postoji. Unesite tacan naziv kategorije! x za kraj: ')
    if naziv=='x':
        Promena()
def Biranje_kategorija():
    os.system('cls')
    print ('     --++        Izbrirajte kategoriju po:        --++ ')
    print ('     --++                                         --++ ')
    print ('     --++        1 Nazivu                         --++ ')
    print ('     --++        2 Opisu                          --++ ')
    print ('     --++        0 Nazad                          --++ ')
    print ('     --++                                         --++ ')
    print ('     --++ --++ --++ --++ --++ --++ --++ --++ --++ --++  ')
    opcija=input('Unesite opciju:')
    while opcija!='0':
        if opcija=='1':
            key=input('Glavna rec kategorije po kojoj zelite biranje je: ')
            IzbaciIzPretrage=Biranje_kategorija_po_nazivu(key)
            Ispis_kategorije_po_pretrazi(IzbaciIzPretrage)
        elif opcija=='2':
            key=input('Glavna rec iz opisa po kojoj zelite biranje je: ')
            IzbaciIzPretrage=Biranje_kategorija_po_opisu(key)
            Ispis_kategorije_po_pretrazi(IzbaciIzPretrage)
        else:
            opcija=input('Greska. Opcija koju ste uneli je pogresna. Odaberite opciju iz menija.')
    if opcija=='0':
        Biranje()

def Biranje_kategorija_po_nazivu(key):
    ListaKategorija=Ucitavanje_kategorije()
    IzbaciIzPretrage=[]
    for kategorija in ListaKategorija:
        if kategorija['Naziv']==key:
            IzbaciIzPretrage.append(kategorija)
    return IzbaciIzPretrage

def Biranje_kategorija_po_opisu(key):
    ListaKategorija=Ucitavanje_kategorije()
    IzbaciIzPretrage=[]
    for kategorija in ListaKategorija:
        opis=kategorija['Opis'].strip().split(' ')
        for rec in opis:
            if key==rec:
                IzbaciIzPretrage.append(kategorija)
    return IzbaciIzPretrage

def Ispis_kategorije_po_pretrazi(IzbaciIzPretrage):
    if IzbaciIzPretrage==[]:
        print ('Ne postoji kategorija sa unetim podatkom!')
    else:
        for izbacen in IzbaciIzPretrage:
            print ('   --++ '+izbacen['Naziv'].ljust(10)+'--++ '+izbacen['Opis'].ljust(30))
            print ('--++--++--++--++--++--++--++--++--++--++--++')
    opcija=input('Za novo biranje kategorija odaberite n, u suprotnom za povratak x: ')
    while opcija!='x':
        if opcija=='n':
            Biranje_kategorija()
        else:
            opcija=input('Pogresna opcija! Za novo biranje kategorija odaberite n, u suprotnom za nazad x: ')
    if opcija=='x':
        Biranje() 	
def Unos_kategorije():
    kategorije = open('kategorije.txt', 'a')
    naziv = str(input('Naziv kategorije je: '))
    Lista = Ucitavanje_kategorije()
    for l in Lista:
        if naziv == l['Naziv']:
            print ('Naziv kategorije mora da bude jedinstven.')
            Unos_kategorije()
    opis = input('Opis kategorije je: ')
    opcija = str(input('Da sacuvate odaberite s, u suprotnom x za nazad. '))
    while opcija != 's':
        if opcija == 'x':
            kategorije.close()
            Unos()
        else:
            opcija = input('Uneli ste pogresnu opciju! Ponudjene su s ili x: ')
    if opcija == 's':
        kategorije.write(naziv+'|'+opis+'\n')
        kategorije.close()
        komand = input('Za snimanje nove kategorije pritisnite n, u suprotnom za nazad x : ')
        while komand != 'n':
            if komand == 'x':
                kategorije.close()
                Unos()
            else:
                komand=input('Uneli ste pogresnu opciju. Odaberite od ponudjenih n ili x: ')
        if komand == 'n':
            Unos_kategorije()
def Ucitavanje_kategorije():
    kategorije = open('kategorije.txt', 'r')
    L=[]
    for red in kategorije.readlines():
        l=red.strip().split('|')
        kategorija={'Naziv': l[0], 'Opis': l[1] }
        L.append(kategorija)
    return L
    kategorije.close()		


def Biranje_uredjaja():
	os.system('clear')
	print ('  --++--++      Biranje uredjaja po:           --++--++')
	print ('     --++       1 Nazivu                              --++ ')
	print ('     --++       2 Opisu                               --++ ')
	print ('     --++       3 Komponentama                        --++ ')
	print ('     --++       0 Nazad                               --++ ')
 
	opcija=input('Unesite opciju:')
	while opcija!='0':
		if opcija=='1':
			key=input('Naziv po kome zelite da birate je: ')
			IzbaciIzPretrage=Biranje_uredjaja_po_nazivu(key)
			Ispis_uredjaja_iz_pretrage(IzbaciIzPretrage)
		elif opcija=='2':
			key=input('Rec po kojoj zelite da birate opis je: ')
			IzbaciIzPretrage=Biranje_uredjaja_po_opisu(key)
			Ispis_uredjaja_iz_pretrage(IzbaciIzPretrage)
		elif opcija=='3':
			key=input('Naziv komponente po kojoj zelite da birate je: ')
			IzbaciIzPretrage=Biranje_uredjaja_po_komponentama(key)
			Ispis_uredjaja_iz_pretrage(IzbaciIzPretrage)
		else:
			opcija=input('Greska. Opcija koju ste uneli je pogresna. Odaberite opciju ponudjenu iz menija.')
	if opcija=='0':
		Biranje()

def Biranje_uredjaja_po_nazivu(key):
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    IzbaciIzPretrage=[]
    for uredjaj in ListaUredjaja:
        if uredjaj['Naziv']==key:
            IzbaciIzPretrage.append(uredjaj)
    return IzbaciIzPretrage

def Ucitavanje_uredjaja_u_listu():
    uredjaji=open('uredjaji.txt', 'r')
    L=[]
    for red in uredjaji.readlines():
        l=red.strip().split('|')
        uredjaj={'Naziv': l[0], 'Opis': l[1], 'Komponente': l[2], 'Postoji': l[3]}
        L.append(uredjaj)
    return L
    uredjaji.close()

def Ispis_uredjaja_iz_pretrage(IzbaciIzPretrage):
    if IzbaciIzPretrage==[]:
        print ('Greska. Ne postoji uredjaj sa tim podatkom.')
    else:
        for izbacen in IzbaciIzPretrage:
            print ('   * '+izbacen['Naziv'].ljust(10)+'* '+izbacen['Opis'].ljust(30)+'* '+izbacen['Komponente'].ljust(30))
            print ('++--++--++--++--++--++--++--++--++--++--')
    opcija=input('Za novo biranje uredjaja odaberite n, u suprotnom za nazad x: ')
    while opcija!='x':
        if opcija=='n':
            Biranje_uredjaja()
        else:
            opcija=input('Pogresna opcija. Za novu biranje uredjaja odaberite u, u suprotnom x za nazad: ')
    if opcija=='x':
        Biranje()
		
def Biranje_uredjaja_po_opisu(key):
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    IzbaciIzPretrage=[]
    for uredjaj in ListaUredjaja:
        opis=uredjaj['Opis'].strip().split(' ')
        for rec in opis:
            if key==rec:
                IzbaciIzPretrage.append(uredjaj)
    return IzbaciIzPretrage
	
def Biranje_uredjaja_po_komponentama(key):
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    IzbaciIzPretrage=[]
    for uredjaj in ListaUredjaja:
        komponente=uredjaj['Komponente'].strip().split('+')
        for rec in komponente:
            if key==rec:
                IzbaciIzPretrage.append(uredjaj)
    return IzbaciIzPretrage
	
def Lista_prodatih_proizvoda(): 
    Stampanje_komp_iz_liste()
    Stampanje_liste_komponenata()
    prodato=[]   
    proizvod=input('Unesite tacan naziv artikla, u suprotnom za kraj odaberite x: ')
    while proizvod!='x':
        if Provera_postojanja_proizvoda(proizvod)==True:
            prodato.append(proizvod)
            proizvod=input('Unesite tacan naziv sledeceg artikla, u suprotnom za kraj odaberite x: ')
        else:
            proizvod=input('Greska. Ni jedan proizvod se ne zove tako. Unesite naziv koji se nalazi u listi, za kraj odaberite x: ')        
    if proizvod=='x':
        opcija=input('Za izdavanje racuna pritisnite s, za povratak bez izdavanja racuna x: ')
        if opcija=='x':
            MeniZaProdavce()
        if opcija=='s':
            return prodato

def Provera_postojanja_proizvoda(proizvod):
    Lista1=Ucitavanje_komp_za_listu()   
    Lista2=Ucitavanje_uredjaja_u_listu()
    Proizvodi=Lista1+Lista2
    Lista=[]
    for i in range(len(Proizvodi)):
        m=Proizvodi[i]
        Lista.append(m['Naziv'])
    for i in range(len(Lista)):
        if proizvod==Lista[i]:
            return True
			
			
def Komponente_za_racun(prodato, ListaKomponenata):
    racun='_ _ _ _ _ _ _ _ _ \n'
    suma=0
    for prodat in prodato:
        for proizvod in ListaKomponenata:
            if prodat==proizvod['Naziv']:
                racun+='*   '+proizvod['Naziv'].ljust(12)+'  '+proizvod['Cena'].ljust(8)+'   *\n'+'_ _ _ _ _ _ _ _\n'
                suma+=int(proizvod['Cena'])
                if proizvod['Raspoloziva kolicina']=='1':
                    proizvod['Raspoloziva kolicina']='0'
                    proizvod['Postoji']='False'
                else:
                    proizvod['Raspoloziva kolicina']=str(int(proizvod['Raspoloziva kolicina'])-1)
                proizvod={'Naziv': proizvod['Naziv'], 'Raspoloziva kolicina': proizvod['Raspoloziva kolicina'], 'Cena': proizvod['Cena'], 'Postoji': proizvod['Obrisano'], 'Opis': proizvod['Opis'], 'Kategorija': proizvod['Kategorija']}
                Lista_komponenata(ListaKomponenata)
    return racun, suma
	
def Racun(prodato):
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    ListaKomponenata=Ucitavanje_komp_za_listu()
    prodaja=prodato
    for u in range(len(ListaUredjaja)):
        uredjaj=ListaUredjaja[u]['Naziv']
        for i in range(len(prodato)):
            prodat=prodato[i]
            if prodat==uredjaj:
                komponente=Rastava_uredjaja_na_komponente(ListaUredjaja[u])
                prodaja+=komponente
    racun, suma=Komponente_za_racun(prodaja, ListaKomponenata)
    return racun, suma
	
def PrintRacuna(Ulogovan, racun, suma):
    Vreme=VremeIDatum()
    ViD='*     '+Vreme+'    *'
    prodavac=str(Ulogovan[0])+' '+str(Ulogovan[1])
    radnik='*    '+prodavac.ljust(20)+'    *'
    porez=suma/5               
    iznos='*      Cena: '+str(suma+porez).ljust(10)+'      *'
    drzavi='*      Porez: '+str(porez).ljust(10)+'     *'
    print (' |--    Prodavnica gaming racunara    --|   ')
    print ('-  -  -  -  -  -  -  -  -  - ')
    print (ViD)
    print ('-  -  -  -  -  -  -  -  -  - ')
    print (racun)
    print ('-  -  -  -  -  -  -  -  -  - ')
    print (iznos)
    print ('-  -  -  -  -  -  -  -  -  - ')
    print (drzavi)
    print ('-  -  -  -  -  -  -  -  -  - ')
    print (radnik)
    print (' |--  Hvala na ukazanom poverenju, pcg team.  --|')
    racuni=open('racuni.txt', 'a')
    upis=Vreme+'|'+str(suma+porez)+'\n'
    racuni.write(upis)
    racuni.close()
    opcija=input('Ako zelite da se vratite nazad u meni, odaberite opciju x: ')
    while opcija!='x':
        opcija=input('Ako zelite da se vratite nazad u meni, odaberite  opciju x: ')
    if opcija=='x':
        MeniZaProdavce()
		
		
def Stampanje_liste_komponenata():
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    for m in ListaUredjaja:
        if m['Postoji']=='True':
            komponente=m['Komponente'].strip().split('+')
            komp=''
            for i in range(len(komponente)):
                komp+=komponente[i]+'   '
            print ('    '+m['Naziv'].ljust(12)+' *   '+komp.strip().ljust(150))
            print ('-  -  -  -  -  -  -  -  -  - ')
def Rastava_uredjaja_na_komponente(uredjaj):
    komponente=uredjaj['Komponente'].strip().split('+')
    return komponente
	
	
def Uklanjanje_uredjaja():
	ListaUredjaja=UcitajUredjajeUListu()
	Ispis_liste_uredjaja()
	naziv=input('Unesite tacan naziv uredjaja koji zelite da obrisete, a za kraj x: ')
	while naziv!='x':
		for i in range(len(ListaUredjaja)):
			m=ListaUredjaja[i]
			if m['Naziv']==naziv:
				komanda=input('Da li ste sigurni da zelite da obrisete uredjaj '+naziv+'? Odaberite o za brisanje, x za nazad: ')
				if komanda=='o':
					ListaUredjaja[i]={'Opis': m['Opis'], 'Postoji': 'False','Komponente':m['Komponente'],'Naziv':m['Naziv']}
					Unosenje_liste_uredjaja(ListaUredjaja)
					komand=input('Kategorija je uspesno obrisana. Za brisanje nove kategorije odaberite n za povratak x: ')
					while komand!='x':
						if komand=='n':
							Uklanjanje_uredjaja()
						else:
							komand=input('Pogresna komanda! n za brisanje nove kategorije, x za nazad! Unesite novu komandu: ')
					if komand=='x':
						Uklanjanje()
				elif komanda=='x':
					Uklanjanje()
				else:
					komanda=input('Uneli ste pogresnu komandu! o za brisanje, x za nazad! Unesite novu komandu: ')
		else: naziv=input('Naziv kategorije koju ste uneli ne postoji. Unesite tacan naziv kategorije! x za kraj: ')
	if naziv=='x':
		Uklanjanje()

	
def Ispis_liste_uredjaja():
    ListaUredjaja=Ucitavanje_uredjaja_u_listu()
    os.system('cls')
    for m in ListaUredjaja:
        if m['Postoji']=='True':
            print ('    '+m['Naziv']+' *   '+ m['Opis'].ljust(12)+' *   '+m['Komponente'].ljust(6)+' *   ')
            print ('++--++--++--++--++--++--++--++--++--++--'	)
		


def Unosenje_liste_uredjaja(ListaUredjaja):
    uredjaji=open('uredjaji.txt', 'w')
    for i in range(len(ListaUredjaja)):
        m=ListaUredjaja[i]
        if m['Naziv']!='':
            uredjaji.write(m['Naziv'] + "|"+m['Opis']+"|" + m['Komponente']+"|"+m['Postoji']+'\n')
    uredjaji.close()

Pocetak(Logovanje())