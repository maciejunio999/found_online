FILE_PATH = "** put your path **"

def file_to_dic(file_path):

    ls = []

    with open(file_path, 'r') as file:
        for line in file:
            ls.append(line.strip())

    lines = {}

    for i in ls:
        x = i.split(' ')
        lines[x[0]] = {'name': x[1] + ' ' + x[2], 'grades': x[3:]}

    return lines

students_with_grades = file_to_dic(FILE_PATH)

def calculate_mean_of_grades(slownik):
    slownik2 = {}

    for uczen in slownik:
        amount_of_grades = 0
        sum = 0
        for grade in slownik[uczen]['grades']:
            amount_of_grades += 1
            sum += int(grade)
        mean = sum / amount_of_grades
        slownik2[uczen] = {'name': slownik[uczen]['name'], 'mean': round(mean, 2)}
    
    return slownik2

students_with_mean = calculate_mean_of_grades(students_with_grades)

write_path = "** put your path **"

with open(write_path, 'w') as outfile:
    for uczen in students_with_mean:
        outfile.write(f'{uczen} {students_with_mean[uczen]["name"]} {students_with_mean[uczen]["mean"]} \n')