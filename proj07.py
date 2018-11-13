'''Project 07 TSA Claims Data
prompts user for file
uses the returned file pointer within read_file function.
    use checkfunction within readfile function.
        usefunction makes sure the data is complete for each line used.
    readfile reads the file and returns complete data stripped and clean of 
    unwanted characters. Formated into a list of tuples.
take returned data from read file and use it for process_data function.
    Total, Average, Max_claim, Max_claim_airport, and 3 lists returned as tuple
take returned data from process_data and use for display_data function.
    formats the data and includes headers
prompt for plot and if "yes" use plot_data function.
'''

import pylab   # needed for plotting

STATUS = ['Approved','Denied','Settled'] 

def open_file():    
    '''Returns file pointer to the file opened by asking user for file name.'''
    
    #prompts user for file name
    file_inputed = input("Please enter a file name: ")
    while True:
        try:
            return open(file_inputed)
        except FileNotFoundError:
            file_inputed = input("File not found. Please enter a valid file name: ")
     
def checkfunction(fixedline):
    '''checks that each desired column from each line has no blank data'''
    if fixedline[1] == "":
        return "skip"
    if fixedline[4] == "":
        return "skip"
    if fixedline[9] == "":
        return "skip"
    if fixedline[10] == "":
        return "skip"
    if fixedline[11] == "":
        return "skip"
    else: 
        return fixedline
    
def read_file(fp):
    '''Takes file pointer as an argument and returns a list of tuples of data. 
    Makes sure data in each column (1, 4, 9, 10, 11) exists each row. 
    If any of that data is missing in a row, that row is ignored 
    Years other than 2002 to 2009 are ignored. 
    Only contains data from columns (1, 4, 9, 10, 11), in that order, 
    '''

    lsoftup = []
    #skips the line with the headers
    fp.readline()
    for line in fp:
         # line will become a list of strings.
        fixedline = line.strip().split(",")
         #run function check to be sure no blank data is used
        if checkfunction(fixedline) == "skip":
                continue
        #date is within range 02 - 09
        if int(fixedline[1][-2:]) in range(2,10):
            #date without whitespace
            date = fixedline[1].strip()
            #airport name without whitespace
            airport_name = fixedline[4].strip()
            #claim amount without $ and no ; when above 1000
            claim_amount = fixedline[9].strip().replace("$", "").replace(";","")
            #status without whitespace
            status = fixedline[10].strip()
            #claim amount without $ and no ; when above 1000
            closed_amount = fixedline[11].strip().replace("$", "").replace(";","")
            
            #change amounts to floats
            claim_amount = float(claim_amount)
            closed_amount = float(closed_amount)
            
            tup = (date, airport_name, claim_amount, status, closed_amount)
            lsoftup.append(tup)
        
    return lsoftup
    
def process(data):
    '''Takes data from read_data function as an argument. Calculates:
    Total: total number of applications that are approved, settled, or denied.
    Average: average close amount, but only for non-zero close amounts in 
    approved or settled applications (not denied).
    Max_claim: The largest claim amount (it is amazingly big!)
    Max_claim_airport: The aiport that had the largest claim amount
    Create three lists:
    
i. List1: total cases (approved + settled + denied) for years from 2002-2009.
ii. List2: total settled + approved cases for each year from 2002 to 2009
iii. List3: total denied cases for each year from 2002 to 2009
Returns tuple: (List1,List2,List3,Total,Average,Max_claim,Max_claim_airport)'''
    
    #initialize values
    Total = 0
    Total2 = 0
    Max_claim = 0
    Max_claim_airport = 0
    Average = 0
    List1 = [0,0,0,0,0,0,0,0]
    List2 = [0,0,0,0,0,0,0,0]
    List3 = [0,0,0,0,0,0,0,0]
    for cell in data:
        #List1: total cases (approved + settled + denied) from 2002 to 2009.
        if cell[3]== "Approved" or cell[3]== "Settled" or cell[3]== "Denied":
            
            Total += 1
            #year = last 2 characters of the date
            year = int(cell[0][-2:])
            List1[year - 2] += 1
        
        #List2: total settled + approved cases for each year from 2002 to 2009
        if  int(cell[0][-2:]) in range(2,10) and (cell[3]== "Approved" or \
               cell[3]== "Settled"):
            
            Average += cell[4] #sum(cell[4] for cell in data)
            List2[year - 2] += 1 
        
        #total amount but not including when the value is 0    
        if  int(cell[0][-2:]) in range(2,10) and (cell[3]== "Approved" or \
               cell[3]== "Settled") and cell[4] != 0:
             
            Total2 += 1           

        #List3: total denied cases for each year from 2002 to 2009
        if cell[3]== "Denied":
            #year = last character of the date
            year = int(cell[0][-1])
            List3[year - 2 ] += 1 

        #max claim and max claim airport
        if int(cell[2]) >= Max_claim:
            #redefine the max claim and what airport it is from
            Max_claim = cell[2]
            Max_claim_airport = cell[1]

    Average = Average / Total2
    
    return (List1,List2,List3,int(Total),Average,Max_claim,Max_claim_airport)

def display_data(tup):
    '''Takes the tuple of data calculated in the process function.
    Returns nothing.'''
    #header title
    print("TSA Claims Data: 2002 - 2009")
    
    print("")
    
    #N is total of all cases from 2002 to 2009
    print("N = {:<10,d}".format(tup[3]))
    
    print("")
    
    #header years
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}"\
          .format(" ",'2002','2003','2004','2005','2006','2007','2008','2009'))
    
    #data from tupled returned from process(data)
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}"\
          .format("Total",tup[0][0],tup[0][1],tup[0][2],tup[0][3],tup[0][4],\
                  tup[0][5],tup[0][6],tup[0][7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}"\
          .format("Settled",tup[1][0],tup[1][1],tup[1][2],tup[1][3],tup[1][4],\
          tup[1][5],tup[1][6],tup[1][7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}"\
          .format("Denied",tup[2][0],tup[2][1],tup[2][2],tup[2][3],tup[2][4],\
          tup[2][5],tup[2][6],tup[2][7]))
    
    print("")
    print("Average settlement: ${:<10.2f}".format(tup[4]))
    print("The maximum claim was ${:>,.2f} at {} Airport".format(tup[5], tup[6]))
    
def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs. 
    Pass through the correct data from main'''

    X = pylab.arange(8)   # create 8 items to hold the data for graphing
    #assign each list's values to 8 items graphed, includes color and label
    pylab.bar(X, accepted_data, color = 'b', width = 0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color = 'g', width = 0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color = 'r', width = 0.25,label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2002","2003","2004","2005","2006","2007",\
                                "2008","2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")
    
def main():
    '''Takes no input. Returns nothing. Call the functions from here.'''
    fp = open_file()
    data = read_file(fp)
    tup = process(data)
    display_data(tup)
    
    #data taken from the process(data) funtion
    accepted_data = tup[0]
    settled_data = tup[1]
    denied_data = tup[2]

    toplot = input("Plot data (yes/no): ")
    if toplot == "yes":
        plot_data(accepted_data, settled_data, denied_data)


if __name__ == "__main__":
    main()