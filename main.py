from calculator import Calculator
from history import History
from art import logo


def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


calc = Calculator()
history = History()

def get_valid_operation():
    valid_operations = ["+", "-", "*", "/"]
    while True:
        calc.show_operation_symbols()
        op = input("Pick an operation: ")
        if op in valid_operations:
            return op
        else:
            print("❌ Invalid operation! Please choose one of the valid symbols.")


def main():

    print(logo)
    print("Welcome to the Python Calculator!")


    last_result = None

    while True:
        print("\noptions: calculate / history / clear / exit")
        choice = input("Choose an option:  ").lower()

        if choice == "calculate":
            if last_result is None:
                num1 = get_valid_number("Enter the first number:  ")
            else:
                use_last = input(f"Type 'yes' to continue calculating with ({last_result}), or type 'no':  ").lower()
                if use_last == "yes":
                    num1 = last_result
                else:
                    num1 = get_valid_number("Enter the first number:  ")


            operation_choice = get_valid_operation()


            num2 = get_valid_number("Enter the second number: ")


            try:
                result = calc.operations[operation_choice](num1, num2)
                answer = f"{num1} {operation_choice} {num2} = {result:4f}"
                print(answer)
                last_result = result
                history.add_record(answer)
            except TypeError:
                print("Please enter a valid number.")
            except Exception as e:
                print(e)
            except KeyError:
                print("Invalid operation!")



        elif choice == "history":
            history.show_history()

        elif choice == "clear":
            history.clear_history()
            print("History cleared.")

        elif choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


main()