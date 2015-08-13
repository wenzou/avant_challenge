__author__ = 'wenzou'


class FactorManager:
    'returns factors of integers'
    def __init__(self, cache=False):
        self.cache = cache
        self.cache_dict = {}

    def return_factor(self, list=[]):
        #for each integer in the list
        #check for its factor
        return_dict = {}
        key = frozenset(list)
        if self.cache and key in self.cache_dict:
            #check cache
            return self.cache_dict[key]


        for integer in list:
            #compare with the rest of the list
            my_factors = []
            for integer_to_comp in list:
                if integer == integer_to_comp:
                    continue
                if integer % integer_to_comp == 0:
                    my_factors.append(integer_to_comp)

            return_dict[integer] = my_factors
        self.cache_dict[key] = return_dict
        return return_dict

