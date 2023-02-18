# import threading
#
# def print_pe_bucatele(interabil_x):
#     for el in interabil_x:
#         print(el)
#
# t1 = threading.Thread(target=print_pe_bucatele, args=([1,2,3,4,5,100],))
# t2 = threading.Thread(target=print_pe_bucatele, args = ("Alexandru",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

#Expected results: printarea poate fi executata in paralel, si e posibila printarea concomitent din ambele threaduri

# printati primele 10 elemente din fisierele txt dintr-un folder de pe PC-ul vostru, folosind context manager, exception handling si os.listdir

import os

path_folder = 'C:/Users/const/Dropbox/SDA/Code Python_41'
fisierele = [file for file in os.listdir(path_folder) if file.endswith('.txt')]
print(fisierele)

for filex in fisierele:
    try:
        with open(f'{path_folder}/{filex}', 'r') as f:
            data = f.read()
            print(f"data complet din fisierul {filex} = {data}")
            print(f"primele 10 car = {data[:10]}")

    except Exception as e:
        #best case pentru exceptii este de a gestiona fiecare tip de exceptie in parte
        print(f'Exceptia intalnita este = {e}')
    finally:
        print(f"Yeeey am terminat de citit fisierul {filex}")
    print(f"{'_' * 60}")




#
#
#
# import os
#
# folder_path = 'C:/Users/const/Dropbox/SDA/Code Python_41'
# files = os.listdir(folder_path)
#
# txt_files = [x for x in files if x.endswith('.txt')]
# print(f"Fisierele txt sunt: {txt_files}")
#
# for txtx in txt_files:
#     try:
#         with open(f'{folder_path}/{txtx}','r') as f:
#             data = f.read()
#             print(f"Data complet in {txtx} = {data}")
#             print(f"data :10 = {data[:10]}")
#     except Exception as e:
#         print(f"Numele exceptiei de deschidere a fisierului este: {e}")
#     finally:
#         print("Yeey, am terminat")