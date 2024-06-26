class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.new_country = [name, population]


    def __add__(self, other_country):
        new_name = self.name + ' - ' + other_country.name
        new_population = self.population + other_country.population
        new_country = Country(new_name, new_population)
        return new_country


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)