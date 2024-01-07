import os.path

class Slownik():
    def __init__(self):
        self.slownik = {}

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                print(line)
                try:
                    x, y = line.split(';')
                    key, value = x.strip(), y.strip()
                    self.slownik[key] = value
                except ValueError:
                    pass
    
    def write_file(self, file_path):
        if os.path.isfile(file_path):
            mode = 'w'
        else:
            mode = 'x'
        with open(file_path, mode) as file:
            for i in self.slownik:
                file.write(f'{i};{self.slownik[i]}\n')

klasa = Slownik()
print(klasa.slownik)
klasa.read_file('** first file path **')
print(klasa.slownik)
klasa.read_file('** second file path **')
print(klasa.slownik)
klasa.write_file('** out file path **')