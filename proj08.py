############################################DOCSTRING





'''For this project, you will create a program that will store the information of diabetes prevalence,
both type-1 and type-2, in over 220 countries within a dictionary. From this dictionary, you need
to select a region to visualize the number of people with diabetes, their age group distribution,
and gender distribution for all the countries covered by the selected region. You will use tables,
bar charts and pie charts for data visualization.'''

import pylab 
#from operator import itemgetter   # optional, if you use itemgetter when sorting

REGIONS = {'MENA':'Middle East and North Africa','EUR':'Europe',\
               'AFR':'Africa','NAC':'North America and Caribbean',\
               'SACA':'South and Central America',\
               'WP':'Western Pacific','SEA':'South East Asia'}

def open_file():
    '''Prompt user to enter a filename containing the diabetes prevalence data.
An error message should be shown if the file cannot be opened. 
The function will loop until it opens a file. Returns a file pointer.
Most likely will need to include special statement to read the Unicode chars:
    encoding ="windows-1252" e.g.
 fp = open("diabetes_data_small.csv",encoding ="windows-1252")'''
 
    usefile = input("Please enter a file name: \n")
    while True:
        #continually prompts user until correct file name given
        try:  
            fp = open(usefile, encoding = "windows-1252")
            return fp
        except FileNotFoundError:
            fp = input("File not found. Please enter a valid file name:")

    
    
def create_dictionary(fp):
    '''reads the file, and creates the dictionary containing the diabetes info.
The dictionary will have three keys (region, country, and age group). 
That is, it is a dictionary of CSE 231 Fall 2018 dictionaries of 
dictionaries of lists of tuples. The function returns the dictionary. 
For each line in the file, you need to read the following:
    
country = line_list[1]
region = line_list[2]
age_group = line_list[3]
gender = line_list[4]
geographic_area = line_list[5]
diabetes = int(float(line_list[6])*1000)
population = int(float(line_list[7])*1000)
tup = (gender, geographic_area, diabetes, population)

# there is more needed here to properly set up the dictionary D
D[region][country][age_group].append(tup)
'''

    dic = {}
    fp.readline()
    for line_list in fp:
        line = line_list.strip().split(',')
        country = line[1]
        region = line[2]
        age_group = line[3]
        gender = line[4]
        geographic_area = line[5]
        diabetes = int(float(line[6])*1000)
        population = int(float(line[7])*1000)
        tup = (gender, geographic_area, diabetes, population)
        
        if region not in dic:
            dic[region] = {}
        if country not in dic[region]:
            dic[region][country] = {}
        if age_group not in dic[region][country]:
            dic[region][country][age_group] = []
        
        dic[region][country][age_group].append(tup)
    return dic

def get_country_total(data):
    '''receives a dictionary from a specific region, and returns a new 
dict of tuples with the number of people with diabetes and the total pop
for each country—the country name is the key, the tuple has total number of
people with diabetes followed by the total population for the country.
    '''  
  #entered data = {'MENA': {'Afghanistan': {'20-24': [('Female', 'Urban', 6786, 442695), ('Male', 'Urban', 2699, 474429)], '35-39': [('Female', 'Urban', 17834, 237228),
  ##dictoftuples = {country: {age range: [gender, geographic area, diabetes, total pop]}}
  #number of people w/ diabetes, total pop for each country- country name-key, the tuple has total num of people with diabetes followed by the total population for the country
  
    dic2 = {}
    #data = get_country_total(data[region]) #You need to call the function with a specific region in mind.
    #### this part goes in main
    
    
    #dic[country][age_group](gender, geographic_area, diabetes, population)
    
    for country in data:
        diabetestot = 0
        populationtot = 0
        for age_group in data[country]:
            for tup in data[country][age_group]:
                #total people with diabetes added
                diabetestot += tup[2]
                #total people in country
                populationtot += tup[3]
            
        tup = (diabetestot, populationtot)
                                
        dic2[country] = tup
        
    #returns {'Afghanistan': (113261, 1770464), 'Egypt': (1301102, 10803831)}
    return dic2 #{returns "country"-key: (number people with diabetes, total pop for country)}
    
