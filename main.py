import pandas
import numpy as np
import json
import math

def calculate_values():
    pass

if __name__ == "__main__":
    df = pandas.read_csv("./sample_data.csv")
    num_people = int(df.nunique()['name'])
    people = df['name'].unique()
    transaction_count = df.count()
    transaction_total = float(df.sum()['transaction_value'])
    

    people_dict = {}
    
    # iniitalize 0 for all people
    for person in people:
        people_dict[person] = 0

    # Load into hashmap
    for index, row in df.iterrows():
        people_dict[row['name']] += row['transaction_value']

    average_cost = transaction_total/num_people
    owed:list[str] = []
    owes:list[str] = []

    for key, value in people_dict.items():
        if (value < average_cost):
            owes.append(key)
        elif (value > average_cost):
            owed.append(key)
        
        people_dict[key] -= average_cost
        people_dict[key] = round(people_dict[key],2)
            


    transaction_matrix = np.zeros((num_people, num_people), dtype=float)
    transaction_matrix = pandas.DataFrame(transaction_matrix, columns=people, index=people)
    #print(transaction_matrix)

    for person in owed:
        while (not (people_dict[person] < 0.011)):
            if(abs(people_dict[owes[0]]) < abs(people_dict[person])):
                transaction_matrix.loc[person, owes[0]] += people_dict[owes[0]]
                people_dict[person] += people_dict[owes[0]]
                people_dict[person] = round(people_dict[person],2)
                people_dict[owes[0]] = 0
                owes.pop(0)
            elif(abs(people_dict[owes[0]]) > abs(people_dict[person])):
                transaction_matrix.loc[person, owes[0]] += people_dict[person]
                people_dict[owes[0]] += people_dict[person]
                people_dict[owes[0]] = round(people_dict[owes[0]],2)
                people_dict[person] = 0
            elif(abs(people_dict[owes[0]]) == abs(people_dict[person])):
                transaction_matrix.loc[person, owes[0]] += people_dict[owes[0]]
                people_dict[owes[0]] += people_dict[person]
                people_dict[owes[0]] = round(people_dict[person],2)
                people_dict[person] = 0
                owes.pop(0)
            
            #print(transaction_matrix)

    transaction_matrix = transaction_matrix.abs()
    output = transaction_matrix.to_dict()
    for person in people:
        new = {x:y for x,y in output[person].items() if y!=0}
        new = {key: value for key, value in sorted(new.items())}
        output[person] = new
    
    output = {key: value for key, value in sorted(output.items())}
    json_string = json.dumps(output, indent=4)  
    
    print(json_string)
    with open("output.json", "w") as outfile: 
        outfile.write(json_string)


