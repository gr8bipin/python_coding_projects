# This Python script implements a simple graphical that allows users to query and add data about capital cities of the world using the Tkinter library.
from tkinter import Tk, simpledialog, messagebox # Tk: used to create a Tkinter root window for GUI interaction. 
                                                  # simpledialog: Provides simple input dialog boxes for the user to enter data. 
                                                  # Displays pop-up message boxes to show results or information to the user.

def read_from_file(): # This function reads data from a file named capital_data.txt, where each line contains a country and its capital separated by a /.
    with open('D:\python_coding_projects\python_projects\capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n') # removes the newline character at the end of the line.
            country, city = line.split('/') # splits the line into 'country' and 'city' based on the '/' delimiter.
            the_world[country] = city # stores the data in a dictionary called 'the_world'.

# This function reads data from a file named capital_data.txt, where each line contains a country and its capital separated by a /.
# The data is stored in a dictionary called the_world, where the key is the country and the value is the capital city.

# write_to_file(country_name, city_name):
def write_to_file(country_name, city_name):
    with open('D:\python_coding_projects\python_projects\capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

# This function appends new country-capital data to capital_data.txt in the format: country/ city.
# 'a' mode is used to append data without overwriting the file.

# Main Program Logic
# Initializing the Application
print("Ask the expert - Capital cities of the world") # display the title of the project in the shell
root = Tk() # create an empty Tkinter window
root.withdraw() # hide the Tkinter window

# Set up a dictionary
the_world = {} # this creates an empty dictionary called the_world, use curly brackets # this dictionary will store the names of the countries and their capital cities
read_from_file()

# A title is printed to the console for context.
# A Tkinter root window is created and immediately hidden using root.withdraw(), as it is not needed for this application.
# The the_world dictionary is initialized to store country-capital data.
# read_from_file() is called to populate the dictionary from the file.

# User Interaction
while True:
    query_country = simpledialog.askstring('country', 'Type the name of a country:')
 # A while loop runs indefinitely to repeatedly prompt the user for a country name.
 # simpledialog.askstring is used to display a dialog box asking the user to type the name of a country. The input is stored in the variable query_country.   

# If the country exists
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
 # If the country is found in the the_world dictionary, its capital city is retrieved.
 # A messagebox displays the result: "The capital city of <country> is <capital>!"   

# if the country is unknown
    else:
        try:
            new_city = simpledialog.askstring('Teach me', 'I don\'t know! What is the capital city of' + query_country + '?')
            the_world[query_country] = new_city
            write_to_file(query_country, new_city)
        except TypeError as e:
            print(f"TypeError occurred: {e}")

 # if the country is not found, the program asks the user for the capital city of that country.
 # The new country-capital pair is added to the dictionary and saved to the file using write_to_file().

# Exiting the Application
    root.mainloop()
 # root.mainloop() is the main event loop for Tkinter, which keeps the application running and responsive.

# How it works?
    # When the script starts, it loads existing country-capital data from capital_data.txt into a dictionary.
    # The user is repeatedly asked for a country name:
        # if the country is known, its capital is displayed in a message box.
        # if the country is unknown, the user is prompted to teach the program the capital city, and this new data is saved to the file.
        # the application runs until manually closed.

# File Structure (capital_data.txt)
    # the file capital_data.txt should have a format like this:
        # Nepal/ Kathmandu
        # USA/ Washington
        # France/ Paris

# Key Features:
    # Persistent storage: The program saves new data permanently to the file.
    # User interaction: Provides a friendly interface using dialog and message boxes.
    # Learning behavior: The program grows its knowledge base with user input.

# Potential Improvements:
    # Error Handling: Add checks for invalid inputs or file issues (eg, file not found)
    # Exit option: Allow the user to exit the loop gracefully by entering a specific keyword (eg., "exit")
    # Data validation: Ensure inputs are not empty or malformed before saving to the file.

