''' open files, reprompting until correct file is input and redefine
    call read_file_2016 using the first opened file and redefine
    call read_file_2000 using the second opened file and redefine
    print out the desired title formats
    print out the data with the list locations taken from the redefined read_file_2016 function
    
    read_file_2016 will read for certain headers and will take the values under each
    it will also calculate totals and ratios and returned as a sorted list of tuples
    
    print out the formatted dashed lines      
    take values from calc totals and divide to find totals for the 2016 data and print formatted
    take values from calc totals and divide to find totals for the 2000 data and print formatted
    
    calc totals will take the sorted list of 2016 data returned from the read_2016_file 
    function and returns one tuple
   
    for plotting will prompt user for "yes" in an if loop
        will define the values needed for make lists for plot function
        make a variable to use the data from the make lists for plot function
        
        make lists for plot function will takes integers as arguments and return a tuple of three lists
        
        take the values from make lists for plot and then enter into plot data function
        
        plot data function will plot the three lists as bar graphs
'''

import pylab   # for plotting
from operator import itemgetter  # useful for sorting

def open_file():
    '''Returns file pointer to file opened by asking user for the filename. 
    Error checking is required. First fine 2016 then 2000'''
    while True:
        #continually prompts user until correct file name given
        try:  
            usefile = input("Enter a file name: ")
            fp = open(usefile, 'r')
            return fp
        except FileNotFoundError:
            print("Error. Please try again.")

def find_index(header_lst,s):
    '''header_lst is the header row split into a list of strings. 
    s is a string. 
    Returns the index (int) of the string s in the header row list. 
    This index is the column index of the string in the data file.'''
    for i,ch in enumerate(header_lst):
        if ch == s:
            return i

def read_2016_file(fp):
    '''returns sorted list of tuples of data from file. 
    Tuples are sorted on the last item in the tuples from smallest to largest. 
    %'s with respect to tot residents, i.e. native + naturalized + non-citizen. 
    
    The values are to be found using the string value—
    pass that string to the find_index function which returns the column index 
    (this allows us to get the right data out of different files). 
    
    Each tuple has six items in this order:
i. state (str) found at column index 2
ii. count of native-born residents (int) found in column EST_VC197
iii. count of naturalized citizens (int) found in column EST_VC201
iv. ratio of naturalized citizens to total residents (float)
v. count of non-citizens (int) found in column EST_VC211
vi. ratio of non-citizens to total residents (float)'''
    ls = []
    headers=fp.readline().split(',')
    fp.readline()
    for x in fp:
        x=x.split(",")
        
        state = x[2] #state (str) found at column index 2
        
        #this is just the index
        ct_native = find_index(headers,"EST_VC197") 
        #count of native-born residents (int) found in column EST_VC197
        oct_native = int(x[ct_native])
        
        #this is just the index
        ct_naturalized = find_index(headers, "EST_VC201")
        #count of naturalized citizens (int) found in column EST_VC201        
        o_ct_natural = int(x[ct_naturalized])
        
        #this is just the index
        ct_non_citizens = find_index(headers, "EST_VC211")
        #count of non-citizens (int) found in column EST_VC211
        o_ct_non_cit = int(x[ct_non_citizens])
        
        totpeople=int(oct_native)+int(o_ct_natural)+int(o_ct_non_cit)

        #ratio of naturalized citizens to total residents (float)
        rto_naural_tot=int(o_ct_natural)/int(totpeople)

        #ratio of naturalized citizens to total residents (float)
        rto_non_cit_tot=int(o_ct_non_cit)/int(totpeople)

        tup=(state,oct_native,o_ct_natural,rto_naural_tot,o_ct_non_cit,rto_non_cit_tot)
        ls.append(tup)

    #5 bc it is sorting by last index (ratio non-citizens to total residents)
    return sorted(ls,key=itemgetter(5))

def read_2000_file(fp2):
    '''Takes a file pointer as an argument. 
    Returns one tuple of values in this order:
i. total population (int) found in column HC01_VC02
ii. count of native-born residents (int) found in column HC01_VC03
iii. count of naturalized citizens (int) found in column HC01_VC05
iv. count of non-citizens (int) found in column HC01_VC06'''
    #pop_total = 
    headers=fp2.readline().split(',')
    fp2.readline()
    for x in fp2:
        x=x.split(",")
        
        #this is just the index
        tot_pop = find_index(headers,"HC01_VC02") 
        #total population (int) found in column HC01_VC02
        o_tot_pop = int(x[tot_pop])
        
        #this is just the index
        ct_native = find_index(headers, "HC01_VC03")
        #count of native-born residents (int) found in column HC01_VC03        
        o_ct_native = int(x[ct_native])
        
        #this is just the index
        ct_natural = find_index(headers, "HC01_VC05")
        #count of naturalized citizens (int) found in column HC01_VC05
        o_ct_natural = int(x[ct_natural])
        
        #this is just the index
        ct_non_citizens = find_index(headers, "HC01_VC06")
        #count of non-citizens (int) found in column HC01_VC06
        o_ct_non_citizens = int(x[ct_non_citizens])
        
        tup = (o_tot_pop, o_ct_native, o_ct_natural, o_ct_non_citizens)
    return tup

