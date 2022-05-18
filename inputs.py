"""Inputs.

Take input and return data in format of list[dict]


Example of output:
[
    {
    'name': 'Bromhexin',
    'form': 'gtt'
    'unit': 'ml',
    'quantity': 100,
    'total_price': 194.0,
    },
    {
    'name': 'Bromhexin',
    'unit': 'ml',
    'quantity': 100,
    'total_price': 194.0,
    },
    {...},
    {...},
]

"""


def better_input(prompt, type, default_value=None):
    error_msg = 'Zadána špatná hodnota, prosím opakuj.'
    while True:
        # get user answer
        answer = input(prompt).strip()

        # check for empty answer, return default value
        if not answer and default_value:
            return default_value
        elif not answer:
            print(error_msg)
            continue
        else:  # we have a message
            # check for correct type
            try:
                answer = type(answer)  # here we try to parse, for example int(1.5)
            except ValueError:
                print(error_msg)
            else:
                return answer


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

    entries = []
    while True:
        item = {
            'name'       : better_input('Název: ', str),
            'form'       : better_input('Forma: ', str),
            'unit'       : better_input('Jednotky: ', str, 'jdn'),
            'quantity'   : better_input('Počet: ', int),
            'total_price': better_input('Celková cena [Kč]: ', float),
            }
        entries.append(item)

        next_q = input('-- další? [a/n]: ')
        if next_q == 'n':
            return entries
