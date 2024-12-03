# 1. feladat

# szam=int(input('Kérlek adj meg egy stzámot!  '))
# szo=input('Most adj meg egy tetszőleges karakterláncot!  ')
# for _ in range(szam):
#     print(f'{szo.lower()} ',end='')


# 2. feladat

# paradicsom=1199
# paprika=1349
# hagyma=289
# print(f'{'paradicsom':<10} {paradicsom} Ft/Kg')
# print(f'{'paprika':<10} {paprika} Ft/Kg')
# print(f'{'hagyma':<11} {hagyma} Ft/kg')
# valasz=''
# fizetendo=0
# while valasz!='nem':
#     valasz=input('Kíván valamit vásárolni?  ')
#     if valasz=='igen':
#         melyik=input('Melyik termékből kér?  ')
#         suly=float(input('Adja meg a mennyiséget Kg-ban!  '))
#         if melyik=='paradicsom':
#             fizetendo=fizetendo+paradicsom*suly
#         if melyik=='paprika':
#             fizetendo=fizetendo+paprika*suly
#         if melyik=='hagyma':
#             fizetendo=fizetendo+hagyma*suly
# print(f'A fizetendő összeg: {fizetendo:.0f} Ft')


# 3. feladat

# from math import sqrt
# a=float(input('Add meg az a oldal hosszát cm-ben!  '))
# b=float(input('Add meg a b oldal hosszát cm-ben!  '))
# c=float(input('Add meg a c oldal hosszát cm-ben!  '))
# s=(a+b+c)*0.5
# if a+b>c and a+c>b and b+c>a: 
#     print('Létezhet ilyen háromszög.')
#     if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2: 
#         print('Ez egy derékszögű háromszög.')
#     elif a==b or a==c or b==c: 
#         print('Ez egy egyenlő szárú háromszög.')
#     else: 
#         print('Ez egy sima háromszög.')
#     print(f'A háromszög kerülete: {a+b+c} cm')
#     print(f'A területe: {sqrt(s*(s-a)*(s-b)*(s-c))} cm2')
# else:
#     print('Nem létezhet háromszög ilyen oldalakkal')


# 4. feladat

# from math import sqrt

# a=int(input('Add meg az a együttható értékét!  '))
# b=int(input('Add meg a b együttható értékét!  '))
# c=int(input('Add meg a c együttható értékét!  '))
# d=(b**2)-(4*a*c)
# if a==0: 
#     print('Az egyenle nem másodfokú!')
# elif d < 0: 
#     print('Az egyenletnek nincs valós megoldása.')
# elif d==0: 
#     print('Az egyenletnek egy valós megoldása van.')
#     print(f'xˇ1={((-b)+sqrt((b**2)-(4*a*c)))/(2*a)}')
# else:
#     print('Az egyenletnek kettő valós megoldása van.')
#     print(f'xˇ1={((-b)+sqrt((b**2)-(4*a*c)))/(2*a)}')
#     print(f'xˇ2={((-b)-sqrt((b**2)-(4*a*c)))/(2*a)}')