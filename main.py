from random import randint

class sum_and_square():
    
    def main(self):
        number_list_number = self.random_number()
        square_list_number = self.square_list(number_list_number)
        print(f'The sum of the four random numbers in the square is {self.sum_number(square_list_number)}')
    
    def random_number(self):
        number_list = []
        for number in range(4):
            the_number = randint(1, 10)
            number_list.append(the_number)
            print(f'From Number {number + 1} we have {the_number}')
        
        return number_list
    
    def square_list(self, number_list):
        square_list = []
        for number in number_list:
            square_list.append(number*number)
            print(f'The square of {number} is {number*number}')
        print()
        return square_list

    def sum_number(self, the_list):
        total_sum = 0
        for total in the_list:
            total_sum += total
        return total_sum

if __name__ == '__main__':
    run = sum_and_square()
    run.main()