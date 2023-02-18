import re

x1 = re.search(r'[a-z]ra', 'afara ploua')
#[n-r] o cifra de la n la = [n,o,p,q,r]
#adica a cautat daca exista un string cu o lista de la n-r inclusiv r urmat de ua in stringul 'afara ploua'

# print(x)

# x2 = re.match(r'[a-z]fara p', 'afara ploua')
# print(x2)

# prop = 'Sebastian invata programare'
# x3 = re.search(r'\web', prop.split(" ")[0])
# print(x3)
#
# strx = 'Andrei Andreea Andrisor Andra'
# x4 = re.findall(r'\w.a', strx)
# print(x4)
# strx = 'Andrei Andreea Andrisor Ion Andra Vasile'
# x5 = re.finditer(r'\wnd', strx)
#
# for gasit in x5:
#     print(gasit)



# path = 'C:/'
# path = r'C:\'

# strx = 'afara ploua fgsf hfdgfdg gfsdgfd4535 543534'
# primul_cuv = strx.split(" ")[1]
#
# print(primul_cuv)


# orase = 'Iasi, Buc, Oradea. Cluj - Tim'
#
# x6= re.split(r',|\.|-', orase)
# print(x6)
#
# x7 = orase.split(",")
# print(f"x7 = {x7}")
#
# orase = 'Iasi, Buc, Oradea, Cluj, Tim'
#
# x8 = re.sub(r' [a-zA-Z]{3}',' invalid',orase)
# print(x8)

strx_9 = 'Alice has elephant'
x_9 = re.sub(r"[a-z]{8}", "dog", strx_9)
print(x_9)

