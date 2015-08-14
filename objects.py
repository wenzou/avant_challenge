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


class CreditLine:
    'A line of credit product.  This is like a credit card except theres no card.'
    def __init__(self, apr=5.0, credit_limit=1000):
        self.payments_due = 0
        self.apr = apr
        self.credit_limit = credit_limit
        #starts at day 0, which is in human terms day 1.
        self.days = 0
        self.interest_charge = 0

    def calculate_interest(self, days_of_interest):
        return self.payments_due * self.apr / 100 / 365 * days_of_interest

    def advance_days(self, days_to_advance):
        if days_to_advance < 0:
            return False
        #since this is a fictional product, we have a helper to advance the days.
        #if the total days end up to be more than 30 days.
        total_days = self.days + days_to_advance
        days_over_30_days = total_days - 30
        if days_over_30_days >= 0:
            times_of_30, remainder_days = divmod(days_over_30_days, 30)
            #charge the interest
            self.payments_due +=self.calculate_interest((30-self.days))
            #for all other 30s, charge and increase payments due
            for i in range(0 ,times_of_30):
                self.payments_due +=self.calculate_interest(30)

            self.payments_due += self.interest_charge
            self.interest_charge += self.calculate_interest(remainder_days)
            #reset the days to be out of 30 days
            self.days = remainder_days


        else:
            #if is it not over 30 days, simply charge the interest
            self.interest_charge += self.calculate_interest(days_to_advance)
            self.days += days_to_advance

        return self.days

    def get_balance(self):
        #this get the principle balance rounded to the nearest 2 decimal places
        return round(self.payments_due, 2)

    def make_payment(self, payment_amount):
        #paydown your balance
        self.payments_due = self.payments_due - payment_amount
        return self.payments_due

    def draw_credit(self, draw_amount):
        #attempts to the draw money against the line of credit
        total = self.payments_due + draw_amount
        if self.credit_limit < total:
            return False
        self.payments_due = total
        return self.payments_due