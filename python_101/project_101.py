#importing modules
from tkinter import messagebox as mb

#directory that has all telephone numbers and their owners
telephone_directory =  {
'1111111111': 'Amal',
'2222222222': 'Mohammed',
'3333333333': 'Khadijah',
'4444444444': 'Abdullah',
'5555555555': 'Rawan',
'6666666666': 'Faisal',
'7777777777': 'Layla'
}

#function that searches for a telephone number owner's name from the directory
def find_owner(phone_number, telephone_directory):
    if (len(phone_number) == 10 and phone_number.isnumeric()):
        if phone_number in telephone_directory:
            print ('The owner is:', telephone_directory[phone_number])
        else:
            print('Sorry, the number is not found')
    else:
        print('This is invalid number')

def messagebox(continueRun):
    res=mb.askquestion('Search Again', 'Do you want to search again?')
    if res == 'yes' :
        return True
    else:
        mb.showinfo('Close', 'The app will be closed')
        return False 


continueRun = True 
while(continueRun):
    #asking the user to enter the telephone number
    find_owner(input('Enter telephone number to know the owner: '), telephone_directory)
    continueRun = messagebox(continueRun)