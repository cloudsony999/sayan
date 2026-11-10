# salary.py

def check_salary_eligibility(employee):

    name = employee["name"]

    if name == "Gayatri":

        if employee["effective_lines"] >= 175:
            return True
        else:
            return False

    elif name == "Sumanto":

        if employee["leaves"] < 3:
            return True
        else:
            return False

    return False


def process_salary(employee):

    eligible = check_salary_eligibility(employee)

    if eligible:

        print("Salary approved for", employee["name"])
        print("Salary Amount: Rs.", employee["salary"])

        return True

    else:

        print("Salary not approved for", employee["name"])

        return False