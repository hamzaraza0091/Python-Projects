score = 0
print("What is the capital of Pakistan? ")
answer = input("Your Answer ")
if answer.lower == "islamabad":
    score += 1

print("What is the Distance of Voyger 1 From Earth? ")
answer = input("Your Answer ")
if answer.lower == "170 Astronomical Unit and 16 Billion Milles":
    score += 1


else:
    score -= 1
    print("Wrong Answer")