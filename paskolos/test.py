import csv


class Loan:
    loans_list = []

    def get_full_info(self):
        return (self.amount * (self.interest / 100)), ((self.amount * (self.interest / 100)) + self.amount)

    def get_loan_info(self):
        return [self.amount, self.period, self.interest]

    def all_loans(self):
        for idx, loan in enumerate(self.loans_list):
            print(f"{idx}: {loan}")

    def get_last_loan(self):
        print(self.loans_list[-1])

    def get_loan_graph(self):
        print(f"Men nr. / Grazintina dalis / Likutis / Priskaiciotos Palukanos / Bendra moketina suma")
        return_part = self.amount / self.period
        left_to_return = self.amount
        for idx in range(1, self.period + 1):
            interest_part = (left_to_return * (self.interest / 100) / self.period)
            all_amount = return_part + interest_part
            left_to_return -= return_part
            print(f"{idx}  /"
                  f" {round(return_part, 2)} /"
                  f" {abs(round(left_to_return, 2))} /"
                  f" {round(interest_part, 2)} /"
                  f" {round(all_amount, 2)}")
        print(f"Total / {self.amount} /"
              f" 0  /"
              f" {self.amount * (self.interest / 100)}  /"
              f" {((self.amount * (self.interest / 100)) + self.amount)}")

    def get_data(self):
        return_part = self.amount / self.period
        left_to_return = self.amount
        for idx in range(1, self.period + 1):
            interest_part = (left_to_return * (self.interest / 100) / self.period)
            all_amount = return_part + interest_part
            left_to_return -= return_part
            self.loan_data.append([idx,
                                   round(return_part, 2),
                                   abs(round(left_to_return, 2)),
                                   round(interest_part, 2),
                                   round(all_amount, 2)
                                   ])
        self.loan_data.append(["Total",
                               self.amount,
                               "0",
                               self.amount * (self.interest / 100),
                               ((self.amount * (self.interest / 100)) + self.amount)
                               ])
        return self.loan_data

    def to_csv(self):
        with open(f"Loan_{self.amount}_{self.period}_{self.interest}%.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Men nr.",
                                 "Grazintina dalis",
                                 "Likutis",
                                 "Priskaiciotos palukanos",
                                 "Bendra moketina suma"])
            for row in self.get_data():
                csv_writer.writerow([row[0], row[1], row[2], row[3], row[4]])


class Customer(Loan):
    def __init__(self, amount, period, interest):
        self.amount = amount
        self.period = period
        self.interest = interest
        self.loans_list.append([self.amount, self.period, self.interest])
        self.loan_data = []

# paskola1 = Loan(1000, 5, 15)
# paskola2 = Loan(2000, 12, 5)
# paskola3 = Loan(500, 3, 9)
#
# paskola3.all_loans()
# paskola2.get_loan_graph()


loan_list = []

while True:
    number = 0
    choose = int(input("Choose meniu: \n\r"
                       " 1.Create New Loan \n\r"
                       " 2.Show all loans \n\r"
                       " 3.Get Last loan info \n\r"
                       " 4.Exit"))
    if choose == 1:
        amount = int(input("Enter amount"))
        period = int(input("Enter loan period"))
        interest = float(input("Enter loan interest"))
        number += 1
        loan + str(number) = Loan(amount, period, interest)

    if choose == 2:
        Loan.all_loans()

    if choose == 3:
        Loan.get_last_loan()

    if choose == 4:
        break


