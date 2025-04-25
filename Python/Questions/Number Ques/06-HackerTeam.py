def timeConversion(s):
    period = s[-2:]
    time_str = s[:-2]
    hours, minutes, seconds = time_str.split(':')
    hours = int(hours)
    
    if period == 'AM':
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12
    
    return f'{hours:02}:{minutes}:{seconds}'

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)


#