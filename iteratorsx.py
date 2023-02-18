# listx = [0,1,2]
#
# for el in listx:
#     print(el, end=", ")
#
# strx = 'Vasile'
# for el in strx:
#     print(el)

# nrx = 12434324324234324235465654
#
# for cifra in nrx:
#     print(cifra)
#
# rational = 123.56654753
# for cifra in rational:
#     print(cifra)

# setx = {1,3,5}
# for el in setx:
#     print(el)

# #range(1,10) generator
# for number in range(1,10):
#     print(number)
# # scoate fiecare element unu cate unu - range este generator
# # generators sunt poreclite operatii lenese
#
# for number in list(range(1,10)):
#     print(number)
# #lista pastreaza in memorie toate elementele si abia apoi le itereaza
# #implicit incarca memoria cu toate elementele mai intai

# import os
#
# pathx = 'C:/Users/const/Dropbox/SDA/Code Python_41'
# fisiere = os.listdir(pathx)
# for f in fisiere:
#     print(f)
#
# from math import sqrt
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def prime_generator(n):
#     # Generator for iterating over n primes
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if is_prime(number):
#             yield number
#             generated_numbers += 1
#         number += 1
#
# print(prime_generator(15))
#
# # for el in prime_generator(15):
# #     print(el)
# #
# #pentru a accesa un obiect de tip generator, e nevoie sa iteram asupra lui
#
# rng = range(2,7)
# print(rng)
#
# #metoda 1 de accesare a datelor intr-un generator
# print(list(rng))
#
# #metoda 2 (...) prin iterare:
# for el in rng:
#     print(el)


# gen = prime_generator(1000000)
# for elem in gen:
#     print(elem)

# nr = 13243432432
#
# try:
#     for cifra in nr:
#         print(cifra)
# except TypeError:
#     print("Are o eroare de TypeError")
#     for cifra in str(nr):
#         print(cifra)

# rng = range(10)
# print(rng)
#
# print(list(range(10)))
# for el in rng:
#     print(el)
#

def aGeneratorFunction(param):

    print('Hello', param)
    yield 42

    print('How are you,', param)
    yield 99

    print('Goodbye', param)
    return 86  # Raises StopIteration with value 86.

print(next(aGeneratorFunction("ION"))

px = next(aGeneratorFunction("ION"))
print(px)

px = next(aGeneratorFunction("ION"))
print(px)

px = next(aGeneratorFunction("ION"))
print(px)
