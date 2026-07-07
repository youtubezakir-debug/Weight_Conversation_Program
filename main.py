# Wieght Conversation Program

Wieght = float(input("Enter Your Wieght: "))
Unit = input("Enter unit in Kilograms or Pounds (Kg/Lb): ")

if Unit == "Kg":
    Wieght = Wieght * 2.20462
    Unit = "lbs."
    print(f"Your Wieght is {Wieght} lbs.")
