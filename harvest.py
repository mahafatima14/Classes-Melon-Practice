############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    #(self, code, first_harvest, color, is_seedless, is_bestseller, name)
    musk = MelonType("musk",1998,"green",True,True,"Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas",2003,"orange",False,False,"Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren",1996,"green",False,False,"Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw",2013,"yellow",False,True,"Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f'{melon_type.name} pairs with')
        for pairing in melon_type.pairings:
            print(f'-{pairing}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_lookup = {}
    
    for melon_type in melon_types:
        melon_lookup[melon_type.code] = melon_types
    
    return melon_lookup

#melon_types = make_melon_types()
#print_pairing_info(melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
        
    
    def is_sellable(self):

        if self.shape_rating>5 and self.color_rating>5 and self.field!=3:
            return True

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_types = make_melon_types()
    melons_by_id = make_melon_type_lookup(melon_types)

    list_of_melons = []

    #parameters for init: self, melon_type, shape_rating, color_rating, field, harvested_by
    melon_1 = Melon(melons_by_id['yw'],8,7,2,'Sheila')
    list_of_melons.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'],3,4,2,'Sheila')
    list_of_melons.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'],9,8,3,'Sheila')
    list_of_melons.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'],10,6,35,'Sheila')
    list_of_melons.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'],8,9,35,'Michael')
    list_of_melons.append(melon_5)
    
    melon_6 = Melon(melons_by_id['cren'],8,2,35,'Micheal')
    list_of_melons.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'],2,3,4,'Michael')
    list_of_melons.append(melon_7)
   
    melon_8 = Melon(melons_by_id['musk'],6,7,4,'Micheal')
    list_of_melons.append(melon_8)
    
    melon_9 = Melon(melons_by_id['yw'],7,10,3,'Sheila')
    list_of_melons.append(melon_9)

    
    return list_of_melons


#melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            print(f"Harvested by: {melon.harvested_by} from Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by: {melon.harvested_by} from Field {melon.field} (NOT SELLABLE)")
