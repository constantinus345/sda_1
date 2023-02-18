# import json
#
#
# path_file = 'C:/Users/const/Dropbox/SDA/Code Python_41/fisier_ex_1.json'
#
# with open(path_file,'r') as f:
#     data = json.load(f)
#     print(data)
#
# l_test = [1,'a']
# print(sum(l_test))
#
#
# def avg(lista):
#     try:
#         suma = sum(lista)
#     except TypeError:
#         suma = 'E o eroare in lista, probabil nu toate elementele sunt integer'
#     return suma / len(lista)
#
# average_right = round(avg(data['right_side']),2)
# print(f"average_right = {average_right}")
#
# average_left = round(avg(data['left_side']),2)
# print(f"average_left = {average_left}")
#
# average_both = (average_right + average_left)/2
# print(f"average_both = {average_both}")



import csv

def csv_to_list_of_jsons(path_to_csv):

    lista_date = []
    with open(path_to_csv,'r') as c1:
        data = csv.reader(c1)
        # print(data)
        for row in data:
            # print(row)
            lista_date.append(row)


    # cheile = lista_date[0]
    # valoarea_1 = lista_date[1]
    # #print(list(zip(cheile, valoarea_1)))

    results_json = []


    for index, el_csv in enumerate(lista_date):
        if index == 0:
            cheile = lista_date[index]
        else:
            randul_x = lista_date[index]

            json_x = dict(zip(cheile,randul_x))
            #print(json_x)
            results_json.append(json_x)

    #print(results_json)
    #print(len(results_json))
    return results_json

csv_path = 'C:/Users/const/Dropbox/SDA/Code Python_41/data_csv.csv'

lista_jsons = csv_to_list_of_jsons(csv_path)
print(lista_jsons)
print(len(lista_jsons))


# string_x = """andrei
# vasile"""
#
# split_x = string_x.split('\n')
# print(split_x)