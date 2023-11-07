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


from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess= input("Pick a number:0,1 or 2")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct")
    else:
        print("Wrong guess")
        print(mylist)
mylist =['','O','']
mixedup_list=shuffle_list(mylist)
guess=player_guess()
check_guess(mixedup_list,guess)


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc(10,20,30,fruit='orange',food='eggs',animal='cat')