def display_table(data, region):
    '''
uses the dictionary from the get_country_total function, 
and uses the full name of the region. 

This function returns nothing. 
It displays (In alphabetical order!) the country name, number of people with 
diabetes, and the total population of that country. 

There are two header lines and at the bottom is one line with totals for
diabetes and population. Truncate country names to 24 characters. 
The formatting string for entries in the table is: "{:<25s}{:>20,d}{:>16,d}"'''
    totdiabetes = 0
    totpop = 0
    for key in REGIONS:
        if region == key:
           print("{:^61s}".format("Diabetes Prevalence in " + REGIONS[region]))
           print("{:<25s}{:>20s}{:>16s}".format("Country Name","Diabetes Prevalence", "Population"))
           print("")
           for key, ch in sorted(data.items()):
               print("{:25s}{:>20,d}{:16,d}".format(key, ch[0], ch[1]))
               totdiabetes += ch[0]
               totpop += ch[1]
    print('')
    print("{:25s}{:>20,d}{:16,d}".format("TOTAL", totdiabetes, totpop))
    print("")
        
        
        
    



    '''5. Can you "sort" a dictionary for each country alphabetically?

Well, you can't sort the dictionary by country name (unless you use a ordered dictionary)! However, there is a simpler way. You can create a list of the keys, sort the list and iterate through the sorted list to access the values from the dictionary. If they keys are sorted, then you can access the values in order.
'''
    '''
    D = {...}

    # There are two ways to get the list of keys
    key_lst = list(D) # This is the same as D.keys()
    key_lst = list(D.keys()) # Explicitly mention that you want the keys.
    
    # Iterate through the key_lst after being sorted
        print(D[key]) # key is each element from key_lst

'''
    '''
    print("{:^61s}".format("Diabetes Prevalence in " + region))
    print("{:<25s}{:>20s}{:>16s}".format("Country Name","Diabetes Prevalence", "Population"))
    print("{:25s}{:>20,d}{:16,d}".format("ENTER", "IN", "LATER"))
'''
def prepare_plot(data):
    '''This function receives a dictionary for a specific region. We want to
plot the region by age group and gender, that is, combine all the countries in the region’s
data so it can be displayed by age group and gender. 

It returns a new dictionary with the age group and gender as its keys—the value totals all the countries in the region’s data
for that age group and gender.

This data will be used to plot the bar chart and pie chart that visualizes the 
age group distribution per gender, and the gender distribution of people
with diabetes respectively for all the countries in a specific region.
    '''

    agedic = {}
    for country in data:
#        diabetesmales = 0
#        diabetesfemales = 0
        #diabetestot = 0
        for age_group in data[country]:
            if age_group not in agedic:
                agedic[age_group] = {}
            for tup in data[country][age_group]:
                if tup[0].upper() not in  agedic[age_group]:
                    agedic[age_group][tup[0].upper()] = tup[2]
                else:
                    agedic[age_group][tup[0].upper()] += tup[2]
#                    diabetesmales += tup[2]
                    #agedic[age_group] = {"Male":diabetesmales}
                    #diabetestot += tup[2]
#                if tup[0] == "Female":
#                    agedic[age_group][] += tup[2]
                    #diabetesfemales += tup[2]
                    #agedic[age_group] = {"Female":diabetesfemales}
                    #diabetestot += tup[2]
        
#            agedic[age_group] = {"MALE":diabetesmales, "FEMALE":diabetesfemales}
    
    return agedic
 

def plot_data(plot_type,data,title):
    '''
    plot_data(plot_type,data,title) This function receives a string indicating which plot will
be used ("BAR" or "PIE"), a dictionary with the diabetes data for a specific region (the
dictionary returned by the prepare_plot function), and the title of the plot. This
function returns nothing. This function is already provided for this project.
        This function plots the data. 
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender. 
    
        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries 
                         within a specific region.
            title (string): Plot title
            
        Returns: 
            None
            
    '''
    
    plot_type = plot_type.upper()
    
    categories = data.keys() # Have the list of age groups
    gender = ['FEMALE','MALE'] # List of the genders used in this dataset
    
    if plot_type == 'BAR':
        
        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories] 
        
        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female, width = width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male, width = width)
        pylab.legend((p1[0],p2[0]),gender)
    
        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')
        
        # Place the tick between both bar plots
        pylab.xticks([x + width/2 for x in range(len(categories))], categories, rotation='vertical')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        #pylab.savefig("plot_bar.png")
        
        
    elif plot_type == 'PIE':
        
        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])
        
        pylab.title(title)
        pylab.pie([female,male],labels=gender,autopct='%1.1f%%')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        #pylab.savefig("plot_pie.png")

