class Country:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display(self):
        print('국가명:',self.name, ', 인구수:', self.number)

class NewCountry(Country):

    def __init__(self, name, number, capital):
        super().__init__(name, number)
        self.capital = capital

    def display(self):
        print('국가명:',self.name, ', 인구수:', self.number,', 수도명:',self.capital)

aCountry = Country('Korea', 5000)
bCountry = NewCountry('NewWorld', 5000, 'Seoul')
aCountry.display()
bCountry.display()
