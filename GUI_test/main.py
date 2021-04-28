import PySimpleGUI as gui


class Person:
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number

    def print_person(self):
        print(f"{self.name} {self.last_name} {self.number}")

    def get_person(self):
        return [self.name, self.last_name, self.number]


main_phone_book = [(Person)]
gui.theme('Green')  # Motyw kolorystyczny


def load_data():  # Polskie znaki wywalają prgram podczas ładowania
    del main_phone_book[:]
    data = open("data.txt", "r", encoding="utf-8")
    for line in data:
        line = line.split()
        main_phone_book.append(Person(line[0], line[1], line[2]))
    data.close()


def add_person():
    person = input("Wprowadź imię, nazwisko i numer (oddziel spacjami)").split()
    data = open("data.txt", "a")
    data.write("\n")
    data.write(""f"{person[0].capitalize()} {person[1].capitalize()} {person[2]}")
    data.close()
    load_data()


def print_all_text(book):
    for person in book:
        person.print_person()


def print_all_window(book):
    # layout to zmienna, która przechowywuje "format" okna. Jest to lista, składająca się z list. Każda lista wewnątrz
    # zmiennej layout to nowy wiersz
    layout = [[gui.Text('Wszystkie kontakty:', size=(20, 1), justification="c", font=("Helvetica", 20))]]  # Tytuł
    for i in range(
            len(book)):  # W forze do listy layout dodaję appendem kolejne wiersze. Każdy wiersz to nowa osoba
        layout.append([gui.Text(i), gui.Text(' '.join(book[i].get_person()), font=("Helvetica", 10))])
    # Poniżej dodaję jakieś bezcelowe przyciski i paski, które mogą zostać wykorzystane do wprowadzania i zapisywania nowych kontaktów itp.
    layout.append([gui.Text("Jakieś pole"), gui.Input()])
    layout.append([gui.Button("Wyszukaj kontakt"), gui.Button("Zapisz kontakt")])
    # Tworzę zmienną window, która jest otwartym nowym oknem, z argumentem layout

    window = gui.Window('Ksionszka', layout)

    # Warunki zamknięcia okna
    event, values = window.read()

    # Zamykanie okna
    window.close()


def main():
    load_data()
    proceed = 'Y'
    while proceed.upper() == 'Y':
        add_person()
        print_all_text(main_phone_book)
        print_all_window(main_phone_book)
        proceed = input("Kontynuować działanie (y/n)")


main()
