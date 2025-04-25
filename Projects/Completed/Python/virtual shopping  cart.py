def getValidQuantity():
    
    pass


def calculateTotal():
    pass

def applyDiscount():
    pass


def checkout():
    pass
def main():
    print('main')

if __name__=='__main__':
    main()

prices={'Apple':10,'Mango':15,'Orango':10,'jack fruit':40}
cart={'Apple':200,'Mango':100,'Orange':60}

items= ['Apple','Mango','Orange','jack fruit']

for item in items:
    print(item)

choice=input("selected an item :- ")
print(choice)

if choice in items:
    quantity=int(input("enter quantity :> "))
    # something here missing
    print(f'{choice} is added to cart',quantity)
    print("check")# also here
else:
    print(f'{choice} is not available')

'''   
Failed to resolve env "C:\\Users\\Aditya Kumar\\Program\\Projects\\Password_Checker\\venv\\Scripts\\python.exe"
'''
