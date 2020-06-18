class Property:
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths


    def display(self):
        print("PROERTY DETAILS")
        print('===============')
        print(self.square_feet)
        print(self.num_bedrooms)
        print(self.num_baths)
        print()

    def prompt_init():
        return dict(square_feet=input('enter square'),beds=input('enter bed'),baths=input("enter baths"))
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string,valid_options):
    input_string += '({})'.format(','.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    valid_laundries = ('coin','ensuite','none')
    valid_balconies = ('yes','no','solarium')

    def __init__(self,balcony='',laundry='',**kwargs):
        super.__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('APARTMENT DETAILS')
        print(self.laundry)
        print(self.balcony)

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input('what laundry facilities does the property have? ({})'.format(','.join(Apartment.valid_laundries)))
        balcony = get_valid_input('Does the property have a balcony? ({})'.format(','.join(Apartment.valid_balconies)))
        parent_init.update(
            {
                'laundry':laundry,
                'balcony':balcony
            }
        )
        return parent_init


class House(Property):
    valid_garage = ('attached','detached','none')
    valid_fenced = ('yes','no')

    def __init__(self,num_stories='',garage='',fenced='',**kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print('HOUSE DETALLS')
        print('# of stories: {}'.format(self.num_stories))
        print('garage:{}'.format(self.garage))
        print('fenced yard: {}'.format(self.fenced))

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input(
            'is the yard fenced?',House.valid_fenced)
        garage = get_valid_input('Is there a garage? ',House.valid_garage)
        num_stories = input('How many stories?')
        parent_init.update(
            {
                'fenced':fenced,
                'garage':garage,
                'num_stories':num_stories
            }
        )
        return parent_init

class Purchase:
    def __init__(self,price='',taxes='',**kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print('PURCHASE DETAILS')
        print('selling price: {}'.format(self.price))
        print('estimated taxes: {}'.format(self.taxes))

    @staticmethod
    def prompt_init():
        return dict(
            price = input('what is the selling price?'),
            taxed = input('What are the estimated taxes?')
        )

class Rental:
    def __init__(self,furnished='',utilities='',rent='',**kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print('RENTAL DETAILS')
        print('rent; {}'.format(self.rent))
        print('estimated utilities: {}'.format(self.utilities))
        print('furnished: {}'.format(self.furnished))

    @staticmethod
    def prompt_init():
        return dict(
            rent = input("What is the monthly rent?"),
            utilities = input('what are the estimated utilities?'),
            furnished = get_valid_input('Is the property furnished?',('yes','no'))
        )

class HouseRental(Rental,House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental,Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentPurchase(Purchase,Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class HousePurchase(Purchase,House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input('what type of property?',('house','apartment')).lower()
        payment_type=get_valid_input('what payment type?',('purchase','rental')).lower()

        PropertyClass = self.type_map[(property_type,payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))