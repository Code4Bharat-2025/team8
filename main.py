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
token= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2Yjg5ZDQxYzI2YzM0NzM0M2Q3OGYyYjY3OGY3NDQwZCIsImp0aSI6Ijc2OTllMWU5MWU2Mjc4NTM3N2UxOTEwYzNhYWNmYjNmYmY4MTEzMDg4NjM2MTkwMjMyZmJlMzk5MTI0ZGE3ODA2OGVkM2JhZWZjM2Q1NjJlIiwiaWF0IjoxNzQ3MjAyODc0LjQ2NDM5MywibmJmIjoxNzQ3MjAyODc0LjQ2NDM5NCwiZXhwIjozMzMwNDExMTY3NC40NjIxNiwic3ViIjoiNzgzMDc2MDgiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsInJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIl19.gjoQKwkkQJz-QNTT29vDpzkpgZCtdp4BAOYwABRodHUMuQjAUexRCD-bYTfrx3lE3n1c1uHnmbfh76p0M_o-vhhVN2VSnHQbn0rx-WAdtimhUxNhhuiKpHcMyTjfHyiozME3Yp4Hd-q9XO29ayWdIgDrRXO_7nZOZTaZk9rNEoQ7fL5sUZc2VjYd_RKxzdFRCPtOC6uXTf7OzP0GEAGrnsBZt3eORQZ7-MpwZsjCKCWHqRwLIwq9esopWof0KQ_m_4zifNOOAHIkOKKJN9BaQE7T4LPTYpi8yC8uMvkYivYwzogxBW7Kwi34vETNcIEZ36V5o5AZW_nA5tEQhYy126z9AirCC4F6S9G6ZEuyZM0RfFwZaDRXBseLyq_EG229wGw0W1GY13C-1IcBy2ABs0pxmymCPhyNlzMplAdwaJV0WGxX19GUPTkxmgWdqatLU15TQpn1lqvXR990WgiPeKsZO2t7r1ErGXtYRVjs71yDSzb1kEIUuQdcouuM6_j8fIkxWigGgS5BJjcDy8-wgkefdZ3GuE1PmYRQadbTikiCr1MKJmAFt2EqLN-sjcd9xvwUEd9G_CKM2fWTLpYmOi5A3qNCTumK7p_Fco9sta2c_hKVHhogazPaVX5VpU-R4zgT7IT5v1ubjGEN7qwGq3wmreZseEKpmnbAUAkITgE'
user= 'HackathonX'
#dt =''







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
