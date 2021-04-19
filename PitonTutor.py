import os

class Budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float(input("How Much is your Budget?\n"))
        self.spending = self.budget * 0.5
        self.main()



    def main(self):
        os.system('cls')
        print("This Calculator follows the 50-20-30 budget rule. \n") 
        main_option = int(input('what do you want to do?\n1) View overall budget\n2) View spending budget\n'))
        if main_option == 1:
             self.overall_budget()
        elif main_option == 2:
             self.spending_budget()
        else:
            quit


    def overall_budget(self):
        os.system('cls')
        option = int(input('How much do you want to save?\n1) 20%\n2) 30%\n'))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print("error. Please select 1 or 2!")
        self.final_saving = self.budget * self.saving
        self.extra = self.budget -self.final_saving - self.spending
        print('\nSpending: $',self.spending,'\nTo Save: $', self.final_saving,'\nExtra: $', self.extra)
        os.system('pause')

    def spending_budget(self):
        os.system('cls')
        print('spending Budget: $',self.spending)
        rent = float(input('\nhow much rent do you pay in one month?\n'))
        bills = float(input('\nHow much are your monthly bills?\n'))
        groceries = self.spending - rent - bills
        print('\nEXPENSES:\nRent: $',rent,'\nBills: $', bills, '\nGroceries: $', groceries)
        os.system('pause')
        self.main()
Budget()