def calc_totals(data_sorted):
    '''Takes the sorted list of 2016 data returned from the read_2016_file 
    function and returns one tuple of values in this order:
i. total count of native-born residents (int)
ii. total count of naturalized citizens (int)
iii. total count of non-citizens (int)
iv. total residents, i.e. the sum of native_born + naturalized + non-native'''
    #value in data sorted at a particular list location
    ct_native = sum([x[1] for x in data_sorted])
    ct_natural = sum([x[2] for x in data_sorted])
    ct_non_citizens = sum([x[4] for x in data_sorted])
    #adding for total pop
    tot_pop = int(ct_native) + int(ct_natural) + int(ct_non_citizens)
    tup = (ct_native, ct_natural, ct_non_citizens, tot_pop)
    return tup

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):
    '''Takes six integers as arguments and returns one tuple of three lists: 
    in this order. 
i. [ native_2000, native_2016]
ii. [ naturalized_2000, naturalized_2016]
iii. [ non_citizen_2000, non_citizen_2016]'''
    list1 = [ native_2000, native_2016]
    list2 = [ naturalized_2000, naturalized_2016]
    list3 = [ non_citizen_2000, non_citizen_2016]
    tup_of_lists = (list1, list2, list3)
    return tup_of_lists
    
def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.
    pass the correct lists for native, naturalized and non-citizens.
    There should be 2 entries in each list corresponding to native, 
    naturalized, and non-citizen counts for the years 2000 and 2016.'''

    X = pylab.arange(2)   # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color and a label
    pylab.bar(X, native_list, color = 'b', width = 0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color = 'g', width = 0.25, label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color = 'r', width = 0.25,label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000","2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    #pylab.savefig("plot.png")

def main():    
    '''Takes no input. Returns nothing. Call the functions from here. 
    Only call plot_data if the prompt returns “yes”.'''
    #open files for the functions
    file, file2 = open_file(), open_file() 
    #call functions
    sorted_tup = read_2016_file(file)
    sorted_tup2 = read_2000_file(file2)
    #title
    print('{:^112s}'.format("2016 Population: Native, Naturalized, Non-Citizen"))
    print("")
    print('{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}'.format("State","Native","Naturalized","Percent Naturalized","Non-Citizen","Percent Non-Citizen"))

    #data with the list locations taken from sorted_tup
    for x in sorted_tup:
        print("{:<20s}{:>15,d}{:>17,d}{:>22.1%}{:>16,d}{:>22.1%}".format(x[0],x[1],x[2],x[3],x[4],x[5]))
        
    #dashed lines
    print("-"*112)
    
    #take values from calc totals and divide to find totals
    usevalues = calc_totals(sorted_tup)
    p2016percent1 = usevalues[1] / usevalues[3]
    p2016percent2 = usevalues[2] / usevalues[3]
    #printing with the found locations from the usevalues and calculated totals
    print("{:<20s}{:>15,d}{:>17,d}{:>22.1%}{:>16,d}{:>22.1%}".format("Total 2016", usevalues[0], usevalues[1], p2016percent1, usevalues[2], p2016percent2))
    
    #take values from calc totals and divide to find totals
    p2000percent1 = sorted_tup2[2] / sorted_tup2[0]
    p2000percent2 = sorted_tup2[3] / sorted_tup2[0]
    #printing with the found locations from the sorted tup 2 and calculated totals
    print("{:<20s}{:>15,d}{:>17,d}{:>22.1%}{:>16,d}{:>22.1%}".format("Total 2000", sorted_tup2[1], sorted_tup2[2], p2000percent1, sorted_tup2[3], p2000percent2))
    
    #if plot is desired
    to_plot = input("Do you want to plot? ")
    if to_plot == "yes":
        
        #values needed for make lists for plot function
        native_2000 = sorted_tup2[1]
        naturalized_2000 = sorted_tup2[2]
        non_citizen_2000 = sorted_tup2[3]
        native_2016 = usevalues[0]
        naturalized_2016 = usevalues[1]
        non_citizen_2016 = usevalues[2]
        
        enter_into_plot = make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016)
        #values from make lists for plot that will be used for plot data
        native_list = enter_into_plot[0]
        naturalized_list = enter_into_plot[1]
        non_citizen_list = enter_into_plot[2]
        plot_data(native_list, naturalized_list, non_citizen_list)
        
if __name__ == "__main__":
    main()