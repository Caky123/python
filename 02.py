class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

class Student(Osoba):
    def __init__(self, jmeno, obor):
        super().__init__(jmeno)
        self.obor = obor

    def predstav_se(self):
        print(f"Jsem {self.jmeno} a studuji {self.obor}")

class Ucitel(Osoba):
    def __init__(self, jmeno, predmet):
        super().__init__(jmeno)
        self.predmet = predmet

    def predstav_se(self):
        print(f"Jsem {self.jmeno} a vyučuji {self.predmet}")


student = Student("Eva", "Matematika")
ucitel = Ucitel("Petr", "Programování")

for osoba in [student, ucitel]:
    osoba.predstav_se()
