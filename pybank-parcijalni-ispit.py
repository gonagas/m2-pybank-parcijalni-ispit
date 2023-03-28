#region OPIS ZADATKA
# SIMULACIJA BANKOVNOG RAČUNA
# Zadatak je započet tako da bi korisnici trebali moci nastaviti dalje po ovom predlošku
# firma (naziv, adresa, oib, odgovorna osoba) unos ispis

# 1. len(oib) provjeri je li OIB točno unesen - za sada koristimo samo provjeru je li ima 11 znakova
# 2. simulacija rada računa u banci. kreirati funkcije za
#     polog novca
#     podizanje novca
#     provjeru je li ima dovoljno novca na računu
#     prikaz stanja na računu
#     mogućnost oročenja
#       transakcija - ID    datum, vrijeme, iznos, stanje, broj racuna, opis, korisnik
#endregion
import random
import datetime
import os


#region GLOBALNE VARIJABLE
company_name = ''
company_street_and_number = ''
company_postal_code = ''
company_city = ''
company_tax_id = ' '
company_manager = ''
currency = ' €'

# company_name = 'Grafing doo'
# company_street_and_number = 'IKS 10'
# company_postal_code = '32100'
# company_city = 'Vinkovci'
# company_tax_id = '56214806575'
# company_manager = 'Goran Žagar'
# currency = ' €'

# Prazan Dictionary u kojem ce biti pohranjene transakcije
transaction_id = 0
transactions = { }

# Format broja racuna: BA-GODINA-MJESEC-Redni_broj 
# BA - Business Account
# Redni_broj - 00001 - 5 znamenki
account_number = '' # BA-2023-03-00042
account_balance = 0.00

#endregion


def generate_account_number():
    global account_number

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if month < 10:
        month = str('0' + str(month))
    else:
        month = str(month)

    if account_number == '':
        account_number = 'BA-' + str(year) + '-' + month + '-00001'
    else:
        number_str = account_number.split('-')[-1]
        number = int(number_str)

        if number < 9:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0000' + str(number)
        elif number < 99:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-000' + str(number)
        elif number < 999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-00' + str(number)
        elif number < 9999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0' + str(number)
        else:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-' + str(number)

    return account_number


