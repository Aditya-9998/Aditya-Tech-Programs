if __name__ == '__main__':
    n = int(input('Enter no:- ').strip())
    if n % 2 == 0 and n in range(6):
        print('Not Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
    else:
        print('Weird')