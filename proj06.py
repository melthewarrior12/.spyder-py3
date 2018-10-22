#source code header?



import pylab   # for plotting
from operator import itemgetter  # useful for sorting

def open_file():
    '''Returns file pointer to file opened by asking user for the filename. 
    Error checking is required. First fine 2016 then 2000'''
    while True:
        #continually prompts user until correct file name given
        try:  
            usefile = input("Enter a file name: \n")
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
        
        state_str = x[2] #state (str) found at column index 2
        
        #this is just the index
        ct_native = find_index(headers,"EST_VC197") 
        #count of native-born residents (int) found in column EST_VC197
        o_ct_native = int(x[ct_native])
        
        #this is just the index
        ct_naturalized = find_index(headers, "EST_VC201")
        #count of naturalized citizens (int) found in column EST_VC201        
        o_ct_naturalized = int(x[ct_naturalized])
        
        #this is just the index
        ct_non_citizens = find_index(headers, "EST_VC211")
        #count of non-citizens (int) found in column EST_VC211
        o_ct_non_citizens = int(x[ct_non_citizens])
        
        totpeople=int(o_ct_native)+int(o_ct_naturalized)+int(o_ct_non_citizens)

        #ratio of naturalized citizens to total residents (float)
        rto_nauralized_tot_fl=int(o_ct_naturalized)/int(totpeople)

        #ratio of naturalized citizens to total residents (float)
        rto_non_citizens_tot_residents_fl=int(o_ct_non_citizens)/int(totpeople)

        tup = (state_str, o_ct_native, o_ct_naturalized, rto_nauralized_tot_fl, o_ct_non_citizens, rto_non_citizens_tot_residents_fl)
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

    #probably need to officially take from the actual function but this should work for now
    sorted_tup = [('Alabama', 4699671, 163629, 0.03294111631266611, 104018, 0.02094047532290061), ('Alaska', 684530, 57364, 0.07484024496207367, 24592, 0.032084082422901394)]
    
    ct_native = sum([x[1] for x in sorted_tup])
    ct_natural = sum([x[2] for x in sorted_tup])
    ct_non_citizens = sum([x[4] for x in sorted_tup])
    tot_pop = int(ct_native) + int(ct_natural) + int(ct_non_citizens)
    tup = (ct_native, ct_natural, ct_non_citizens, tot_pop)
    return tup

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):
    '''Takes six integers as arguments and returns one tuple of three lists, 
    in this order. 
    (This is a trivial function to ensure your data is organized for plotting.)
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
    This function is written for you. 
    just have to pass the correct lists for native, naturalized and non-citizens.
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
    open_file(), open_file()
    #print("                               2016 Population: Native, Naturalized, Non-Citizen                                \n")
    print('{:31s}'.format("2016 Population: Native, Naturalized, Non-Citizen"))
    print('{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}'.format("State","Native","Naturalized","Percent Naturalized","Non-Citizen","Percent Non-Citizen"))
    #find_index(header_lst,s)
    #read_2016_file(fp)
    '''I noticed we need to print all of those data inside the file of 2016 that each list have six elements are included, but as a matter of fact, the function used to calculate the total residence, total noncitizens, total  native, etc... that only include four elements in it tuple.    If this calc_total function designed to store only four elements, is that mean we have to finish the extra calculation : rate of neutralized in total_residence and rrate of non_native over total_residence in the main function?
    the ratio calculations should be done within the main() function. '''
    
    '''
    At program start prompt the user for the files to be analyzed: year 2016 first, then year 2000.
     
    The format string for the table header is:
    {:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}
    ''' 
    
    
                               
    
    31
    
    print("----------------------------------------------------------------------------------------------------------------")
    to_plot = input("Do you want to plot? ")
    if to_plot == "yes":
        plot_data(native_list, naturalized_list, non_citizen_list)
        
if __name__ == "__main__":
    main()
    
    

    
    





'''

"2016 Population: Native, Naturalized, Non-Citizen"
("State","Native","Naturalized","Percent Naturalized", "Non-Citizen","Percent Non-Citizen")
"="*112
"Do you want to plot? "
'''