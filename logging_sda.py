import logging

logging.basicConfig(filename='loger_sda.log', format = '%(asctime)s %(message)s', filemode='w')

obj_log = logging.getLogger()

"""
Niveluri de logging: 
debug: cel mai jos nivel de alerta
info: info
warning: atrage atentia
error
critical
"""

obj_log.setLevel(logging.DEBUG)
obj_log.debug("Just an info")


def division_stuff(x, y):
    return x/y

a = 8
b= 0

try:
    print(division_stuff(a,b))
    obj_log.info("Done division")
except ZeroDivisionError:
    obj_log.critical(f"Zero division of function division_stuff with arguments {a,b}")