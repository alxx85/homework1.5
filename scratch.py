class animals:
    feed = 0

    def __init__(self, name, types, weight, vote):
        self.name = name
        self.types = types
        self.weight = weight
        self.vote = vote

    def feeds(self):
        if self.feed == 0:
            self.feed = 1
            print('{} {}, накормлено'.format(self.types, self.name))
        else:
            print('{} {}, не хочет есть!'.format(self.types, self.name))

    def voice(self):
        return print('{} {}, говорит {}'.format(self.types, self.name, self.vote))

class horned(animals):
    def collections(self):
        print('{} {}, подоенна!'.format(self.types, self.name))

class fur(animals):
    def collections(self):
        print('{} {}, подстриженна...'.format(self.types, self.name))

class feathered(animals):
    def collections(self):
        print('У {} {}, яйца собраны...'.format(self.types, self.name))

all_weight = 0
max_weight = 0
max_weight_name = ''

animals_list = []

animal_0 = horned('Манька', 'Корова', 2100, 'Му')
animal_1 = feathered('Серый', 'Гусь', 4, 'Га')
animal_2 = feathered('Белый', 'Гусь', 3, 'Га')
animal_3 = fur('Барашек', 'Овца', 92, 'Ме')
animal_4 = fur('Кудрявый', 'Овца', 97, 'Ме')
animal_5 = feathered('Ко-ко', 'Курица', 1, 'Ко')
animal_6 = feathered('Кукареку', 'Курица', 2, 'Ко')
animal_7 = horned('Рога', 'Коза', 170, 'Бе')
animal_8 = horned('Копыта', 'Коза', 135, 'Бе')
animal_9 = feathered('Кряква', 'Утка', 3, 'Кря')
animals_list = [animal_0, animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9]

for animal in animals_list:
    animal.feeds()
    animal.collections()
    all_weight += animal.weight
    if max_weight < animal.weight:
        max_weight = animal.weight
        max_weight_name = animal.name

print(all_weight, max_weight_name)