# Learning to build functions with outputs
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"


print(my_function(25))


def format_name(first_name, last_name):
    """Take a first and last name and
     output a result of the name as Lowercase"""
    if first_name == "" or last_name == "":
        return "You did not provide valid input"
    f_name = first_name.title()
    l_name = last_name.title()

    return f" Results :{f_name}  {l_name}"


print(format_name(input("What is your first name?"),
                  input("What is your last name?")))


# Days in months
def is_leap(m_year):
    if m_year % 4 == 0:
        if m_year % 100 == 0:
            if m_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(i_year, i_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if i_month == 2 and is_leap(i_year):
        return 29
    else:
        return month_days[i_month - 1]


year = int(input("Please enter a year"))
month = int(input("Please enter a month"))
days = days_in_month(year, month)
print(days)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)
