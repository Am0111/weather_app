import os

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
 
weather_data = { # the data that we will use
    "riyadh": {
        "date" : "22/03/2016",
        "temp" : 11,
        "humidity": 23.2,
        "weather condition" : "sunny"
    }
    ,
        "abha": {
        "date" : "22/03/2020",
        "temp" : 22,
        "humidity": 22.2,
        "weather condition" : "clouldy"
    }
}

def weather_query()-> str:
    city = input("please enter city name : ")
    if city in weather_data :
    
        print(f"the condition of {city} is {weather_data[city]["weather condition"]} and humidity = {weather_data[city]["humidity"]}")
    else :
        raise KeyError(f"the city named '{city}' not in our database ")


def add_data():

    city = input("Enter city ")
    date = input("Enter date ") # must be checked 
    temp = float(input("Enter temparture ")) # must be checked 
    humidity = float(input("Enter humidity ")) #must be checked 
    condition = input("Enter condition (sunny, rainny, cloudy) ")

    if condition in ["cloudy","rainny","sunny"]:
        weather_data[city] = {"date":date,"temp":temp,"humidity":humidity,"weather condition":condition}
        print(f"\033[32m weather data of {city} added successfully \033[36m ")
    else:
        raise Exception("Provide only supported weather condition (sunny, rainny, cloudy) ")

def update_data():

    city = input("Enter city ")

    if city in weather_data :
        
        date = input("Enter date ") # must be checked 
        temp = float(input("Enter temparture ")) # must be checked 
        humidity = float(input("Enter humidity ")) #must be checked 
        condition = input("Enter condition (sunny, rainny, cloudy) ")

        weather_data[city]["date"] = date
        weather_data[city]["temp"] = temp
        weather_data[city]["humidity"] = humidity
        weather_data[city]["weather condition"] = condition
        print(f"\033[32m weather data of {city} updated successfully \033[36m ")

    else:
        raise Exception("Provided city not in our database !")

def display_data():

    print(f'''\033[32m 
{weather_data}          
          \033[36m ''')

def delete_data():

    city = input("Enter city ")
    if city in weather_data :
        del weather_data[city]
        print(f"\033[32m weather data of {city} deleted successfully \033[36m ")

    else:
        raise Exception(f"the city named {city} not in our database !")



while(True):
    clear_terminal()
    print('''\033[36m 
    ------------------------------------------------
    Welcome in ( Weather Data Aggregation app 🌤️ )            
    ------------------------------------------------ \033[34m \033[1m
    1 - Search the weather data of a city 📤
    2 - Add new weather data of a city 📥
    3 - Update weather data of a city 🆙
    4 - Delete weather data of a city 🗑️
    5 - Display all weather data 🌎
    6 - Exit 👋
        \033[0m \033[36m
    ''')
    user_choise = int(input("Select a number from above menu : "))

    if not user_choise in range(1,7):
        
        print('''     
\033[31m Selected number not in the above menu! \033[36m
              ''')
        
    elif user_choise == 1 :
        try:
            weather_query()
        except KeyError as e :
            print("\n \033[31m Error: ",e,'\033[36m \n')
    elif user_choise == 2:
        try:
            add_data()
        except Exception as e:
            print("\n \033[31m Error: ",e,'\033[36m \n')
    elif user_choise == 3 :
        try:
            update_data()
        except Exception as e:
            print("\n \033[31m Error: ",e,'\033[36m \n')
    elif user_choise == 4 :
        try:
            delete_data()
        except Exception as e :
            print("\n \033[31m Error: ",e,'\033[36m \n')
    elif user_choise == 5 :
        try:
            display_data()
        except Exception as e :
            print("\n \033[31m Error: ",e,'\033[36m \n')
    elif user_choise == 6:
        print("\n \033[33m Thank you for using Weather Data Aggregation app 👋 \n ")
        break
    
    input("Press Enter to continue...")
