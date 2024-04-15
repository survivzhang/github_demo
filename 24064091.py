def main(csvfile, age_group, country):
  age_upper = age_group[1]
  age_lower = age_group[0]
  OP1 = []
  OP2 = []
  OP3 = []
  OP3_all_time = []
  OP3_time = {}
  OP3_average={}
  OP3_income = []
  sum_OP3 = 0
  OP4_age = {}
  OP4_income = {}
  try:
    with open(csvfile) as file_object:
      contents = file_object.readlines()
      #open the file and read it by line
  except FileNotFoundError:
    msg = "Sorry, the file " + csvfile + " doesn't exist"
  else:
      for line in contents[1:]:
      #loop all the data by line
        parts = line.split(',')
        id = parts[0]
        age = int(parts[1])
        gender = parts[2]
        time_spent_hour = int(parts[3])
        platform = parts[4]
        interests = parts[5]
        country_single = parts[6]
        demographics = parts[7]
        profession = parts[8]
        income = float(parts[9])
        indebt = parts[10]
        # collect every type of data
        if profession.lower() == 'student' and age_lower <= age <= age_upper and indebt and time_spent_hour > 7  and country_single.lower() == country.lower():
        #OP1 condition
          OP1.append([id, income])
          #OP1
        if age_lower <= age <= age_upper:
          #OP2 OP3 condition
          OP2.append(country_single)
          OP2 = list(set(OP2))
          #exclude duplicate elements
          OP2.sort()
          #sort in alphabetically ascending order
          #OP2
          OP3_all_time.append(time_spent_hour)
          #collect time_spent
          OP3_income.append(income)
          #collect income
          if demographics.lower() in OP3_time:
            OP3_time[demographics.lower()].append(time_spent_hour)
          else:
            OP3_time[demographics.lower()] = [time_spent_hour]
          #OP3 data in different platform
        if platform in OP4_age:
          OP4_age[platform].append(age)
          OP4_income[platform].append(income)
          #ensure age and income in the same position of diff dictionaries
        else:
          OP4_age[platform] = [age]
          OP4_income[platform] = [income]
          #creat new platfrom in dictionary 
          #OP4 data collect
      OP3_time_average = sum(OP3_all_time)/len(OP3_all_time)
      OP3_income_average = sum(OP3_income)/len(OP3_income)
      for inco in OP3_income:
        sum_OP3 += (inco - OP3_income_average)**2
        #the part of function
      deviation = (sum_OP3 / (len(OP3_income)-1))**(1/2)
      # OP3 deviation
      for key, value in OP3_time.items():
        OP3_average[key] = sum(value)/len(value)
      #the average time of all demographics
      min_time = min(time for time in OP3_average.values())
      #find the min_time _spend
      demographics_with_min_time = [key for key in OP3_average.keys() if OP3_average[key] == min_time]
      #all the platform with min_time_spent
      chosen_demo = sorted(demographics_with_min_time)[0]
      #sort in alphabetical order and find the first
      OP3_time_average = round(OP3_time_average, 4)
      deviation = round(deviation, 4)
      OP3 = [OP3_time_average, deviation, chosen_demo]
      #OP3 
      max_length = max(len(value) for value in OP4_age.values())
      #the most people in one platform
      platforms_with_most_people = [key for key,value in OP4_age.items() if len(value)==max_length]
      #all the platforms with most people
      platform_with_most_people = sorted(platforms_with_most_people)[0]
      #sort in alphabetical order and find the first
      sum_upstairs = 0
      sum_downstairs_age = 0
      sum_downstairs_income = 0
      sum_downstairs=0
      average_age = sum(OP4_age[platform_with_most_people]) / len(OP4_age[platform_with_most_people])
      average_income = sum(OP4_income[platform_with_most_people]) / len(OP4_income[platform_with_most_people])
      for index in range(max_length):
        single_age_diff = OP4_age[platform_with_most_people][index] - average_age
        single_income_diff = OP4_income[platform_with_most_people][index] - average_income
        sum_upstairs += (single_age_diff * single_income_diff)
        sum_downstairs_age += (single_age_diff ** 2)
        sum_downstairs_income += (single_income_diff ** 2)
      sum_downstairs = (sum_downstairs_income * sum_downstairs_age)**(1/2)
      #the function
      coefficient = sum_upstairs / sum_downstairs
      coefficient = round(coefficient, 4)
      OP4 = coefficient
  return OP1, OP2, OP3, OP4



OP1,OP2,OP3,OP4 = main('SocialMedia.csv', [18,25], 'australia')

print(OP1,OP2,OP3,OP4)