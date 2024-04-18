import csv
import os

path = "./data"

with open('sorted_data.csv', mode='w', newline='') as csv_file:
    # create fields for csv file
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # get a list of all the files in the data folder
    for file in os.listdir(path):
        with open(os.path.join(path, file), "r") as import_data:
            reader = csv.DictReader(import_data)
            for row in reader:
                if row['product'] == "pink morsel":  # Assuming 'Product' is the column name
                    price = float(row['price'][1:])
                    sold = int(row['quantity'])
                    sales = str(price * sold)
                    date = row['date']
                    region = row['region']

                    output = {'sales': sales, 'date': date, 'region': region}
                    writer.writerow(output)
