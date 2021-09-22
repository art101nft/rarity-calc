class Category:
    '''Contain info on category including counts and stuff'''
    def __init__(self, name):
        self.name = name
        self.traits = []
        self.trait_count = {}
        self.trait_freq = {}
        self.trait_rarity = {}
        self.trait_rarity_normed = {}
