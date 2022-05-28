students_count = int(input("Ingrese cantidad de estudiantes: "))
students_grade_point_count = int(input("Ingrese la cantidad de notas por estudiantes: "))

for x in range(1, students_count + 1):
    print("Procesando estudiante N°: " + str(x))
    sum = 0
    for z in range(1, students_grade_point_count+1):
        grade_point = float(input("Ingrese nota N°" + str(z) + " :"))
        while grade_point < 0 or grade_point > 7 :
            grade_point = float(input("Ingrese nota N°" + str(z) + " :"))
        sum = sum + grade_point
    average = sum/students_grade_point_count
    print("El promedio de notas del estudiante " + str(x) + " es: " + str(average))
    if(average >= 6.5 ):
        print("Estudiante eximido, felicitaciones.")