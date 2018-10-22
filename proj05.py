'''Computer Project #5
    Prompt user for a file to be analyzed
    pass through first 2 lines of code
    print headers
    for loop used to find continent names
        embedded for loop to find change
            embedded if loop to find max change alng with year
        if loop to find max change of all continents.
        print with format
'''

def open_file():
    '''Returns fp to the file. Opened by asking user for the file name.
    Error checking required, keep prompting until a valid file is entered.'''
    while True:
        #continually prompts user until correct file name given
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

def main():
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
        #print(continent)
        maxdelta = 0

        #this loop calculates each of the deltas (there are 6 deltas)
        for i in range(6): #range is 6 because 6 deltas i is the column
            #starting at the end of the name to end of range plus 1 (=6 total)
            change = calc_delta(line,i+1) #column i+1 b/c column i0 are names
            
            #comparing to maxdelta to delta
            if change >= maxdelta:
                maxdelta = change 
                
                #keep track of the year using same column pulled for the delta
                year = years[15+6*(i):15+6*(i+1)]
                year = int(year) + 50
                
        delta = maxdelta
        
        if maxdelta >= maxmaxdelta:
            maxmaxdelta = maxdelta
            maxcontinent = continent
            maxyear = year
    
        #display the formatted output by calling the display functions
        print(format_display_line(continent,year,delta))
        
    #display formatted outpuf for max of max
    print("\n"+"Maximum of all continents:"+"\n"+format_display_linemax(maxcontinent, maxyear, maxmaxdelta))
    

if __name__ == "__main__":
    main()