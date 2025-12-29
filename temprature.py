temp = float(input("Enter temperature: "))
unit = input("Is this in (C) or (F)? ").lower()

if unit == "c":
    f = (temp * 9/5) + 32
    print(f"{temp}°C = {f}°F")
elif unit == "f":
    c = (temp - 32) * 5/9
    print(f"{temp}°F = {c}°C")
else:
    print("Invalid unit.")