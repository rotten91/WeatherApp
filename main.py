import sys
from data_driver import DataDriver
import contextlib


class Main():

    def __init__(self):
        self.wu_key = '8aa4b38d78a0c7b3'
        self.io_key = '15f0dcbd752adbe5bc417321d6d8f3dd'

    def welcome(self):
        with contextlib.closing(open('welcome.txt', 'r')) as f:
            print(f.read())

    def menu(self):
        self.welcome()
        try:
            choice = int(input(">>>"))
        except ValueError:
            sys.stderr.write("NIE MA TAKIEJ OPCJI ")
        except UnboundLocalError:
            sys.stderr.write("CYFERKIII")
        try:
            while True:
                if choice == 1:
                    print("Wpisz nazwe miasta : \n")
                    try:
                        city = str(input(">>>"))
                        DataDriver(wu_apikey=self.wu_key,
                                   io_apikey=self.io_key, city=city).fetch_data()
                        start.menu()
                    except AttributeError:
                        sys.stderr.write("Nie ma takiego miasta \n")
                elif choice == 2:
                    print("Wpisz nazwe wybranego miasta : \n")
                    try:
                        city = str(input(">>>"))
                        DataDriver(wu_apikey=self.wu_key,
                                   io_apikey=self.io_key, city=city).print_file()
                        start.menu()
                    except AttributeError:
                        sys.stderr.write("Nie ma podanego miasta w bazie\n")
                elif choice == 3:
                    break
        except UnboundLocalError:
            sys.stderr.write("Uzywamy cyfr 1-3! :)\n")
            start.menu()
if __name__ == '__main__':
    start = Main()
    start.menu()
