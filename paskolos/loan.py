import csv
from sqlalchemy.orm import sessionmaker
from table import Loans, engine

Session = sessionmaker(bind=engine)
session = Session()


class Loan:
    def __init__(self, amount, period, interest):
        self.amount = amount
        self.period = period
        self.interest = interest

    def __str__(self):
        return f"{self.amount} {self.period} {self.interest}"

    def get_full_info(self):
        return (self.amount * (self.interest / 100)), ((self.amount * (self.interest / 100)) + self.amount)

    def get_loan_info(self):
        return [self.amount, self.period, self.interest]

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
        self.loan_data = []
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

# while True:
#     choose = int(input("Choose meniu: \n\r"
#                        " 1.Create New Loan \n\r"
#                        " 2.Show all loans \n\r"
#                        " 3.Show loan graph \n\r"
#                        " 4.Get full loan info \n\r"
#                        " 5.Modify loan \n\r"
#                        " 6.Exit "
#                        ))
#     if choose == 1:
#         amount = int(input("Enter amount"))
#         period = int(input("Enter loan period"))
#         interest = float(input("Enter loan interest"))
#         loan = Loan(amount, period, interest)
#         loan_db = Loans(amount, period, interest)
#         session.add(loan_db)
#         session.commit()
#         loan.to_csv()
#
#     elif choose == 2:
#         all_loans = session.query(Loans).all()
#         for loan in all_loans:
#             print(loan)
#
#     elif choose == 3:
#         all_loans = session.query(Loans).all()
#         for loan in all_loans:
#             print(loan)
#         choose = int(input("Choose loan:"))
#         get_loan = session.query(Loans).get(choose)
#         init_loan = Loan(get_loan.amount, get_loan.period, get_loan.interest)
#         init_loan.get_loan_graph()
#
#     elif choose == 4:
#         all_loans = session.query(Loans).all()
#         for loan in all_loans:
#             print(loan)
#         choose = int(input("Choose loan:"))
#         get_loan = session.query(Loans).get(choose)
#         init_loan = Loan(get_loan.amount, get_loan.period, get_loan.interest)
#         print(init_loan.get_full_info())
#
#     elif choose == 5:
#         all_loans = session.query(Loans).all()
#         for loan in all_loans:
#             print(loan)
#         choose = int(input("Choose loan:"))
#         get_loan = session.query(Loans).get(choose)
#         get_loan.amount = int(input("Enter loan amount: "))
#         get_loan.period = int(input("Enter loan period: "))
#         get_loan.interest = float(input("Enter loan interest: "))
#
#     elif choose == 6:
#         break
#
#     else:
#         print("Wrong input, try again")


