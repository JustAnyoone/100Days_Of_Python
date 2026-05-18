age_id = int(input("What's your current age ? : "))

def life_in_weeks(age):
    weeks_left = (90 - age)
    weeks = weeks_left * 52
    print(f"You have {weeks} weeks left")

life_in_weeks(age_id)