Loan Management Service
Requirements
Python 3.6.8
Django==3.2.11
django-extensions==3.1.0
celery==5.1.2
redis==4.3.6
ipython==7.13.0
requests==2.27.1
pytest==7.0.1
Steps to Run
Clone the GitHub repo:

bash
Copy code
git clone
Change directory into the Branch-International folder:

bash
Copy code
cd bright-money/lone_ease
Run migrations:

bash
Copy code
python manage.py migrate
Run the server:

bash
Copy code
python manage.py runserver
To run tests corresponding to the API's:

bash
Copy code
python manage.py test
Entities
UserInformation

name: "John Doe"
email: "johndoe@example.com"
annual_income: 500000
aadhar_id: 123456789012
credit_score: 750
user_uuid: "c9577b41-daaf-4276-9403-ba825fd1058c"
UserTransactionInformation

aadhar_id: 123456789012
registration_date: "2023-01-01"
amount: 10000
transaction_type: "CREDIT"
credit_score: 750
LoanInfo

loan_id: "398ed9c2-287d-4bd7-b753-f26526d30ed9"
user_uuid: "c9577b41-daaf-4276-9403-ba825fd1058c"
loan_type: "CAR"
loan_amount: 500000
annual_interest_rate: 12
term_period: 12
disbursement_date: "2023-07-01"
EMIDetails

loan_id: "398ed9c2-287d-4bd7-b753-f26526d30ed9"
amount_due: 45000.0
amount_paid: 0.0
installment_date: "2023-08-01"
API Details
register_user

URL: http://127.0.0.1:8000/register_user/
Type: POST
Request Body:
json
Copy code
{
  "aadhar_id": 123456789012,
  "name": "John Doe",
  "email_id": "johndoe@example.com",
  "annual_income": 500000
}
Response:
json
Copy code
{
  "message": "user successfully registered",
  "data": {
    "user_uuid": "c9577b41-daaf-4276-9403-ba825fd1058c"
  },
  "success": "True"
}
apply_loan

URL: http://127.0.0.1:8000/apply_loan/
Type: POST
Request Body:
json
Copy code
{
  "user_uuid": "c9577b41-daaf-4276-9403-ba825fd1058c",
  "loan_type": "CAR",
  "loan_amount": 500000,
  "interest_rate": 12,
  "term_period": 12,
  "disbursement_date": "2023-07-01"
}
Response:
json
Copy code
{
  "message": "loan applied successfully",
  "data": {
    "EMI_details": [
      {
        "amount_due": 45000.0,
        "amount_paid": 0.0,
        "installment_date": "2023-08-01"
      },
      {
        "amount_due": 45000.0,
        "amount_paid": 0.0,
        "installment_date": "2023-09-01"
      },
      {
        "amount_due": 45000.0,
        "amount_paid": 0.0,
        "installment_date": "2023-10-01"
      }
    ],
    "loan_id": "398ed9c2-287d-4bd7-b753-f26526d30ed9"
  },
  "success": "True"
}
make_payment

URL: http://127.0.0.1:8000/make_payment/
Type: POST
Request Body:
json
Copy code
{
  "loan_id": "398ed9c2-287d-4bd7-b753-f26526d30ed9",
  "amount": 45000
}
Response:
json
Copy code
{
  "message": "EMI paid successfully for this month",
  "data": {
    "emi_due": 45000.0,
    "emi_paid": 45000.0,
    "installment_paid": "2023-08-01"
  },
  "success": "True"
}
get_statement

URL: http://127.0.0.1:8000/get_statement/?loan_id=398ed9c2-287d-4bd7-b753-f26526d30ed9
Type: GET
Request Params:
json
Copy code
{
  "loan_id": "398ed9c2-287d-4bd7-b753-f26526d30ed9"
}
Response:
json
Copy code
{
  "message": "success",
  "data": {
    "upcoming_transactions": [
      {
        "amount_due": 45000.0,
        "installment_date": "2023-09-01"
      }
    ],
    "past_transactions": [
      {
        "amount_paid": 45000.0,
        "installment_date": "2023-08-01"
      }
    ]
  },
  "success": "True"
}
EMI Calculations
EMI is calculated by the given formula:

plaintext
Copy code
EMI = P × [R × (1 + R)^n] / [(1 + R)^n - 1]
Where:

P = Principal loan amount
R = Periodic interest rate (annual interest rate in decimal / 12)
n = Repayment tenure in months
