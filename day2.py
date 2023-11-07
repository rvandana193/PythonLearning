def check_even_list(num_list):
    for number in num_list:
        if number%2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1,3,5]))
print(check_even_list([1,3,2,5]))


work_hours=[('Sam',100),('John',200),('Tom',300)]
def emp_check(work_hours):
    current_max=0
    emp_of_month =''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max = hours
            emp_of_month = employee
        else:
            pass
    return(emp_of_month,current_max)
print(emp_check(work_hours))