# Blood Donation Eligibility Program

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood ✅")
    else:
        print("You are not eligible because weight is less than 50 kg ❌")
else:
    print("You are not eligible because age is less than 18 ❌")