def open_account():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RAČUNA\n'.center(65))
    print('Podaci o vlasniku računa\n'.center(65))
    print('-' * 65)

    global company_name
    global company_street_and_number
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance
    global transaction_id

    company_name = input('Naziv Tvrtke:\t\t\t\t').title()
    company_street_and_number = input('Ulica i broj sjedišta Tvrtke:\t\t').title()
    company_postal_code = input('Poštanski broj sjedišta Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjedište Tvrtke:\t').title()
    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        # string.isdigit() vraca Ture ako su sve znamenke u stringu brojke
        if not company_tax_id.isdigit():
            print('OIB mora sadržavati samo znamenke.\nMolimo Vas ponovite unos\n')
        elif len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati točno 11 znamenki.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t').title()
    print()

    #input('\n(Pritisnite bilo koju tipku) ')    # Nece spremiti nista, jer su sve izmjene vec spremljene, 
                                                        # ali dobro izgleda :-)

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RAČUNA\n'.center(65))
    print('Podaci o vlasniku računa\n'.center(65))
    print('-' * 65)
    print(f'Naziv Tvrtke:\t\t\t\t{company_name}')
    print(f'Ulica i broj sjedišta Tvrtke:\t\t{company_street_and_number}')
    print(f'Poštanski broj sjedišta Tvrtke:\t\t{company_postal_code}')
    print(f'Grad u kojem je sjedište Tvrtke:\t{company_city}')
    print(f'OIB Tvrtke:\t\t\t\t{company_tax_id}')
    print(f'Ime i prezime odgovorne osobe Tvrtke:\t{company_manager}\n')
    print(f'Podaci o vlasniku računa tvrtke {company_name}, su uspješno spremljeni.')
    print('-' * 65)
    input('Za nastavak pritisnite bilo koju tipku\t')

    # Detalji o racunu
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RAČUNA\n'.center(65))
    print('Stanje računa\n'.center(65))
    print('-' * 65)

    print(f'Broj računa {generate_account_number()}')

    # {account_balance:.2f} Broj account_balance zaokruzi na dvije decimale SAMO kod prikaza, broj ostaje ne promijenjen
    print(f'Trenutno stanje računa:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upišite iznos koji želite položiti na račun.\nNAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        # transakcija - datum, vrijeme, iznos, stanje, broj racuna, opis
        # transaction = [datetime.datetime.date,
        #                datetime.datetime.time,
        #                amount,
        #                account_balance]

        transaction.append(datetime.datetime.now().date().isoformat())
        transaction.append(datetime.datetime.now().time().isoformat("seconds"))
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Polog kod otvaranja računa')
        transaction.append(company_manager)
        transaction_id += 1
        transactions[transaction_id] = transaction

    else:
        amount = 0.00
    
    print('-' * 65)
    print()
    input('Za povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def main_menu():
    choice = -1

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('GLAVNI IZBORNIK\n'.center(65))
    print('-' * 65)

    if company_name == '':
        print('1. Kreiranje računa')        # Kreiranje podataka
    else:
        print('1. Ažuriranje računa')       # Azuriranje podataka

    print('2. Prikaz stanja računa')        # Trenutno stanje
    print('3. Prikaz prometa po računu')    # Dictionary

    print('4. Polog novca na račun')        # Dodaj na racun i kreiraj transakciju
    print('5. Podizanje novca s računa')    # Oduzmi s racuna i kreiraj transakciju

    print('0. Izlaz')                       # Izadi iz while petlje

    print('-' * 65)
    if company_name == '':
        while choice != 1 and choice != 0:  # Ako korisnik odustane, treba izaci iz programa
            print('Jos niste otvorili racun. Molimo prvo kreirajte racun. Hvala!')
            print('-' * 65)
            choice = int(input('Vas izbor:\t'))
            print()
    else:
        print('Molimo Vas upisite samo broj ispred opcije koju zelite odabrati')
        print('-' * 65)
        choice = int(input('Vas izbor:\t'))
        print()

    return choice


def display_account_balance():
    # Detalji o racunu
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PRIKAZ STANJA RACUNA\n'.center(65))

    print(f'Broj racuna:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')

    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n\n')
    print('-' * 65)
    print()
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def create_transaction():
    global account_balance
    global transaction_id
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('UPLATA NA RAČUN\n'.center(65), '\n')

    print(f'Broj računa:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')

    print(f'Trenutno stanje računa:\t{account_balance:.2f}{currency}\n')
    print('-' * 65)

    print('Molimo Vas upišite iznos koji želite poloziti na račun.\nNAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        transaction.append(datetime.datetime.now().date().isoformat())
        transaction.append(datetime.datetime.now().time().isoformat("seconds"))
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Uplata na račun')
        transaction.append(company_manager)
        transaction_id += 1
        transactions[transaction_id] = transaction

    else:
        amount = 0.00

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('UPLATA NA RAČUN\n'.center(65), '\n')

    print(f'Broj računa:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')

    print(f'Na račun ste uspješno uplatili:\t{amount:.2f}{currency}\n')
    print(f'Novo stanje računa:\t\t{account_balance:.2f}{currency}\n')
    
    print('-' * 65)
    print()
    input('Za povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def update_account():
    global company_name
    global company_street_and_number
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AŽURIRANJE PODATAKA\n'.center(65))
    print('-' * 65)

    print('Odaberite broj ispred stavke koju želte ažurirati\n')

    print(f'1. Naziv Tvrtke:\t\t\t\t{company_name}')
    print(f'2. Ulica i broj sjedišta Tvrtke:\t\t{company_street_and_number}')
    print(f'3. Poštanski broj sjedišta Tvrtke:\t\t{company_postal_code}')
    print(f'4. Grad u kojem je sjedište Tvrtke:\t\t{company_city}')
    print(f'5. OIB Tvrtke:\t\t\t\t\t{company_tax_id}')
    print(f'6. Ime i prezime odgovorne osobe Tvrtke:\t{company_manager}')
    print()
    choice = int(input('\t'))
        
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print('*' * 65)
    # print('PyBANK ALGEBRA\n'.center(65), '\n')
    # print('AŽURIRANJE PODATAKA\n'.center(65))
    # print('-' * 65)
    print()
    if choice == 1:
        company_name = input('Upišite naziv Tvrtke:\t').title()
    if choice == 2:
        company_street_and_number= input('Upišite ulicu i broj sjedišta Tvrtke:\t').title()
    if choice == 3:
        company_postal_code = input('Upišite poštanski broj sjedišta Tvrtke:\t')
    if choice == 4:
        company_city = input('Upišite grad u kojem je sjedište Tvrtke:\t').title()
    if choice == 5:
        company_tax_id = input('Upišite OIB Tvrtke:\t')
    if choice == 6:
        company_manager = input('Upišite ime i prezime odgovorne osobe Tvrtke:\t').title()
    if choice == '':
        pass
    else:
        pass

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AŽURIRANJE PODATAKA\n'.center(65))
    print('-' * 65)

    print(f'1. Naziv Tvrtke:\t\t\t\t{company_name}')
    print(f'2. Ulica i broj sjedišta Tvrtke:\t\t{company_street_and_number}')
    print(f'3. Poštanski broj sjedišta Tvrtke:\t\t{company_postal_code}')
    print(f'4. Grad u kojem je sjedište Tvrtke:\t\t{company_city}')
    print(f'5. OIB Tvrtke:\t\t\t\t\t{company_tax_id}')
    print(f'6. Ime i prezime odgovorne osobe Tvrtke:\t{company_manager}')
     
    print()
    print('Podaci su uspješno ažurirani\n')
    
    print('-' * 65)
    print()
    input('Za povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def withdraw_money():
    global account_balance
    global transaction_id

    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PODIZANJE NOVCA S RAČUNA\n'.center(65), '\n')

    print(f'Broj računa:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')

    print(f'Trenutno stanje računa:\t{account_balance:.2f}{currency}\n')
    print('-' * 65)

    print('Molimo Vas upisite iznos koji želite podići s računa.\nNAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    amount = input('\t')
    while True:
        if amount != '':
            amount = float(amount)
        
        if amount <= account_balance:
            transaction = []
            account_balance -= amount

            transaction.append(datetime.datetime.now().date().isoformat())
            transaction.append(datetime.datetime.now().time().isoformat("seconds"))
            transaction.append(amount)
            transaction.append(account_balance)
            transaction.append(account_number)
            transaction.append('Isplata s računa')
            transaction.append(company_manager)
            transaction_id += 1
            transactions[transaction_id] = transaction
            break

        elif amount > account_balance:
            print()
            print('Na računu nije raspoloživo dovoljno sredstava.\nUnesite novi iznos:')
            amount = float(input('\t'))
            continue

        else:
            amount = 0.00
            
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PODIZANJE NOVCA S RAČUNA\n'.center(65), '\n')

    print(f'Broj racuna:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')
    print('-' * 65)

    print(f'Uspješno ste s računa podigli:\t{amount:.2f}{currency}\n')
    print(f'Novo stanje racuna:\t\t{account_balance:.2f}{currency}\n')
    print('-' * 65)
    print()
    input('Za povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def show_transactions():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('*' * 144)
    print('PyBANK ALGEBRA\n'.center(144), '\n')
    print('PRIKAZ PROMETA PO RAČUNU\n'.center(144))

    print(f'Broj računa:\t\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.now().isoformat(" ", "seconds")}\n')

    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}')

    print('-' * 144)
    print(f'|{"ID":<5}|{"Broj":^20}|{"Korisnik":^20}|{"Datum":^15}|{"Vrijeme":^15}|{"Vrsta":^30}|{"Iznos":^15}|{"Stanje":^15}|')
    print(f'|{"":<5}|{"Računa":^20}|{"":^20}|{"transakcije":^15}|{"transakcije":^15}|{"transakcije":^30}|{"transakcije":^15}|{"računa":^15}|')
    print('-' * 144)

    for key, value in transactions.items():
        print(f'|{key:<5}', end='')
        print(f'|{value[4]:^20}', end='')
        print(f'|{value[6]:^20}', end='')
        print(f'|{value[0]:^15}', end='')
        print(f'|{value[1]:^15}', end='')
        print(f'|{value[5]:^30}', end='')
        print(f'|{value[2]:>13.2f}{currency}', end='')
        print(f'|{value[3]:>13.2f}{currency}|')
    
    print('-' * 144)
    print()
    input('Za povratak u Glavni izbornik pritisnite bilo koju tipku\t')

# Main menu
choice = main_menu()

while choice != 0:
    if choice == 1 and company_name == '':
        open_account()
    elif choice == 1 and company_name != '':
        update_account()
    if choice == 2:
        display_account_balance()
    if choice == 3:
        show_transactions()
    if choice == 4:
        create_transaction()
    if choice == 5:
        withdraw_money()
    if choice > 5:
        choice = main_menu()
        continue
    


    choice = main_menu()

# Dodati odjavni ekran
os.system('cls' if os.name == 'nt' else 'clear')
    
print('*' * 65)
print('PyBANK ALGEBRA\n'.center(65), '\n')
print('Hvala Vam što koristite naše usluge\n'.center(65))
print('Ugodan dan'.center(65), '\n')
print('*' * 65)