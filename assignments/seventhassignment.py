details = []
def add():
    global details
    n=int(input('Enter number of employees: '))
    for i in range(1,n+1):
        d={}
        print(f'enter details of the employee-{i}')
        d['Name']=input('Enter name of employee: ')
        d['Ep id']=input('Enter employment id:')
        d['Domain']=input('Enter domain : ')
        d['Email id']=input('Enter email : ')
        details.append(d)
        print()
    print()
    condition()

def remove():
    global details
    n=input('to remove an employee type a , to remove attribute of element type b, to delete entire employe details type c: ')
    if n=='a':
        ch=input('enter an attribute of emplpoyee to reomove: ')
        for i in details:
            if ch == i.get('Name') or (ch == i.get('Ep id') or (ch == i.get('Domain') or ch == i.get('Email id'))) :
                details.remove(i)
                break
        else :
            print('employee with given attribute not found: ')
        print()
        condition()        
    elif n=='b':
        ch=input('Enter an element which that element to be reomved from that employee details')

        for i in range(len(details)):
            if ch == details[i].get('Name') :
                details[i].pop('Name')
                break
            elif ch == details[i].get('Ep id'):
                details[i].pop('Ep id')
                break
            elif ch == details[i].get('Domain'):
                details[i].pop('Domain')
                break
            elif ch == details[i].get('Email id'):
                details[i].pop('Email id')
                break
        else :
            print('employee with given attribute not found: ')
        print()
        condition()
    elif n== 'c':
        details.clear() 
        print()
        condition()

def p():
    global details
    n=input('to print an employee type a , to print detalis of all the employees type b: ')
    if n=='a':
        ch=input('enter an attribute of emplpoyee to print employe details: ')
        for i in details:
            if ch == i.get('Name') or (ch == i.get('Emp id') or (ch == i.get('Domain') or ch == i.get('Email'))) :
                print(i)
        else :
            print('employee with given attribute not found: ')
        print()
        condition()        
    elif n=='b':
        print(details)
        print()
        condition()

def condition():
    n=input('to add type v, to remove type k, to print type y : ')
    if n=='v':
        add()
    elif n=='k':
        remove()
    elif n=='y':
        p()

condition()
    




