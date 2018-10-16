'''Put overall header comments here.'''

def open_file():
    '''Returns fp to the file. Opened by asking user for the file name.
    Error checking required, keep prompting until a valid file is entered.'''
    while True:
        try:  
            usefile = input("Enter a file name: \n")
            fp = open(usefile, 'r')
            return fp
        except FileNotFoundError:
            print("Error. Please try again.")

def print_headers():
    '''Print the headers for the output'''
    print("     Maximum Population Change by Continent")
    print("      ")
    print("Continent                     Years     Delta")
    

def calc_delta(line,col):
    '''Takes one line of data from the data file as an argument
    along with a column index (int) in the line (where the continent’s name is
    “column 0”, the first data value is in “column 1”, etc.).
    
    Examines successive columns to determine percent change. 
    Continent name is in a 15-character wide field.
    Each value is in a 6-character wide field.
    Returns change as a float.'''

    #col is column
    #start at 15 because before index 15 it is continent name
    #col -1 b/c start before the number and col because ending after number
    number1 = line[15+6*(col-1):15+6*(col)]
    number2 = line[15+6*(col):15+6*(col+1)]
    number1=float(number1)
    number2=float(number2)
    change = ((number2) - (number1))/(number1)
    
    return change

def format_display_line(continent,year,delta):
    '''Takes continent name (str), year (int), change (float). 
    Returns formatted string.
    Continent field 26 characters left justified,
    year and its predecessor (year-50) printed w/ hyphen 
    change displayed as a percent.'''
    
    last = int(year) - 50
    yearst = str(last) + "-" + str(year)
    percent = (delta * 100)
    percent = int(round(percent))
    percent = str(percent) + "%"
    
    return("{:<26s}{}{:>10s}".format(continent,yearst,percent))

def format_display_linemax(continent, maxyear, maxmaxdelta):
    '''Takes continent name (str), year (int), change (float). 
    Returns formatted string.
    Continent field 26 characters left justified,
    year and its predecessor (year-50) printed w/ hyphen 
    change displayed as a percent.'''
    
    last = int(maxyear) - 50
    yearst = str(last) + "-" + str(maxyear)
    percent = (maxmaxdelta * 100)
    percent = int(round(percent))
    percent = str(percent) + "%"
    
    return("{:<26s}{}{:>10s}".format(continent,yearst,percent))

def main(): ## should only be about this long 
    '''Take no input, return nothing, call functions. Close file here.'''


   #Prompt user for a file to be analyzed
    fp = open_file() #runs the function to prompt for 
    
    #to get rid of the useless first line
    fp.readline()
    
    #the first line that actually has data we need
    years = fp.readline()
    
    print_headers()
    
    maxmaxdelta = 0
    
    #this loop will give the first column (the names)
    for line in fp:
        #name is the name of the continent
        continent = line[:15].strip()
        print(continent)
        maxdelta = 0
        #columnyear = 0
        #this loop calculates each of the deltas (there are 6 deltas)
        for i in range(6): #range is 6 because 6 deltas i is the column
            #change = to the function called starting at the end of the name to end of range plus 1 (=6 total)
            change = calc_delta(line,i+1) #starts at column 1+1 because column i0 is the names
            #delta = int(round(delta))
            #comparing to maxdelta to delta
            if change >= maxdelta:
                maxdelta = change 
                #one is added each time a new max is found but will be behinf if no new year is found
                #year=1750+(50*c_number)
                #should keep track of the year by using the same column pulled for the delta
                year = years[15+6*(i):15+6*(i+1)]
                year = int(year) + 50
                # need to keep track of the year the delta happened (or the i? reassign the years as well 
                #KEEP TRACK OF TIME WILL WILL BE DONE SIMILARLY TO THE WAY WE USED THE COLUMNS IN THE CALCDELTA FUNCTION
            #logic for max delta


        print(year)    
        print(maxdelta)#in the right place to print?
        #this might break everything but the format function needs it?
        ########################################################delta = maxdelta
        #################delta = maxdelta
        
        if maxdelta >= maxmaxdelta:
            maxmaxdelta = maxdelta
            #probably wrong
            ####################################################maxyear = year
    
    #print("outoutofloop", year)    
    #print("maxdeltaoutoutofloop", maxdelta)
    #TESTING
    #print("together", str(year) + "-" + str(int(year) + 50))
    #print(maxdelta)
    
    ##print headers
    #print_headers()
    
    
    ###display the formatted output by calling the display functions
    #####################################format_display_line(continent,year,delta)
    #need these inputs

    print("Maximum of all continents:      ")
    #######################format_display_linemax(continent, maxyear, maxmaxdelta)

