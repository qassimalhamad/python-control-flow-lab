# Exercise 1: Vowel or Consonant

def check_letter():
    letter = input("Enter a letter ")
    if len(letter) != 1:
        print("Please enter a single letter.")
    else:
        vowels = "aeiou"
        letter = letter.lower()
        if letter in vowels:
            print("The letter " + letter + " is a vowel.")
        else:
            print("The letter " + letter + " is a consonant.")
 
# Call the function
check_letter()

# Exercise 2: Old enough to vote?


def check_voting_eligibility():
    age = int(input("Please enter your age: "))
    # int(age) does not work
    if age < 0:
        
        print("No negative numbers please.")
    else:
        voting_age = 18
        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    dog_age = int(input("Input the dog's age: "))
    if dog_age < 0:
        print("No negative numbers please.")
    else:
        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7
        print("Dog age is " + str(dog_years))

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice


def weather_advice():
    cold = input("is it cold? (yes/no) ")
    raining = input("is it raining? (yes/no) ")
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    month = input('Enter the month of the year (Jan - Dec): ')
    day = int(input('Enter the day of the month: '))
    if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print('Invalid month .')
    elif day < 1 or day > 31:
        print('Invalid day .')
    else:
        if (month == 'Dec' and day >= 21) or (month == 'Jan') or (month == 'Feb') or (month == 'Mar' and day < 20):
            season = 'Winter'
        elif (month == 'Mar' and day >= 20) or (month == 'Apr') or (month == 'May') or (month == 'Jun' and day < 21):
            season = 'Spring'
        elif (month == 'Jun' and day >= 21) or (month == 'Jul') or (month == 'Aug') or (month == 'Sep' and day < 22):
            season = 'Summer'
        else:
            season = 'Fall'
        print(month + ' ' + str(day) + ' is in ' + season)

# Call the function
determine_season()