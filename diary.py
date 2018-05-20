import sys
from collections import OrderedDict
from peewee import *
import datetime
db=SqliteDatabase('diary.db')#el nombre de la base de datos

class Entry(Model):
    content= TextField()
    timestamp=DateTimeField(default=datetime.datetime.now)#permite cojer la fecha y la hora de entrada de este modulo
    class Meta:
        database=db
#METODOS
def add_entry():
    """Agregar un registro"""
    print("Introduzca un registro, Presione Ctrl+z+Enter para terminar")
    data=sys.stdin.read().strip()#permite seguir trabajando hasta q el usurioa queira parar de hacer
    #en este caso solo parara cuando aplatemos ctrl+z+enter
#esto es para guardar en la base de datos el if
    if data:
        if input("Desea Guardaar este Registro [Y/N] : ").lower() == 'y':
              Entry.create(content=data)
              print("SE HA GUARDADO EXITOSAMENTE")
def view_entries():
    """Ver registros"""
    entries=Entry.select().order_by(Entry.timestamp.desc())
    for entry in entries:
        timestamp=entry.timestamp.strftime('%A %B %D, %Y %I:%M%p')
        print(timestamp)
        print("_-_-_-_-_-_")
        print(entry.content)
        print("n----> Ver el siguiente registro")
        print("q----> Salir del menu")

        next_entry=input("Desea ver la siguiente entrada [n/q]").lower().strip()
        if next_entry=='q':
            break

def delete_entries():
    """Eliminar registro"""

menu=OrderedDict([#con este metodo simpre aparce el menu en el orden ingresado
    ('a',add_entry),
    ('v',view_entries),
])

def menu_loop():
    """Mostrar opciones"""
    choice=None
    while choice != 'x':#mientras la opcion q capture sea diferente de x se repite si aplasta x se sale
        print("Presiona 'x' para salir ")
        for key, value in menu.items():#nos permite corrernos cada uno de los elementos q nos manden nuestros elementos
            print('{}---->{}'.format(key,value.__doc__))
        choice=input("Escoja Opcion : ").lower().strip()#el strip permite eliminar los espacios o letras q se ponga asi''
        #se captura lo q el ususario escoja y ademas se manda el comentario
        #vamos a evaluar si nuestra opcion esta dentro de nuestro menu
        if choice in menu:
            menu[choice]()
def init(): #metodo propio para q se conecte
        db.connect()
        db.create_tables([Entry],safe=True)#se crea tablas
if __name__ == '__main__':
    init()#llama al metodo
    menu_loop()
