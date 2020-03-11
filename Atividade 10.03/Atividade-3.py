# -*- coding: utf-8 -*-

#Name: Pastry POS
#Author: Victor Lopes
#Date: 2020/03/10 (ISO 8601)
#Description: This code simulate a POS (Point of sale) for a Pastry. Where you insert a amount of the sale and it sum every and print it with the total sales.

from random import randint

class pastry_pos():

    def main(self):
        initial_amount = 0
        self.sum(initial_amount)
        pass
    
    def sum(self, amount):
        print('Instuction:\n1 - This program dont check if you type e int value, then PLEASE type ONLY numbers\n2 - For exit the loop type 0')
        sales = 0
        actual_amount = amount 
        run_condition = True
        while run_condition:
            price = int(input('Value: '))
            if price == 0:
                break
            sales += 1
            actual_amount += price
        print(f'Finish, you did {sales} sales and you actual amount is {actual_amount}')
        pass

if __name__ == '__main__':
    run = pastry_pos()
    run.main()
