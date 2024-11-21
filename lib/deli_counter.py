katz_deli = []

def line(deli):
    if len(deli) == 0:
        print('The line is currently empty.')
    else:
        cust_list = []
        for i in range(len(deli)):
            cust_list.append(f"{i+1}. {deli[i] }")
        print(f"The line is currently: {' '.join(cust_list)}")


def take_a_number(deli, customer):
    deli.append(customer)
    print(f"Welcome, {customer}. You are number {len(deli)} in line.")

def now_serving(deli):
    if len(deli) == 0:
        print('There is nobody waiting to be served!')
    else:
        print(f"Currently serving {deli[0]}.")
        deli.pop(0)


