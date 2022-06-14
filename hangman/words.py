import random


class Words():

    def __init__(self):

        self.titles = ['animals', 'birds', 'superheroes',]

        self.animals = [
            'aligator',
            'gazelle',
            'crocodile',
            'elephant',
            'reindeer',
            'leopard',
            'jaguar',
            'cheetah',
            'anaconda',
            'rhinoceros'
        ]

        self.birds = [
            'falcon',
            'vulture',
            'peacock',
            'ostrich',
            'parrot',
            'mynah',
            'eagle',
            'sparrow',
            'pigeon',
            'raven'
        ]

        self.superheroes = [
            'super man',
            'spider man',
            'captain america',
            'bat man',
            'wolverine',
            'wonder woman',
            'iron man',
            'aqua man',
            'black widow',
            'doctor strange'
        ]

        self.flowers = [
            'marigold',
            'daffodil',
            'daisy',
            'orchid',
            'hibiscus',
            'morning glory',
            'chrysanthemum',
            'tulip',
            'sun flower',
            'dandelion'
        ]

        self.cities = [
            'copenhagen',
            'amsterdam',
            'stockholm',
            'singapore',
            'shanghai',
            'saint petersburg',
            'belgrade',
            'budapest',
            'vancouver',
            'brisbane'
        ]

        self.category_list = [
            'animals',
            'birds',
            'superheroes',
            'flowers',
            'cities'
        ]

    def randomise(self, num):
        rand_num = random.randint(0, num)
        return rand_num
    
    def get_type(self):
        num = self.randomise(len(self.category_list)-1)

        if num == 0:
            self.category = (self.category_list[num])
            return self.animals
        
        if num == 1:
            self.category = (self.category_list[num])
            return self.birds

        if num == 2:
            self.category = (self.category_list[num])
            return self.superheroes

        if num == 3:
            self.category = (self.category_list[num])
            return self.flowers

        if num == 4:
            self.category = (self.category_list[num])
            return self.cities

    def get_word(self):
        self.selected_category = self.get_type()
        num = self.randomise(len(self.selected_category)-1)
        return(self.selected_category[num])
