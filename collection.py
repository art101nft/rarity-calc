class Collection:
    '''Representation of an entire collection of items'''
    def __init__(self):
        self.traits = []                # List of tuples coupling (category, trait)
        self.item_count = 0             # Number of items in collection
        self.items = []                 # List of all item objects in collection
        self.trait_count = {}           # Mapping of number of traits to count
        self.categories = {}            # Dict of all categories in collection with counts and stuff

    def get_avg_trait_per_cat(self):
        '''Return the average number of traits per category'''
        traits_per_cat = []
        for c in self.categories.values():
            traits_per_cat.append(len(c.traits))
        return sum(traits_per_cat)/len(traits_per_cat)
