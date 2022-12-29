import pickle
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class app_structure:
    def __init__(self):
        self.structure = {}
        self.directions = []
        self.linear_variables = []
        self.services = []    #list that hold directons to service


    def add_new_type(self, type_name):  #directions is a list with keys values from structure that provides access to proper destination in app
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        if type_name not in eval(temporary_string).keys():
            temporary_string += ".update(" + type_name + " = " + "{}" + ")"
            eval(temporary_string)
        else:
            return "nazwa " + type_name + " już istnieje, wybież inną nazwę"


    def add_new_service(self, service_name):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        if service_name not in eval(temporary_string).keys():
            temporary_string += ".update(" + service_name + " = " + "service()" + ")"
            eval(temporary_string)
            self.services.append(self.directions.copy() + [service_name])
        else:
            return "nazwa " + service_name + " już istnieje, wybież inną nazwę"


    def add_linear_paramether(self, coeffcient_name, coueffcient_value, variable_name):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".add_linear_paramether('" +  str(coeffcient_name) + "', '" +  str(coueffcient_value) + "','"  + str(variable_name) + "')"
        eval(temporary_string)


    def add_constant_paramether(self, constant_name, constant_value):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".add_constant_paramether('" +  str(constant_name) + "', '" + str(constant_value) + "')"
        eval(temporary_string)


    def add_precentage_counter(self, percentage):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".add_precentage_counter('" + str(percentage) + "')"
        eval(temporary_string)


    def calculate_cost_first_constant(self, linear_variables1):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".calculate_cost_first_constant('" + str(linear_variables1) + "')"
        return eval(temporary_string)


    def calculate_cost_second_constant(self, linear_variables1):    #nieurzywane
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".calculate_cost_second_constant('" + str(linear_variables1) + "')"
        return eval(temporary_string)


    def get_linear_variables(self, variable):        #wprowadza zmienne do policzenia ceny
        self.linear_variables.clear()
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".paramethers"
        paramethres = eval(temporary_string)
        for paramther in paramethres:
            self.linear_variables.append(float(input()))


    def inherit_paramether(self, paramether, key_value): #paramether is a dict ; key value is a list that have to be in path
        for path in self.services:
            temporary_string = "self.structure"
            if key_value == path[:len(key_value)]:
                for step in path:
                    temporary_string += ".get('" + str(step) + "')"
                temporary_string += ".paramethers.append(" + str(paramether) + ")"
                eval(temporary_string)


    def inherit_constant(self, constant, key_value):
        for path in self.services:
            temporary_string = "self.structure"
            if key_value == path[:len(key_value)]:
                for step in path:
                    temporary_string += ".get('" + str(step) + "')"
                temporary_string += ".constant.add(" + str(constant) + ")"
                eval(temporary_string)


    def inherit_percentage(self, percentage, key_value):
        for path in self.services:
            temporary_string = "self.structure"
            if key_value == path[:len(key_value)]:
                for step in path:
                    temporary_string += ".get('" + str(step) + "')"
                temporary_string += ".percentages.append(" + str(percentage) + ")"
                eval(temporary_string)


    def remove(self, name):
        temporary_string = "self.structure"
        del self.directions[len(self.directions) - 1]
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        temporary_string += ".pop('" + str(name) + "')"
        eval(temporary_string)


    def give_types_and_services(self):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        return eval(temporary_string).keys()

    def daj_nazwy_wspulczynnikow_liniowych(self):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        outcome = set(i["coeffcient_name"] for i in eval(temporary_string).paramethers)
        return outcome

    def daj_nazwy_stalych(self):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        outcome = set(i[0] for i in eval(temporary_string).constant)
        return outcome


    def daj_wartosci_mnoznikow(self):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        outcome = eval(temporary_string).percentages
        return outcome


    def czy_usluga(self, przyklad):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        return type(eval(temporary_string).get(przyklad)) != type({})


    def daj_wspulczynniki_liniowe(self):
        temporary_string = "self.structure"
        for i in self.directions:
            temporary_string += ".get('" + str(i) + "')"
        outcome = eval(temporary_string).paramethers
        return outcome

