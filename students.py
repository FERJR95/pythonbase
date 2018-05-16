from peewee import *

db=SqliteDatabase('students.db')#el nombre de la base de datos

class Student(Model):#para importar la clase sin el model no funciona
    username=CharField(max_length=255, unique=True)
    points=IntegerField(default=0)
#el modelo siempre tendra q tener una base meta
    class Meta:
        database=db
#siempre debera contener un if:

if __name__ == '__main__':
    db.connect()#con esto se conecta a la base de datos
    db.create_tables([Student],safe=True)#aqui van todos los modelos q tengamos con el safe se verifica si existe o no la tabla
