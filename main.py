# Weight Conversation Program

Weight = float(input("Enter Your Weight: "))
Unit = input("Enter Your Weight unit: Kilograms or Pounds (K/L): ")

if Unit == "K":
    Weight = Weight * 2.204
    Unit = "lbs."
    print(f"Your Weight is {round(Weight, 1)} lbs.")

elif Unit == "L":
    Weight =Weight / 2.204
    Unit = "kg"
    print(f"Your Weight is {round(Weight, 1)} kgs.")


