__author__ = 'wenzou'


class FactorManager:
    'returns factors of integers'
    def __init__(self):
        pass

    def return_factor(self, list=[]):
        #for each integer in the list
        #check for its factor
        return_dict = {}
        for integer in list:
            #compare with the rest of the list
            my_factors = []
            for integer_to_comp in list:
                if integer == integer_to_comp:
                    continue
                if integer % integer_to_comp == 0:
                    my_factors.append(integer_to_comp)

            return_dict[integer] = my_factors

        return return_dict
