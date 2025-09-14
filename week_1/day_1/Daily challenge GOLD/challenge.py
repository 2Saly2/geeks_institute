from datetime import datetime, date

raw = input("Enter your birthdate (DD/MM/YYYY): ").strip()
try:
    birth = datetime.strptime(raw, "%d/%m/%Y").date()
except ValueError:
    print("Invalid date format. Use DD/MM/YYYY.")
    raise SystemExit

today = date.today()
if birth > today:
    print("Birthdate is in the future. Please enter a past date.")
    raise SystemExit

age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1


candles = age % 10 if age >= 0 else 0

print(f"\nYou are {age} years old. Candles to show: {candles}\n")

year = birth.year
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    leap = True
else:
    leap = False


top = "   ___" + ("i" * candles) + "___"
happy_line = "  |:H:a:p:p:y:|"
underline = " __|___________|__"
carrots = " |^^^^^^^^^^^^^^^^^|"
bday_line = " |:B:i:r:t:h:d:a:y:|"
empty_line = " |                 |"
base = " " + "~" * 19

if leap:
    print("You were born in a leap year — showing two cakes!\n")
    print(top)
    print(happy_line)
    print(underline)
    print(carrots)
    print(bday_line)
    print(empty_line)
    print(base)
    print() 
    print(top)
    print(happy_line)
    print(underline)
    print(carrots)
    print(bday_line)
    print(empty_line)
    print(base)
else:
    print(top)
    print(happy_line)
    print(underline)
    print(carrots)
    print(bday_line)
    print(empty_line)
    print(base)