if __name__ == "__main__":
    main()
    
    
  


'''    
    start = 0 # starting number is located at 0
    for ch in fp: #for each character in a line from file
        numbers = ch[15:] #.strip() # where the numbers begin
    for i in range (7): # wants just the index for the number location
        first = i[start:start+6] #start at 0 and end at 0+6 <-- used to find only the numbers
        print(first)
        start += 6 #instead of printing the very first number it will now print the next number when it loops around
    return numbers, first'''
    
'''#first number in set until 6 index over #####should it be changed by the value i+6?
    number1 = i[15:21].strip()
    #second number in set from first number end until 6 over #####should it be changed by the value i+6?
    number2 = i[21:27].strip()
    change = (int(number2) - int(number1))/ int(number1)
    #should be able to round the change
    change = ("%.2f" % change)
    #####now change for the next value loop'''

'''
    for i in range(6):
        #first number in set until 6 index over #####should it be changed by the value i+6?
        number1 = i[15:21].strip()
        #second number in set from first number end until 6 over #####should it be changed by the value i+6?
        number2 = i[21:27].strip()
        change = (int(number2) - int(number1))/ int(number1)
        #should be able to round the change
        change = ("%.2f" % change)
        #####now change for the next value loop
        ###logic for max of max deltas
        '''
'''   
(Hint: I developed the slice values by writing a short program that had a string that was
one line of the file and then I looped through the string using slicing to print the pairs of
values, e.g. for Africa I printed 106 & 107, 107 & 111, 111 & 133, etc. Once I could do
that, I knew that I could slice out the desired values and then the rest was easy.)'''

 
'''
    start = 0 # starting number is located at 0
    for ch in fp: #for each character in a line from file
        numbers = ch[15:] #.strip() # where the numbers begin
    for i in range (7): # wants just the index for the number location
        first = i[start:start+6] #start at 0 and end at 0+6 <-- used to find only the numbers
        print(first)
        start += 6 #instead of printing the very first number it will now print the next number when it loops around
    return numbers, first'''
        
'''   
    numbers = "" ######################################## note from teacher
    numbers = str()
    numbers = line[15:] #numbers are where the numbers begin
    print(numbers)
    start = 0 #starting number is located at 0
    for i in range (7): # wants just the 6 index for the number location
        first = numbers[start:start+6] #start at 0 and end at 0+6 <-- used to find only the numbers
        print(first)
        start += 6 #instead of printing the very first number it will now print the next number when it loops around
    return name, numbers, first
    
    change = (line + i+1)/ (line) # not even close'''
    
'''
    calc_delta is supposed to calculate one value at a time only. 
    need a nested loop in you main function. 
    outer loop goes through each line in the file and the inner loop is range(6),
    that is because each line has 6 deltas.
    The the inner loop will give you your column.
    And that way you can find the maximum delta for each line. 
    And also the maximum delta for the entire file.'''
    
''' 
"Enter a file name: "
"Error. Please try again."
"Maximum Population Change by Continent\n"
"{:<26s}{:>9s}{:>10s}".format("Continent","Years","Delta")
"\nMaximum of all continents:"

'''



'''
a) Initialize the maximum to be a small number, e.g. zero. This is usually done before a loop.
b) If a new value is greater than the existing maximum, assign maximum to be the new value.
Also, you may want to update associated values, e.g the year of the new maximum.
3) Items 1-9 of the Coding Standard will be enforced for this project.
4) We provide a proj05.py program for you to start with.
5) Use of advanced data structures such as list, sets, and dictionaries is prohibited.

'''