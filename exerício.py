students = []
for item in students:
    print (item)

def creat_new_student(nome, matricula, senha):
    new_student = {"nome": "" , "matrícula": "", "senha": ""}

    new_student["nome"] = nome
    new_student["matrícula"] = matricula
    new_student["senha"] = senha

    students.append(new_student)
    return "Aluno cadastrado com sucesso!"
    
print(creat_new_student("Camila", 832483, 2271009))
creat_new_student("Ana", 112233, 1234567)
creat_new_student("Alberto", 223344, 7654321)
   
def get_student_name(nome):
    for item in students:
        if item["nome"] == nome:
            return(item)
print(get_student_name("Camila"))