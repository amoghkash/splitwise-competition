import csv
from random import randint, random
import math

max_transaction_value = 200

if (input("Randomize Values? y or n\n") == "y"):
    people_count = randint(3,25)
    transaction_count = randint(25,250)
else:
    people_count = int(input("How many people involved?\n"))
    transaction_count = int(input("How many total transactions?\n"))

with open('./sample_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "transaction_value"]
    writer.writerow(field)

    for i in range(transaction_count):
        person_name = "Person" + str(randint(1, people_count))
        transaction_value = round((random() * max_transaction_value) + 1,2)
        datapoint = [person_name, transaction_value]
        writer.writerow(datapoint)