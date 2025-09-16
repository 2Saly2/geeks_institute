import random

def get_random_temp(season):
    if season.lower() == "winter":
        low, upper = -10, 16
    elif season.lower() == "summer":
        low, upper = 24, 40
    elif season.lower() in ["autumn", "fall"]:
        low, upper = 0, 23
    else:  
        low, upper = 8, 28
    return random.randint(low, upper)

def main():
    season = input("Enter the season (winter, spring, summer, autumn): ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}°C")
    
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 17 <= temp <= 23:
        print("Mild weather")
    elif 24 <= temp <= 32:
        print("Warm weather")
    else:
        print("Hot! Stay hydrated")

main()

