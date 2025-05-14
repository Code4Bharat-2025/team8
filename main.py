# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime
import requests
import json
import sys



languages = {'English':'en' , 'Arabic':'ar','Spanish':'es','Chinese':'zh' }
types = ['events','births','deaths','holidays','selected']
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# tp = ''
# language = ''
token= ''
user= ''
#dt =''


def getLanguageButtons:
	buttons = []
        for i,j in languages.items():
		button = {
                    "type": "solid",
                    "body": i,
                    "reply": i
                }
		buttons.append(button)
	return buttons

def getEventTypes:
	events = []
	buttons = []
        for i in types:
		button = {
                    "type": "solid",
                    "body": i,
                    "reply": i
                }
		buttons.append(button)
	return buttons

def getMonthsButtons:
	buttons = []
        for i,j in months.items():
		button = {
                    "type": "solid",
                    "body": i,
                    "reply": i
                }
		buttons.append(button)
	return buttons





def validate_date(date_string, date_format="%m/%d"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False




def getHistoricaldata(language,tp,dt):


    url = 'https://api.wikimedia.org/feed/v1/wikipedia/'+language+'/onthisday/'+ tp +'/' + dt
    #print(url)

    headers = {
      'Authorization': token,
      'User-Agent': user
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    for key,value in data.items():
        for index, item in enumerate(value):
            print( f" {item['text']}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(True):
        print('Choose language')
        for i,j in languages.items():
            print(i)

        io = input("Language pls: ")
        print('What are you interested in: ')
        language = languages[io]
        for i in types:
            print (i)

        tp = input("Enter type: ")
        print("What date are you interested in : ")
        mnth = input("Month : ")
        month = months[mnth]
        date = input(" date : ")
        dt = str(month)+'/'+str(date)
        if validate_date(dt) != True:
            print("Invalid date :" + str(date) + "/" + mnth)
        else:
            getHistoricaldata(language,tp,dt)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
