def find_text_in_file():
    look_up = input("Enter an text to look up: \n")
    found = False
    try:
        with open("input.txt", "r") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
                if not found:
                        print("Text not found in the file.")
    except FileNotFoundError:
        print("The file 'input.txt' does not exist.")
        return

def add_text_to_file():
    text = input("What text you want to add to the file? \n")
    try:
        with open("input.txt", "a") as file:
            file.write(text + "\n")
    except FileNotFoundError:
        print("The file 'input.txt' does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return

def main():
    while True:
        print("Choose an option:")
        print("1. Find text in file")
        print("2. Add text to file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): \n")

        if choice == '1':
            find_text_in_file()
        elif choice == '2':
            add_text_to_file()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
