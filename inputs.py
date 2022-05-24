# zkratka: (latinsky, jednotky-pozdeji se vyplní samy),
VALID_FORMS = {
    'aer':      ('aerosol',),
    'cps':      ('capsula',),
    'cap':      ('capsula',),
    'col':      ('collyrium',),
    'crm':      ('cream',),
    'drg':      ('dragée',),
    'emp':      ('emplastrum',),
    'eml':      ('emulsio',),
    'ext':      ('extractum',),
    'foa':      ('foam',),
    'gel':      ('gel',),
    'glo':      ('globula',),
    'gra':      ('granulat',),
    'gtt':      ('guttae',),
    'inh':      ('inhalatio',),
    'inj':      ('injectio',),
    'liq':      ('liquidum',),
    'lot':      ('lotio',),
    'ole':      ('oleum',),
    'plv':      ('pulveres',),
    'plv ads':  ('pulvis adspersorius',),
    'pst':      ('pasta',),
    'shp':      ('shampoo',),
    'sir':      ('sirupus',),
    'sol':      ('solutio',),
    'spc':      ('species',),
    'spr':      ('spray',),
    'sup':      ('suppositorium',),
    'sus':      ('suspensio',),
    'tab':      ('tabuletta',),
    'tbl':      ('tabuletta',),
    'tct':      ('tinctura',),
    'ung':      ('unguentum',),
    }

LABEL_ASSETS = {
        'Name':'Zadejte název produktu: ', 
        'Form':'Zadejte lékovou formu: ',
        'Units':'Zadejte typ jednotky: ', 
        'Quantity':'Zadejte počet jednotek: ',
        'Price':'Zadejte celkovou cenu: ',
        }        

VALID_UNITS = ('ml','g','ks',)    # další units...

def user_input():
    """Take input from user.

    Exmaple input:
        Nazev: Bromhexin
        Forma: gtt
        Jednotky: ml
        Pocet: 100
        Celkova cena: 194
        -- další? [a/n]:
    """
    seznam = []
    poradi_cedulky = 0
    dalsi = 'a'
    
    while True:   
        if dalsi == 'a':
            seznam.append({})
            for inpt in LABEL_ASSETS.keys():
                seznam[poradi_cedulky][inpt] = input(LABEL_ASSETS[inpt])
                if inpt == 'Quantity' or inpt == 'Price':
                    while True:
                        try:
                            int(seznam[poradi_cedulky][inpt])
                            break
                        except ValueError:
                            seznam[poradi_cedulky][inpt] = input(LABEL_ASSETS[inpt])
                elif inpt == 'Units':
                    while seznam[poradi_cedulky][inpt] not in VALID_UNITS:
                        seznam[poradi_cedulky][inpt] = input(LABEL_ASSETS[inpt])
                elif inpt == 'Form':  
                    while seznam[poradi_cedulky][inpt] not in VALID_FORMS.keys():
                        seznam[poradi_cedulky][inpt] = input(LABEL_ASSETS[inpt])
            poradi_cedulky += 1
            dalsi = input('Chcete vytvořit další cedulku? [a/n]: ')
        elif dalsi == 'n':
            break
        else:
            dalsi = input('Chcete vytvořit další cedulku? [a/n]: ')     
    return seznam


if __name__ == '__main__':
    raise SystemExit(user_input())
