# You have been asked to create a program that organizes and updates medical records efficiently.

# Create an empty dictionary
medical_costs = {}

# Populate the medical_costs dictionary
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Add three patients in one line of code
medical_costs.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})

# Print medical_costs
print(medical_costs)

# Update Vinay's insurance cost to 3325.0
medical_costs["Vinay"] = 3325.0

# Calculate and print the average medical cost of each patient.
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: {}".format(average_cost))

# Create a second dictionary that maps patient names to their ages
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = list(zip(names, ages))
names_to_ages = {pair[0]:pair[1] for pair in zipped_ages}

print(names_to_ages)

# Use .get() to get the value of Marina's age
marina_age = names_to_ages.get("Marina", None)
print("Marina's age is {}".format(marina_age))

# Using a Dictionary to create a medical database
medical_records = {}

# Add Marina's medical data to the dictionary
medical_records["Marina"] = {"Age": 27, "Sex":"Female", "BMI":31.1,
                             "Children":2, "Smoker": "Non-smoker",
                             "Insurance_cost": 6607.0}

# Add more patients
medical_records["Vinay"] = {"Age":24, "Sex":"Male", "BMI":26.9, "Children": 0,
                            "Smoker":"Non-smoker", "Insurance_cost":3225.0}
medical_records["Connie"] = {"Age":43, "Sex":"Female", "BMI":25.3,
                             "Children":3, "Smoker":"Non-smoker",
                             "Insurance_cost":8886.0}
medical_records["Isaac"] = {"Age":35, "Sex":"Male", "BMI":20.6, "Children":4,
                            "Smoker":"Smoker", "Insurance_cost":6420.0}
medical_records["Valentina"] = {"Age":52, "Sex":"Female", "BMI":18.7,
                                "Children":1, "Smoker":"Smoker",
                                "Insurance_cost": 6420.0}

print(medical_records)

# Access a specific piece of data in the database
print("Connie's insurance cost is {} dollars".format(medical_records["Connie"].get("Insurance_cost")))

# Vinay has moved to another country
del medical_records["Vinay"]

#Display each patient's record
for name, info in medical_records.items():
    print("{} is a {} year old {} {} with a BMI of {} and insurance cost of {}.".format(name, info["Age"], info["Sex"], info["Smoker"], info["BMI"], info["Insurance_cost"]))

    