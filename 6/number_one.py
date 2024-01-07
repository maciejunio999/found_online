import os.path

class PhoneBook():
    def __init__(self):
        self.slownik = {}

    def read(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    print(line)
                    try:
                        x, y = line.split(',')
                        key, value = x.strip(), y.strip()
                        self.slownik[key] = value
                    except ValueError:
                        pass
        else:
            print("There is no such file.")
        
    
    def add_record(self, name_and_phone):
        name, phone = name_and_phone.split(',')
        key, value = name.strip(), phone.strip()
        if 0 < len(key):
            print(f"Added user named: {key}.")
            self.slownik[key] = value
        else:
            print("You have to give at least name.")
    
    def write(self, file_path):
        if os.path.isfile(file_path):
            print("Modified file under given path.")
            mode = 'w'
        else:
            print("Created file under given path.")
            mode = 'x'
        with open(file_path, mode) as file:
            for i in self.slownik:
                file.write(f'{i},{self.slownik[i]}\n')

READ_FILE = "** your file in path **"
WRITE_FILE = "** your file out path **"

pb = PhoneBook()
print(pb.slownik)
pb.read(READ_FILE),
print(pb.slownik)
pb.add_record('maciek,123456789')
print(pb.slownik)
pb.write(WRITE_FILE)
pb.add_record('ala,')
pb.add_record(',987654321')
pb.write(WRITE_FILE)