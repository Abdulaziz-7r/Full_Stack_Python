import datetime

def birthdayCalculator(name_and_date):
    oldest, youngest = [0,''], [10000,'']
    for  row in name_and_date:
        name,date = row.split(',')
        date = date.split('-')
        try:
            date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
        except ValueError:
            print(f"Invalid date for {name}")
            break
        age = datetime.datetime.today().year - date.year
        print(f'{name} is {age} years old and she/he was born on {(date.strftime("%A"))}')
        if len(name_and_date) <= 1:
            continue
        if oldest[0] < age:
            oldest[0], oldest[1] = age, name
        elif youngest[0] > age:
            youngest[0], youngest[1] = age, name
    

    if len(name_and_date) <= 1:
        print("There is no oldest or youngest person")
    else:    
        print(f'The oldest one is {oldest[1]}')
        if youngest[1] != "":
            print(f'The youngest one is {youngest[1]}')

    print(f"Total People: {len(name_and_date)}")



def main():
    name_and_date =[]
    print("Enter name and day of birth as \"name, dd-mm-yyyy\" and done if you finished: ")
    while(True):
        name_date = input()
        if(name_date.lower() == 'done'):
            break
        name_and_date.append(name_date)
    
    birthdayCalculator(name_and_date)

if __name__ == "__main__":
    main()
