# Weight Conversation Program

Weight = float(input("Enter Your Weight: "))
Unit = input("Enter unit in Kilograms or Pounds (Kg/Lb): ")

if Unit == "Kg":
    Weight = Weight * 2.20462
    Unit = "lbs."
    print(f"Your Weight is {Weight} lbs.")
