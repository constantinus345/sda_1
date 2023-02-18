"""
Lambda
- Scrieti o functie care returneaza suma patratului a 3 numere
- Scrieti o functie care returneaza suma radicalilor a doua numere
- Func care returneaza un sir scris cu litere mici

-Functie care returneaza un sir fara diacritice

JSON
Creati un fisier JSON care contine contactul unei persoane, cu nume, prenume, tel, email si 2 adrese - home & office (adresa sa fie la nivelul 2, include si codul postal)
Scrieti acest fisier intr-un folder nou-creat cu modulul os pe desktop
Cititi din fisierul JSON codul postal

Creati un fisier JSON cu membrii familiei (fictiv e ok, 3 e ok), ce include nume, prenume, varsta, cate 2 hobby-uri si 2 numere de telefon.
Scrieti acest fisier intr-un folder nou-creat cu modulul os pe desktop
Cititi din fisierul JSON primul hobby de la toti membrii, stocat intr-o lista.

CSV
Creati un fisier CSV, salvati in memorie intr-un folder nou-creat cu modulul os pe desktop

Creati un fisier CSV dintr-o lista de liste, apoi cititi fisierul linie cu linie

Creati un fisier CSV cu o lista de elevi si mediile lor la 3 discipline la BAC.
Salvati fisierul, apoi returnati elevul cu media cea mai mare. Plus o functie care returneaza lista de elevi care au sub media X.



Pandas, Polars - external libs
- Cititi si printati un fisier csv cu ajutorul librariei pandas, apoi cu a librariei polars.

GENERATORS
Scrieti un generator de sir fibonacci
https://www.geeksforgeeks.org/generators-in-python/


"""
# def scriere(x):
#     for i in range(x):
#         yield i*3
#
# genx = scriere(10)
# print(genx)
#
# # print(next(genx))
# # print(next(genx))
# # print(next(genx))
# # print(next(genx))
#
# for ix in genx:
#     print(ix)

#Sirul lui Fibonacci = 1,1,2,3,5,8.... - adica primele numere sunt 1, 1 apoi urmatoarele sunt precedentele doua adunate
#Functia Fibonacci generata intr-un mod generator ~ lazy generating
# def fib(x):
#     a, b = 1,1
#     # echivalent cu:
#     # a= 1
#     # b =1
#     while a<x:
#         yield a
#         a,b = b, a+b
#
# var_fib = fib(10)
# # print(next(var_fib))
#
# for ix in var_fib:
#     print(ix)

def fibi(x):
    a,b = 1,1
    lista_fib = []
    while a<x:
        lista_fib.append(a)
        a, b = b, a+b

    return lista_fib

lisx = fibi(10)
print(lisx)