class service:
    def __init__(self):
        self.paramethers = []               # paramethers is a list of dictionaries where dictionaries are represent paramthres
        self.constant = set()               # constant is a set of tuples :(constant_name, constant_value)
        self.percentages = []

    def add_linear_paramether(self, coeffcient_name, coueffcient_value, variable_name):
        #this funcion add linear pramethers to pramethers list
        self.paramethers.append(dict((("coeffcient_name", coeffcient_name), ("coueffcient_value", float(coueffcient_value)), ("variable_name", variable_name))))


    def add_constant_paramether(self, constant_name, constant_value):
        # this is constant ingrideint of the sum
        self.constant.add((constant_name, constant_value))


    def add_precentage_counter(self, percentage):
        #this is a percentage counter that increases(or decreases) sum with is made of (constant) and linear parametres
        self.percentages.append(percentage)


    def calculate_cost_first_constant(self, variable_values):  #variable_values is a list of proper variables that matches paramtehers
        #this funcion returns outcome cost of service
        variable_values = eval(variable_values)
        cost = 0
        gen = zip(list(i["coueffcient_value"] for i in self.paramethers), variable_values)
        for pramether, value in gen:
            cost += pramether * value
        if len(self.constant) > 0:
            cost += sum(set(float(i[1]) for i in self.constant))
        if len(self.percentages) > 0:
            cost *= float(self.percentages[0])
        return cost


    def calculate_cost_second_constant(self, variable_values):  # variable_values is a list of proper variables that matches paramtehers
        # this funcion returns outcome cost of service
        variable_values = eval(variable_values)
        cost = 0
        gen = zip(list(i["coueffcient_value"] for i in self.paramethers), variable_values)
        for pramether, value in gen:
            cost += pramether * value
        cost *= float(self.percentages[0])
        cost += sum(set(float(i[1]) for i in self.constant))
        return cost




with open("data.txt", 'rb') as file:
    x = pickle.load(file)

x.directions.clear()


class MyGridLayout(GridLayout):
    pass


