import os.path
import re



class NoGivenNameAndPhoneException(Exception):
    "The given value doesn't include name or phone of user."
    pass

class PhoneLengthError(Exception):
    len = 9

    def __init__(self, phone, *args):
        super().__init__(args)
        self.phone = phone

    def __str__(self):
        return f'The {self.phone} is not in a valid length {self.len}'

class PhoneIncludesLettersError(Exception):
    def __init__(self, phone, *args):
        super().__init__(args)
        self.phone = phone

    def __str__(self):
        return f'The {self.phone} includes letters, so its invalid'



class PhoneBook():
    def __init__(self):
        self.slownik = {}

    def read(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        x, y = line.split(',')
                        key, value = x.strip(), y.strip()
                        self.slownik[key] = value
                    except ValueError:
                        pass
        else:
            raise FileNotFoundError
        
    
    def add_record(self, name_and_phone):
        name, phone = name_and_phone.split(',')
        key, value = name.strip(), phone.strip()
        if 0 < len(key) and 0 < len(value):
            if 9 == len(value):
                if re.search('[a-zA-Z]', value):
                    raise PhoneIncludesLettersError(value)
                else:
                    print(f"Added user named: {key}.")
                    self.slownik[key] = value
                
            else:
                raise PhoneLengthError(value)
        else:
            raise NoGivenNameAndPhoneException
    
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
pb.read(READ_FILE)
#pb.add_record('maciek,')
#pb.add_record(',123456789')
pb.add_record('maciek,123456789')
#pb.add_record('ala,1234aaaaa')
#pb.add_record('ala,124')
pb.write(WRITE_FILE)