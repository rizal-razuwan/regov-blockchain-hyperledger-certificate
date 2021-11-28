"""[Question 1]

Evaluate your software practices, with a focus on 
    object oriented programming  
    
We have provided you with a stub class called Account that 
represents a bank account. Please fill out the stub functions,
then write a program that creates 3 unique instances of the class,
and store them in a data structure of your choice. Explain your thought 
process behind choosing a data structure.

"""

# Stack and Queqe data structure

from foryou.stack import Stack


class Account:
    def __init__(self, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def getNotes(value):
        """ determine the number of notes based on
        amount deposited, which start count from the 
        highest to the lowest [ 500 -> 10 ]"""

        x = 0  # number of notes based on amount

        for i in range(6):
            Q = []
            q = Q[i]
            x += int(value / q)
            value = int(value % q)

            if value > 0:
                x = -1
            else:
                return x

    def deposit(self, amount):
        notes = [500, 200, 100, 50, 20, 10]
        notes_list = []
        self.balance = + amount
        x = self.getNotes(amount)
        
        Stack.push(x)

        for notes in range(x):
            notes_list = notes.append(notes_list)

        return(self.balance)

    def withdraw(self, amount):
        if Stack.isEmpty:
            return print("your account balance is not sufficient")

        elif amount > Stack.size:
            return print("your transaction is error")

        else:
            Stack.pop(self.amount)

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"


# check account balance
def atm(value):
    if Account.name is None:
        return "Your are not authorised"
    else:
        print(Account.__str__)
