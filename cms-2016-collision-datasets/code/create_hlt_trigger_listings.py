"""
Create HLT Trigger Listing for 2016 Datasets
"""

import csv

YEAR = 2016
INPUT_FILE_PATH = "./inputs/triggers_runII_year_fixed.txt"

def create_trigger_listing_file():
    with open(INPUT_FILE_PATH, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        output = open(f"./inputs/hlt-{YEAR}-dataset.txt", "w")
        for line in data:
            if line[7] == str(YEAR):
                output.write(f'{line[6]},{line[0]}\n')

def main():
    create_trigger_listing_file()

if __name__ == "__main__":
    main()