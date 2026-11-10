# main.py

from employee import employees
from salary import process_salary
from gmail_service import send_salary_email


def start_salary_processing():

    print("AI COMPANY - HR SALARY SYSTEM")
    print("-----------------------------")

    for employee in employees:

        print("\nProcessing:", employee["name"])

        salary_status = process_salary(employee)

        if salary_status:

            print("Preparing salary email...")

            email_status = send_salary_email(employee)

            if email_status:
                print("Salary notification completed.")
            else:
                print("Salary email could not be sent.")

        else:

            print("Salary conditions not satisfied.")
            print("No email will be sent.")


start_salary_processing()