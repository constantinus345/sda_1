
# def addx(*args):
#     sumx = 0
#     for x in args:
#         sumx += x
#     return  sumx
#
# print(addx(1,2,3))

# #alternativa cu lamda- functie de o linie
# x1 = lambda x: x.upper()
# print(x1("aBcDe"))
#
# #alternativa cu def
# def upx(strx):
#     return strx.upper()
#
# print(upx("aBcDe"))

# #----------------------------------------
# sum_squares = lambda x,y: x**2 + y**3
# print(sum_squares(3,2))
# print(sum_squares(4,3))
#
# def sum_squares(x,y):
#     return  x**2 + y**3
#
# print(sum_squares(3,2))
# print(sum_squares(4,3))
#
# #metoda lambda- functie de un rand
# listx = list(range(4,7))
# print(f"listx = {listx}")
# patratul_el_din_lista = list(map(lambda x: x**2, listx))
# print(f"patratul_el_din_lista cu lamda = {patratul_el_din_lista}")
#
# #metoda list comprehension
# patratul_el_din_lista_ls = [x**2 for x in listx]
# print(f"patratul_el_din_lista_ls cu list comprehension = {patratul_el_din_lista_ls}")
#
# #metoda cu def - functie clasica
# def patratul_el_din_lista_def(lista_custom):
#     return [x**2 for x in lista_custom]
#
# print(f"patratul_el_din_lista_def cu def + list compr. = {patratul_el_din_lista_def(listx)}")

sum_plus_10 = lambda a: a+10
print(sum_plus_10(100))

def sum_plus_10(a,b,c):
    return a

print(sum_plus_10(100))


inmultire = lambda a,b: sum_plus_10(a)*b

print(f"inmultire(1,5) = {inmultire(1, 5)}")







