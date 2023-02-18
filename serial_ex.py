#Creati o variabila JSON cu 3 chei, dintre care o cheie sa contina o lista cu 2 dictionare cu 2 chei
#Salvati continutul acestei variabile intr-un fisier pe desktop
#Cititi continutul acestui fisier, printati tot continutul
#Printati doar a 2-a cheie
#printati a doua subcheie din primul dictionar din cheia "etajata"

#Creati o variabila valida CSV cu header 3 coloane si 2 randuri
#Salvati acest fisier pe desktop
#printati acest fisier

#fara context manager => riscante, not good
f= file.open()
f.write("safa")
f.close()

#context manager
with open(file, 'operatiune w sau r etc') as alias:
    pass #fa ceva
# operatiunea de deschidere si inchidere se face automat
# implicit mai putine riscuri- pierderea datelor, supraincarcarea memoriei etc.



