def total_cost(budget, days):
    return budget * days

def get_valid_num(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except  ValueError:
            print("Invalid input! Please enter a valid integer.")

def plan(name, destination, budget, days):
    '''Format and display the user's name'''
    message = f"Hello, {name.title()}!"
    print(message)

    '''Confirm the destination
    '''
    if destination=='mountain':
        print('you elected Mountain')
    elif destination=='beach':
        print('you elected Beach')
    else:
        print('you elected another place')    
    '''Evaluate budget'''
    if budget >= 500:
        print("your budget >=500 so Luxury")
    elif budget >= 200:
        print('your budget is Good')
    else:
        print('Not enough! Minimum budget is 200.')

    '''Display total cost'''
    total_cost_value = total_cost(budget, days)
    print(f"Total cost for {days} days is: {total_cost_value}")

'''Get user inputs in the specified order'''
name = input("Enter your name: ")
print('choice mountain or beach')
destination = input('Where do you want to go:- ').strip().lower()

budget = get_valid_num('Enter your budget: ')
days = get_valid_num("Enter the number of days: ")

'''Call the travel planner function'''
plan(name, destination, budget, days)