'''
This is code to track personal spending
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd

class finances(object):

    def __init__(self,month,year):
        self.month = month
        self.year = year
        self.purchases = None
        self.income = None
        self.data = pd.read_csv('finances.csv')

    def income_and_purchases(self):
        self.income_data = self.data[self.data.In_or_Out == "In"]
        self.purchase_data = self.data[self.data.In_or_Out == "Out"]

        self.income = dict(self.income_data.groupby('Category')['Amount'].apply(list))

        self.purchases = dict(self.purchase_data.groupby('Category')['Amount'].apply(list))

    def totals(self):
        self.sum_purchases_cat = {k: sum(v) for (k,v) in self.purchases.items()}

        self.sum_income_cat = {k: sum(v) for (k,v) in self.income.items()}

        print()
        print('Purchases by Category: ')
        print(self.sum_purchases_cat)
        print()
        print('Income by Category: ')
        print(self.sum_income_cat)

        self.sum_purchases ={'Purchases': sum(self.sum_purchases_cat.values())}

        self.sum_income ={'Income': sum(self.sum_income_cat.values())}

        print()
        print(self.sum_income)
        print(self.sum_purchases)

    def net_income(self):
        self.net_income = {'Net Income':self.sum_income['Income']-self.sum_purchases['Purchases']}
        print()
        print(self.net_income)


if __name__ == '__main__':
    balance = finances('Feb',2018)
    balance.income_and_purchases()
    balance.totals()
    balance.net_income()
