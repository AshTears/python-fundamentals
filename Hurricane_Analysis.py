# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 
         'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 
         'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 
          'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 
          'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 
                       175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], 
                  ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
                  ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], 
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', 
           '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', 
           '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages():
  updated_damages = []
  for record in damages:
    if record.startswith("Damages"):
      updated_damages.append(record)
      continue
    num = float(record[:-1])
    new_damages = 0
    if record[-1] == 'M':
      new_damages = conversion["M"] * num
    else:
      new_damages = conversion["B"] * num
    updated_damages.append(new_damages)
  return(updated_damages)

# test function by updating damages
#print(update_damages())

# 2 
# Create a Table
def create_hurricanes():
  hurricanes = {}
  for storm in range(0, len(names)):
    k = names[storm]
    hurricanes[k] = {
      'Name':names[storm], 'Month':months[storm], 'Year':years[storm], 'Max Sustained Wind':max_sustained_winds[storm], 
      'Areas Affected':areas_affected[storm], 'Damage':damages[storm], 'Deaths':deaths[storm]
    }
  return hurricanes
  
# Create and view the hurricanes dictionary
hurricanes_dict = create_hurricanes()
#print(hurricanes_dict)

# 3
# Organizing by Year
def organize_year():
  year_dict = {}
  for year in range(0, len(years)):
    k = years[year]
    year_info = {'Name':names[year], 'Month':months[year], 'Year':years[year], 
                 'Max Sustained Wind':max_sustained_winds[year], 'Areas Affected':areas_affected[year], 'Damage':damages[year], 
                 'Deaths':deaths[year]}
    if k not in year_dict:
      year_dict[k] = []
      year_dict[k].append(year_info)
    else:
      year_dict[k].append(year_info)
  return year_dict
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_year()
#print(hurricanes_by_year)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def count_areas_affected():
  areas_dict = {}
  for array in areas_affected:
    for name in array:
      if name not in areas_dict:
        areas_dict[name] = 1
      else: areas_dict[name] += 1
  return areas_dict
areas_affected_count = count_areas_affected()
#print(areas_affected_count)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def area_most_hit():
  max_value = 1
  area_hit = ""
  for key, value in areas_affected_count.items():
    if value > max_value:
      max_value = value
      area_hit = key

  return (area_hit, max_value)

#print(area_most_hit())
# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest_storm():
  deaths_copy = deaths.copy()
  deaths_copy.sort()
  max_number = deaths_copy[-1]
  max_index = deaths.index(max_number)
  storm = names[max_index]
  return(storm, max_number)

#print("Deadliest storm is %s with %d deaths." %(deadliest_storm()))
# 7
# Rating Hurricanes by Mortality
def mortality_ratings():
  mortality_rating = {0: [], 1: [], 2: [], 3: [],  4: [], 5: []}
  for key, value in hurricanes_dict.items():
    if value['Deaths'] > 10000:
      mortality_rating[5].append(key)
    elif value['Deaths'] > 1000:
      mortality_rating[4].append(key)
    elif value['Deaths'] > 500:
      mortality_rating[3].append(key)
    elif value['Deaths'] > 100:
      mortality_rating[2].append(key)
    elif value['Deaths'] > 0:
      mortality_rating[1].append(key)
    else:
      mortality_rating[1].append(key)
  return mortality_rating
# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality_ratings = mortality_ratings()
#print("Hurricane Mortality Ratings: ",hurricane_mortality_ratings)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def greatest_damage():
  damages_list = update_damages()
  name_damages = list(zip(names, damages_list))

  max_damage = 100000.00
  storm = ""
  for pair in name_damages:
    if pair[1] == 'Damages not recorded':
      continue
    elif pair[1] > max_damage:
      max_damage = pair[1]
      storm = pair[0]
  return (storm, max_damage)

print("%s has the greatest damage with %.2f." %(greatest_damage()))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating():
    damage_rating = {0: [], 1: [], 2: [], 3: [],  4: []}
    damages_list = update_damages()
    name_damages = list(zip(names, damages_list))
    for pair in name_damages:
        if pair[1] == 'Damages not recorded': continue
        if pair[1] >= damage_scale[4]:
            damage_rating[4].append(pair[0])
        elif pair[1] >= damage_scale[3]:
            damage_rating[3].append(pair[0])
        elif pair[1] >= damage_scale[2]:
            damage_rating[2].append(pair[0])
        elif pair[1] >= damage_scale[1]:
            damage_rating[1].append(pair[0])
        else: damage_rating[0].append(pair[0])
            
    return damage_rating
    
print(damage_rating())