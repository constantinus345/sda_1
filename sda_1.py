# # print(3/0)
#
# try:
#     print(3 / 2)
# except ZeroDivisionError:
#     # e good case practice sa scriem tipul de exceptii așteptat/expected.
#     print('Aveti diviziune cu 0')
# finally:
#     print("Se executa indiferent daca instructiunea a mers sau nu")

#
# try:
#     print(3 / 0)
# except:
#     # gestioneaza toate erorile posibile, functioneaza dar nu e caz de buna practica.
#     print('Aveti diviziune cu 0')

# import librarie

# nr = 10
# de_impartit = list(range(-3,5))
# # print(de_impartit)
#
# for numar in de_impartit:
#     try:
#         print(f"{nr}/{numar} = {nr/numar}")
#     except ZeroDivisionError:
#         continue

# lista = list(range(1,7))
# print(lista)
#
# try:
#     print(lista[100])
# except Exception as alias:
#     print(alias)

# a = 3
# b = [1, 0, 2]
# for elem in b:
#     if elem == 0:
#         raise ValueError("Zero nu se divide")
#     # raise ne da posibilitatea de a personaliza un mesaj de eroare
#
# # try, except, finally, raise.
#
# import pickle
#
# # data = {
# #     'a': [1, 2.0, 3, 4+6j],
# #     'b': ("Alice has a cat", "Python programming is great"),
# #     'c': [False, True, False]
# # }
#
# path_mine = "C:/Users/const/Dropbox/SDA/Code Python_41"
# path_file = f"{path_mine}/data.pickle"
#
# # with open(path_file, 'wb') as alias:
# #     pickle.dump(data, alias)
#
# with open(path_file, 'rb') as alias_2:
#     data_read = pickle.load(alias_2)
#
# # print(data_read)
# import pandas
# # modul pentru procesare de date de tip tabelar. Alternative: csv, polar etc.
# path_excel = 'C:/Users/const/Dropbox/SDA/Code Python_41/test_1.xlsx'
#
# tabel = pandas.read_excel(path_excel)
# print(tabel)

# json_ex = {"a":1, "b":2}
# import json
#
# path_json = f"C:/Users/const/Dropbox/SDA/Code Python_41/json_ex.json"
# #
# # json_obiect = json.dumps(json_ex)
# #
# # with open(path_json, 'w') as alias_json:
# #     alias_json.write(json_obiect)
#
# with open(path_json,'r') as alias_json_read:
#     data_json_read = json.load(alias_json_read)
#
# print(f"Datele din Json sunt: {data_json_read}")
#
# {'k1':3,'k2':9}
#

# #creati 3 fisiere json cu 2 chei: prima cheie un numar, a doua cu patratul acelui numar
#
import json
path_folder = "C:/Users/const/Dropbox/SDA/Code Python_41"

for x in range(3,6):
    # range(3,6) genereaza o lista de la 3-5
    jsonx = {'k1':x,'k2':x*x}
    #am creat iterativ fisierele json

    path_file = f"{path_folder}/file_{x}_patrat.json"
    #am creat calea fisierelor json in folderul ales in variabila path_folder

    json_obiect = json.dumps(jsonx, indent=4)
    #am creat obiectul json din dictionar in string, pentru a putea fi salvat in fisier

    with open(path_file, 'w') as alias_json:
        #am deschis fisierul salvat in path_file
        #am selectat operatiunea de "write" prin 'w'
        #am ales un alias pentru fisier
        alias_json.write(json_obiect)
        #in fisier am scris obiectul json_object care face face referire la jsonx


json_x = {"k1":[{"sk1": 2, "sk2": 3}],"k2":4}

print(json_x['k1'][0]['sk1'])
#
# dict_x = {'k1':1,'k2':2}
# print(dict_x['k1'])











