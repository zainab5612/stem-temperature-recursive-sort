def recursive_sort(list_to_sort, key=0):
    """
     Recursively sorts a list of tuples using bubble sort.

    Args:
    list_to_sort (list): The list of tuples to be sorted.
    key (int): The index to sort by (0 for room number, 1 for room name).

    Returns:
    list: The sorted list.
    """
    # Base case: if the list has 1 or fewer items, it's already sorted
    if len(list_to_sort) <= 1:
        return list_to_sort

    # Go through the list and swap elements if they’re in the wrong order
    swapped = False
    for i in range(len(list_to_sort) - 1):
        if list_to_sort[i][key] > list_to_sort[i + 1][key]:
            # Swap the items
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            swapped = True

    # If nothing was swapped, the list is already sorted
    if not swapped:
        return list_to_sort

    # Keep sorting the list recursively, ignoring the last sorted element
    return recursive_sort(list_to_sort[:-1], key) + [list_to_sort[-1]]


def print_header():
    """
    Prints the title and author for the STEM Center Temperature Project.
    """
    # Display the project title and the author name
    print("STEM Center Temperature Project")
    print("Zainab Abdulhasan")


def print_menu():
    """
    Shows the main menu with different options for the user.
    """
    print("""
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
""")


# Placeholder functions from Assignment 4
def new_file(dataset=None):
    print("New File Function Called, dataset:", dataset)

def choose_units():
    print("Choose Units Function Called")

def change_filter(sensor_list=None, active_sensors=None):
    print("Change Filter Function Called, sensor_list:", sensor_list, "active_sensors:", active_sensors)

def print_summary_statistics(dataset=None, active_sensors=None):
    print("Summary Statistics Function Called, dataset:", dataset, "active_sensors:", active_sensors)

def print_temp_by_day_time(dataset=None, active_sensors=None):
    print("Print Temp by Day/Time Function Called, dataset:", dataset, "active_sensors:", active_sensors)

def print_histogram(dataset=None, active_sensors=None):
    print("Print Histogram Function Called, dataset:", dataset, "active_sensors:", active_sensors)


def main():
    """
      Main function that sets up the program and runs it.
    """
    # Define the sensors dictionary with room numbers, names, and ID
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }

    # Create a list of tuples (room number, room name, sensor ID)
    sensor_list = [(room_number, sensors[room_number][0], sensors[room_number][1]) for room_number in sensors]

    # Display original and sorted lists with additional spacing
    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n", recursive_sort(sensor_list.copy(), 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list.copy(), 1))
    print("\nOriginal unsorted list\n", sensor_list)


    print()
    # Show the project title and author
    print_header()

    # Main program loop to display the menu and handle user input
    while True:
        print_menu()
        try:
            # Ask the user for their menu choice
            choice = int(input("What is your choice? "))
            if choice == 1:
                new_file()
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(sensor_list)
            elif choice == 4:
                print_summary_statistics()
            elif choice == 5:
                print_temp_by_day_time()
            elif choice == 6:
                print_histogram()
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice, please enter an integer between 1 and 7.")
        except ValueError:
            # If the input isn’t an integer, show an error message
            print("*** Please enter a number only ***")

        # Add spacing between each menu interaction for readability
        print()


if __name__ == "__main__":
    main()


"""
"C:\\Users\\zandu\\python projects\\Assignment-6.py\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\Assignment-6.py\\Assignment-6.py" 

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

List sorted by room number
 [('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 5), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

STEM Center Temperature Project
Zainab Abdulhasan

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0
"""