def main():
    '''prompt for and opening a file. 
Next, calls the create_dictionary() function to build the data dictionary. 

Then prompt the user for a region to visualize the data. 
If the region is a valid region, the program will display a table of the 
diabetes prevalence for each country represented by the region 
(the program will continue prompting until a valid region is entered). 

Then, the program will prompt the user whether they want to display the age 
group and gender distributions of the data and plot the data. For this prompt, 
the program only accepts yes/no answers! 

The program will stop once the user enters “quit” for the region prompt. 
Keep in mind that the program evaluates “Quit” and “qUIt” and “quiT” as the same word (Hint: Use the upper() function)'''
    x = True
    fp = open_file()
    data = create_dictionary(fp)
    while x == True:
        
        print('''                Region Codes
    MENA: Middle East and North Africa
    EUR: Europe
    AFR: Africa
    NAC: North America and Caribbean
    SACA: South and Central America
    WP: Western Pacific
    SEA: South East Asia
    ''')

        region = input("Enter region code ('quit' to terminate):")
        if region.upper() == "QUIT":
            x == False
            break
        try:
            regiondic = data[region.upper()]
            #data = dataregion = data[0]
        except KeyError:
            print("Error")
        
        cdata = get_country_total(regiondic)
        
        #if region in REGIONS:
        display_table(cdata, region.upper())
        #else:
        #    print("error")
           
            
        toplot = input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?:")
        if toplot == "yes":
            something = prepare_plot(regiondic)
            title = "Diabetes Prevalence by Age Group and Gender"
            plot_data("PIE",something,title)
            plot_data("BAR",something,title)
        if toplot == "no":
            continue

        #region = region.upper()
        if region.upper() == "QUIT":
            x == False





    '''you need to keep the original data intact. Do not assign the result 
        from get_country_total to the variable data, it will overwrite the original dictionary.'''
    #data = create_dictionary(fp)
    #print(data) # data is the entire dictionary for all regions
    #data = get_country_total(data[region])
    #print(data) # Here is just the dictionary for a specific region.
    
    '''plot_values = prepare_plot(data) # You require the original dictionary, but you replaced it with the country total.
        '''
    
    '''    
        "\nDiabetes Prevalence Data in 2017"
        MENU = \
        ''''''
                    Region Codes
        MENA: Middle East and North Africa
        EUR: Europe
        AFR: Africa
        NAC: North America and Caribbean
        SACA: South and Central America
        WP: Western Pacific
        SEA: South East Asia
        ''''''
        
        "Enter region code ('quit' to terminate): "
        "Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: "
        "Error with the region key! Try another region"
        "Incorrect Input! Try Again!"
        
    '''
        
###### Main Code ######
if __name__ == "__main__":
    main()
        
        
        
        
        
    "Please enter a file name: "
    "File not found. Please enter a valid file name: "
    "Enter region code ('quit' to terminate): "
    "Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: "
    "Enter region code ('quit' to terminate): "
    "Error with the region key! Try another region"
    
    
    
    
    
    
    
    
    
    '''
    Hints and Suggestions
    a) Dictionaries can contain other elements like float, list, and even other dictionaries. How
    to access a dictionary with multiple keys? Just like any other dictionary:
    Dictionary = {‘KeyA’ :{ ‘Key1’: value_list1, ‘Key2’: value_list2}}
    Dictionary[KeyA][Key2] would give value_list2
    b) Dictionaries, just like lists, are not always sorted. One way to sort a dictionary is by
    having a sorted list of keys. To get the list of keys on a dictionary, use the keys()
    function.
    c) Entering a non-existing or incorrect region can be a very troublesome error! Python has
    a way to try these conditions and avoid such errors.'''