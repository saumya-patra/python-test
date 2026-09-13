text = input("What text you want to add to the file? \n")
with open("input.txt", "a") as file:
    file.write(text + "\n")