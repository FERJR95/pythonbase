from peewee import *

db=SqliteDatabase('students.db')#el nombre de la base de datos

class Student(Model):#para importar la clase sin el model no funciona
    username=CharField(max_length=255, unique=True)
    points=IntegerField(default=0)
#el modelo siempre tendra q tener una base meta
    class Meta:
        database=db
#siempre debera contener un if:
students=[
    {'username':'Aldo','points':10},
    {'username':'Betty','points':7},
    {'username':'Ariel','points':9},
    {'username':'Jairo','points':0},
    {'username':'Dayana','points':9},

    ]
#metodo para anadir estudiantes
def add_students():
    for student in students:
        try:
            #crear mi registro
            Student.create(username=student['username']
                          ,points=student['points'])
        except IntegrityError:#cuando ya existe me vota el IntegrityError
            student_records= Student.get(username=student['username'])
            student_records.points=student['points']#para q se actualize solo las calificaciones
            student_records.save()#guardar cambios
#metodo que me obtenga el alumno con la calificacion mas alta
def top_student():
    topcalif= Student.select().order_by(Student.points.desc()).get()#para hacer los querys siempre poner la clase
    return topcalif #retornamos la calificacion

if __name__ == '__main__':
    db.connect()#con esto se conecta a la base de datos
    db.create_tables([Student],safe=True)#aqui van todos los modelos q tengamos con el safe se verifica si existe o no la tabla
    add_students()
    print('El mejor estudiante es : {}'.format(top_student().username))#el format todo lo q este dentro del metodo format se coloca en las llaves
