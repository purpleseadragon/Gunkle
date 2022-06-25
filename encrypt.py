import os
import random
import csv

directory_path_init = r'C:\Users\o_dav\OneDrive\Documents\python_projects\Gunkle\countries'
directory_path_new = r'C:\Users\o_dav\OneDrive\Documents\python_projects\Gunkle\countries_updated'

    
def generate_code(n):
    """Outputs n long random string"""
    letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
                'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
                'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
                's', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
                'X', 'y', 'Y', 'z', 'Z', '1', '2', '3' , '4', '5', '6', '7',
                '8', '9']
    name = ""
    for _ in range(n):
        name += random.choice(letters)
    return name

def rename_countries():
    # maps country IDs to names
    countries_dict = {}

    # for file names in directory - disregarded error checking as next to 0 chance 
    # that there are matching names
    for filename in os.listdir(directory_path_init):
        f = os.path.join(directory_path_init, filename)
        new_name = generate_code(10)
        new_name += ".png"
        countries_dict[filename] = new_name
        os.rename(f, os.path.join(directory_path_init, new_name))
    return countries_dict

countries_dict = rename_countries()

# writes country names and codes to file
with open("country_codes.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for key in countries_dict:
        writer.writerow([key, countries_dict[key]])

