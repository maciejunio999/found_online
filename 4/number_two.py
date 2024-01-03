import csv
import os.path

FILE_PATH = "** your path**"

check_file = os.path.isfile(FILE_PATH)

def main(file_path):
    main_dict = {}

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["user"]} has password: {row["password"]}.')
            main_dict[row["user"]] = row["password"]
            line_count += 1
        print(f'Processed {line_count} lines.')

    print(main_dict)

    user = ''

    while user != 'q':
        user = input("Tell us Your username: ").strip()
        if 'q' == user:
            break
        password = input("Tell us Your password for this username: ").strip()
        if 0 < len(user) and 0 < len(password):
            main_dict[user] = password
        else:
            print("Put username and password or end.")

    print(main_dict)

    main_list = [[key, value] for key, value in main_dict.items()]

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([["user", "password"]])
        writer.writerows(main_list)

def create_file(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        field = [["user", "password"]]
        
        writer.writerow(field)

if check_file:
    main(FILE_PATH)
else:
    print('nofile')
    create_file(FILE_PATH)
    main(FILE_PATH)