class aplikacja_do_wycen_App(App):
    def build(self):
        self.root = GridLayout(cols=1, spacing=10)
        with open("data.txt", 'rb') as file:
            self.x = pickle.load(file)
        self.x.directions.clear()
        self.count = 2
        def dostosowywanie_funkcji(przejscie, button):
            def zredukowaneprejsce(self, *args):
                return przejscie(button)
            return zredukowaneprejsce
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        layout = BoxLayout()
        layout.add_widget(Button(text="WRÓĆ", on_press = self.back, background_color =(0.4, 0.77, 1, 1)))
        layout.add_widget(Button(text="DODAJ +", on_press = self.dodaj, background_color =(0, 1, 0.4, 1)))
        self.root.add_widget(layout)

        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)
        return self.root


    def czy_na_pewno1(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text="Czy na pewno chcesz usunąć: " + str(self.x.directions[-1]) + "?"))
        la = BoxLayout()
        la.add_widget(Button(text="Tak", on_press = self.usun))
        la.add_widget(Button(text="Nie", on_press = self.dodaj_back))
        self.root.add_widget(la)
        self.count = 3
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def usun_typ(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.x.remove(self.x.directions[-1])
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

        def dostosowywanie_funkcji(przejscie, button):
            def zredukowaneprejsce(self, *args):
                return przejscie(button)
            return zredukowaneprejsce
        self.count = 2
        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        layout = BoxLayout()
        layout.add_widget(Button(text="DODAJ +", on_press = self.dodaj, background_color =(0, 1, 0.4, 1)))
        layout.add_widget(Button(text="WRÓĆ", on_press = self.back, background_color =(0.4, 0.77, 1, 1)))
        if len(self.x.directions) > 0 :
            layout.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press = self.czy_na_pewno1, background_color =(1, 0.2, 0.2, 1)))
            self.count += 1
        self.root.add_widget(layout)
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def diresctionsstr(self, directions):
        str = ""
        for i in directions:
            str += i + " -> "
        str = str[:-4]
        return str

    def service_options(self, button_name, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.x.directions.append(button_name)
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        layout = BoxLayout()
        layout.add_widget(Button(text="oblicz cenę", on_press = self.oblicz_cene))
        layout.add_widget(Button(text="ustawienia", on_press = self.ustawienia_uslugi))
        self.root.add_widget(layout)
        self.root.add_widget(Button(text="WRÓĆ", on_press = self.back, background_color =(0.4, 0.77, 1, 1)))
        self.count = 3
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def oblicz_cene(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1

        self.count = 4
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text="oblicz cenę"))
        self.robocze = list(range(len(self.x.daj_wspulczynniki_liniowe())))
        licznik = 0
        for i in self.x.daj_wspulczynniki_liniowe():
            self.root.add_widget(Label(text='Nazwa wspułczynnika: ' + str(i["coeffcient_name"] + "       Nazwa zmiennej" + str(str(i["variable_name"])))))
            self.robocze[licznik] = TextInput(text='', multiline=False)
            self.root.add_widget(self.robocze[licznik])
            self.count += 2
            licznik += 1
        self.root.add_widget(Button(text="Oblicz", on_press = self.oblicz))
        self.root.add_widget(Button(text="WRÓĆ", on_press = self.service_options, background_color =(0.4, 0.77, 1, 1)))
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def oblicz(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.zmienne = list(int(i.text) for i in self.robocze)
        wynik = self.x.calculate_cost_first_constant(self.zmienne)
        wynik_końcowy = "{:.2f}".format(wynik)
        self.root.add_widget(Label(text="Wynik to: " + str(wynik_końcowy) + " zł"))
        self.root.add_widget(Button(text="Kontynuuj", on_press = self.back))
        self.count = 2
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)


    def przejscie(self, button_name, *args):

        def dostosowywanie_funkcji(przejscie, button):

            def zredukowaneprejsce(self, *args):
                return przejscie(button)
            return zredukowaneprejsce

        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.count = 2
        self.x.directions.append(button_name)
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        la = BoxLayout()

        la.add_widget(Button(text="WRÓĆ", on_press = self.back, background_color =(0.4, 0.77, 1, 1)))
        la.add_widget(Button(text="DODAJ +", on_press = self.dodaj, background_color =(0, 1, 0.4, 1)))
        if len(self.x.directions) > 0 :
            la.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press = self.czy_na_pewno1, background_color =(1, 0.2, 0.2, 1)))
        self.root.add_widget(la)

        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)


    def przejscieservice(self, button_name, *args):
        def dostosowywanie_funkcji(przejscie, button):

            def zredukowaneprejsce(self, *args):
                return przejscie(button)

            return zredukowaneprejsce

        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.count = 2
        self.x.directions.pop()
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))

        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        la = BoxLayout()

        la.add_widget(Button(text="WRÓĆ", on_press=self.back, background_color=(0.4, 0.77, 1, 1)))
        la.add_widget(Button(text="DODAJ +", on_press=self.dodaj, background_color=(0, 1, 0.4, 1)))
        if len(self.x.directions) > 0:
            la.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press=self.czy_na_pewno1,
                                 background_color=(1, 0.2, 0.2, 1)))
        self.root.add_widget(la)

        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def back(self, *args):
        if len(self.x.directions) != 0:
            def dostosowywanie_funkcji(przejscie, button):

                def zredukowaneprejsce(self, *args):
                    return przejscie(button)
                return zredukowaneprejsce
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.x.directions.pop()
            strr = self.diresctionsstr(self.x.directions)
            if len(strr) == 0:
                strr = "Strona początkowa"
            self.root.add_widget(Label(text=strr))
            self.count = 2
            for button in self.x.give_types_and_services():
                if self.x.czy_usluga(button):
                    func = dostosowywanie_funkcji(self.service_options, button)
                    self.root.add_widget(Button(text=button, on_press=func, background_color=(0, 0.5, 1, 1)))
                    self.count += 1
                else:
                    func = dostosowywanie_funkcji(self.przejscie, button)
                    self.root.add_widget(Button(text=button, on_press=func))
                    self.count += 1
            la = BoxLayout()

            la.add_widget(Button(text="WRÓĆ", on_press=self.back, background_color=(0.4, 0.77, 1, 1)))
            la.add_widget(Button(text="DODAJ +", on_press=self.dodaj, background_color=(0, 1, 0.4, 1)))
            if len(self.x.directions) > 0:
                la.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press=self.czy_na_pewno1,
                                     background_color=(1, 0.2, 0.2, 1)))
            self.root.add_widget(la)

            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)


    def dodaj_back(self, *args):
        def dostosowywanie_funkcji(przejscie, button):

            def zredukowaneprejsce(self, *args):
                return przejscie(button)

            return zredukowaneprejsce

        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        self.count = 2
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        la = BoxLayout()

        la.add_widget(Button(text="WRÓĆ", on_press=self.back, background_color=(0.4, 0.77, 1, 1)))
        la.add_widget(Button(text="DODAJ +", on_press=self.dodaj, background_color=(0, 1, 0.4, 1)))
        if len(self.x.directions) > 0:
            la.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press=self.czy_na_pewno1,
                                 background_color=(1, 0.2, 0.2, 1)))
        self.root.add_widget(la)

        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def dodaj(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.count = 4
        self.root.add_widget(Label(text="DODAJ +"))
        la = BoxLayout()
        la.add_widget(Button(text="usługę", on_press=self.dodaj_usluge))
        la.add_widget(Button(text="typ usług", on_press=self.dodaj_typ_uslug))
        self.root.add_widget(la)
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.dodaj_back, background_color =(0.4, 0.77, 1, 1)))
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def dodaj_usluge(self, *args):
        self.nowa_usluga = {}
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text='Podaj nazwę usługi'))
        self.tekst = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst)
        self.root.add_widget(Button(text="zatwierdź", on_press = self.zatwierdz_nawe_uslugi))
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.dodaj, background_color =(0.4, 0.77, 1, 1)))
        self.count = 5
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)


    def dodaj_typ_uslug(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text='Podaj nazwę typu usług'))
        self.tekst = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst)
        self.root.add_widget(Button(text="zatwierdź", on_press = self.zatwierdz_nawe_typu_uslug))
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.dodaj, background_color =(0.4, 0.77, 1, 1)))
        self.count = 5
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def zatwierdz_nawe_typu_uslug(self, *args):
        try:
            self.x.add_new_type(self.tekst.text)
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            strr = self.diresctionsstr(self.x.directions)
            if len(strr) == 0:
                strr = "Strona początkowa"
            self.root.add_widget(Label(text=strr))
            self.root.add_widget(Label(text="Dodano nowy typ: "+ str(self.tekst.text)))
            self.root.add_widget(Button(text="Kontynuuj", on_press = self.dodaj_back))
            self.count = 3
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Użyto spacji, lub innego niedozwolonego znaku. Spróbuj inną nazwę."))
            self.root.add_widget(Button(text="Powrót", on_press = self.dodaj_typ_uslug))
            self.count = 2
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def zatwierdz_nawe_uslugi(self, *args):
        try:
            self.x.add_new_service(self.tekst.text)
            self.x.directions.append(self.tekst.text)
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            strr = self.diresctionsstr(self.x.directions)
            if len(strr) == 0:
                strr = "Strona początkowa"
            self.root.add_widget(Label(text=strr))
            self.root.add_widget(Label(text="Dodano nowa usluge: " + str(self.tekst.text)))
            self.root.add_widget(Button(text="Kontynuuj", on_press = self.ustawienia_uslugi))
            self.count = 3
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Użyto spacji, lub innego niedozwolonego znaku. Spróbuj inną nazwę."))
            self.root.add_widget(Button(text="Powrót", on_press = self.dodaj_usluge))
            self.count = 2


    def ustawienia_uslugi(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Button(text="dodaj współczynnik liniowy", on_press = self.dodaj_wsp_lin))
        wsplin=""
        for i in self.x.daj_nazwy_wspulczynnikow_liniowych():
            wsplin += i + ", "
        wsplin = wsplin[:-2]
        self.root.add_widget(Label(text="dodane współczynniki: " + wsplin))
        self.root.add_widget(Button(text="dodaj stałą", on_press = self.dodaj_stala))
        stale=""
        for i in self.x.daj_nazwy_stalych():
            stale += i + ", "
        stale = stale[:-2]
        self.root.add_widget(Label(text="dodane stale: " + stale))
        self.root.add_widget(Button(text="dodaj mnożnik", on_press = self.dodaj_mnoznik))
        wsplin=""
        for i in self.x.daj_wartosci_mnoznikow():
            wsplin += str(i) + ", "
        wsplin = wsplin[:-2]
        self.root.add_widget(Label(text="dodane mnożniki: " + wsplin))
        la = BoxLayout()
        la.add_widget(Button(text="USUŃ", on_press=self.czy_na_pewno, background_color =(1, 0.2, 0.2, 1)))
        la.add_widget(Button(text="WRÓĆ", on_press=self.back, background_color =(0.4, 0.77, 1, 1)))
        self.root.add_widget(la)
        self.count = 8
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def dodaj_wsp_lin(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text='Podaj nazwę wspulczynnika(np.cena ramki)'))
        self.tekst1 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst1)
        self.root.add_widget(Label(text='Podaj wartosc wspulczynnika(np.10(zł/m) (nie podawaj jednostki!(sama liczba)))'))
        self.tekst2 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst2)
        self.root.add_widget(Label(text='Podaj zmiennej(np.obwód(polecam przy nazwie podać jednostkę np.: obwód (w metrach)))'))
        self.tekst3 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst3)
        la = BoxLayout()

        la.add_widget(Button(text="zatwierdź", on_press=self.zatwierdz_wsp_lin))
        if len(self.x.directions) == 1:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług" ,
                                 on_press=self.odziedzicz_wsp_lin))
        else:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług w " + str(self.x.directions[-2]), on_press=self.odziedzicz_wsp_lin))
        self.root.add_widget(la)
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.ustawienia_uslugi, background_color =(0.4, 0.77, 1, 1)))
        self.count = 9
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def odziedzicz_wsp_lin(self, *args):
        try:
            self.x.inherit_paramether( dict((("coeffcient_name", self.tekst1.text), ("coueffcient_value", float(self.tekst2.text)), ("variable_name", self.tekst3.text))), self.x.directions[:-1])

            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Pomyślnie dodano parametr do pozostałych usług"))
            self.root.add_widget(Button(text="Kontynuuj", on_press=self.ustawienia_uslugi))
            self.count = 2
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2

    def odziedzicz_stala(self, *args):
        try:
            stala = (self.tekst1.text, self.tekst2.text)
            self.x.inherit_constant( stala, self.x.directions[:-1])

            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Pomyślnie dodano parametr do pozostałych usług"))
            self.root.add_widget(Button(text="Kontynuuj", on_press=self.ustawienia_uslugi))
            self.count = 2
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2


    def odziedzicz_mnoznik(self, *args):
        try:
            self.x.inherit_percentage( self.tekst1.text, self.x.directions[:-1])

            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Pomyślnie dodano parametr do pozostałych usług"))
            self.root.add_widget(Button(text="Kontynuuj", on_press=self.ustawienia_uslugi))
            self.count = 2
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2



    def zatwierdz_wsp_lin(self, *args):
        try:
            self.x.add_linear_paramether(self.tekst1.text, self.tekst2.text, self.tekst3.text)
            self.ustawienia_uslugi()
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2



    def dodaj_stala(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text='Podaj nazwę stalej(np. robocizna)'))
        self.tekst1 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst1)
        self.root.add_widget(Label(text='Podaj wartosc stalej(w złowtówkach)'))
        self.tekst2 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst2)
        la = BoxLayout()
        la.add_widget(Button(text="zatwierdź", on_press=self.zatwierdz_stala))
        if len(self.x.directions) == 1:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług" ,
                                 on_press=self.odziedzicz_stala))
        else:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług w " + str(self.x.directions[-2]), on_press=self.odziedzicz_stala))
        self.root.add_widget(la)
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.ustawienia_uslugi, background_color =(0.4, 0.77, 1, 1)))
        self.count = 7
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def zatwierdz_stala(self, *args):
        try:
            self.x.add_constant_paramether(self.tekst1.text, self.tekst2.text)
            self.ustawienia_uslugi()
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2


    def dodaj_mnoznik(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text='Podaj wartosc mnoznika (np. 1.23)'))
        self.tekst1 = TextInput(text='', multiline=False)
        self.root.add_widget(self.tekst1)
        la = BoxLayout()
        la.add_widget(Button(text="zatwierdź", on_press=self.zatwierdz_mnoznik))
        if len(self.x.directions) == 1:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług" ,
                                 on_press=self.odziedzicz_mnoznik))
        else:
            la.add_widget(Button(text="skopiuj współczynnik do wszystkich usług w " + str(self.x.directions[-2]), on_press=self.odziedzicz_mnoznik))
        self.root.add_widget(la)
        self.root.add_widget(Button(text="WRÓĆ", on_press=self.ustawienia_uslugi, background_color =(0.4, 0.77, 1, 1)))
        self.count = 5
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def zatwierdz_mnoznik(self, *args):
        try:
            self.x.add_precentage_counter(self.tekst1.text)
            self.ustawienia_uslugi()
            with open("data.txt", "wb") as file:
                pickle.dump(self.x, file)
        except:
            while self.count > 0:
                self.root.remove_widget(self.root.children[0])
                self.count -= 1
            self.root.add_widget(Label(text="Podano, złe wartości wsułczynnika (np. wyrazy w rubryce na wartość liczbową)"))
            self.root.add_widget(Button(text="Powrót", on_press=self.dodaj_wsp_lin))
            self.count = 2

    def czy_na_pewno(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))
        self.root.add_widget(Label(text="Czy na pewno chcesz usunąć: " + str(self.x.directions[-1]) + "?"))
        la = BoxLayout()
        la.add_widget(Button(text="Tak", on_press = self.usun))
        la.add_widget(Button(text="Nie", on_press = self.ustawienia_uslugi))
        self.root.add_widget(la)
        self.count = 3
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

    def usun(self, *args):
        while self.count > 0:
            self.root.remove_widget(self.root.children[0])
            self.count -= 1

        self.x.remove(self.x.directions[-1])
        strr = self.diresctionsstr(self.x.directions)
        if len(strr) == 0 :
            strr = "Strona początkowa"
        self.root.add_widget(Label(text=strr))


        def dostosowywanie_funkcji(przejscie, button):
            def zredukowaneprejsce(self, *args):
                return przejscie(button)
            return zredukowaneprejsce
        self.count = 2
        for button in self.x.give_types_and_services():
            if self.x.czy_usluga(button):
                func = dostosowywanie_funkcji(self.service_options, button)
                self.root.add_widget(Button(text=button, on_press=func, background_color =(0, 0.5, 1, 1)))
                self.count += 1
            else:
                func = dostosowywanie_funkcji(self.przejscie, button)
                self.root.add_widget(Button(text=button, on_press=func))
                self.count += 1
        la = BoxLayout()
        la.add_widget(Button(text="WRÓĆ", on_press = self.back, background_color =(0.4, 0.77, 1, 1)))
        la.add_widget(Button(text="DODAJ +", on_press = self.dodaj, background_color =(0, 1, 0.4, 1)))
        if len(self.x.directions) > 0 :
            la.add_widget(Button(text="USUŃ: " + str(self.x.directions[-1]), on_press = self.czy_na_pewno1, background_color =(1, 0.2, 0.2, 1)))
        self.root.add_widget(la)
        with open("data.txt", "wb") as file:
            pickle.dump(self.x, file)

if __name__ == '__main__':
    app = aplikacja_do_wycen_App()
    app.run()


