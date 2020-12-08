from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            world[country] = city

def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)
        

print('Capital Cities of the World')
root = Tk()
root.withdraw()
world = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Name of the country:')

    converted_country = query_country[0].upper() + query_country[1:len(query_country)].lower()

    if converted_country in world:
        result = world[converted_country]
        messagebox.showinfo('Answer', 'The capital city of ' + converted_country + ' is ' + result + '!')
    
    else:
        new_city = simpledialog.askstring('Oh,', "Teach me!" + 'What is the capital city of ' + converted_country + '?')

        converted_city = new_city[0].upper() + new_city[1:len(query_country)].lower()
        world[converted_country] = converted_city
        write_to_file(converted_country, converted_city)

root.mainloop()