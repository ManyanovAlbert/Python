from datetime import datetime
from math import sin, pi


def bio_rhythm(P, T):
    return sin(2.0 * pi * T / P) * 100


date_entry = input('Введите дату рождения в формате dd.mm.YYYY:')
date0 = datetime.strptime(date_entry, '%d.%m.%Y')

date_entry = input('Введите дату расчета в формате dd.mm.YYYY:')
date1 = datetime.strptime(date_entry, '%d.%m.%Y')

T = date1.toordinal() - date0.toordinal()

print(bio_rhythm(23, T))
print(bio_rhythm(28, T))
print(bio_rhythm(33, T))