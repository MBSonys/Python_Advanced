from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker
from table import Loans, engine
from loan import Loan
import pandas as pd
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
import base64
from mail import sending_email
from logger import logger

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
sns.set_style("dark")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
            period = int(request.form['period'])
            interest = float(request.form['interest'])
            email_to_send = request.form['email_send']
            loan = Loan(amount, period, interest)
            loan_db = Loans(amount, period, interest)
            show_loan = loan.get_loan_info()
            session.add(loan_db)
            session.commit()
            loan.to_csv()
            loan_table = loan.get_data()
            indexing = [x for x in range(len(loan_table))]
            table = pd.DataFrame(loan_table, indexing, ["Men nr.",
                                                        "Grazintina dalis",
                                                        "Likutis",
                                                        "Priskaiciotos Palukanos",
                                                        "Bendra moketina suma"
                                                        ])
            data_visual = sns.distplot(table['Priskaiciotos Palukanos'], kde=False, bins=20)
            img = BytesIO()
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            sending_email(email_to_send, show_loan, loan_table)
            logger.info(f"New loan added {amount} - {period} - {interest}")
            return render_template("loan.html",
                                    show_seaborn=data_visual,
                                    loan_to_show=show_loan,
                                    tables=[table.to_html(classes='data', header="true", index=False)],
                                    plot_url=plot_url
                                    )

        except BaseException as ex:
            print(ex)
            return "Ivyko klaida, bandykite dar karta <h1></h1>"
    return render_template('base.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)