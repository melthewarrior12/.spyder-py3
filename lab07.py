def open_file():
    while True:
        try:
            usefile = input("Enter a file name:")
            fp = open(usefile,'r')
            return fp
        except FileNotFoundError:
            print("Error file not found")
def format_display(i,lst_count):
       #     for i in range(1,10):
    percent0 = float((int(lst[i]) / int(lst_count)))   
    n = i+1
    strr = str(n) + ":"       
    lst_benford = ['(30.1%)','(17.6%)','(12.5%)','( 9.7%)','( 7.9%)','( 6.7%)','( 5.8%)','( 5.1%)','( 4.6%)']     
    return('{:>5s}{:>7.1%} {:4s}'.format(strr,percent0,lst_benford[i]))
    
    
lst =[0,0,0,0,0,0,0,0,0]
fp = open_file()

for index in fp:
    index = index.strip()
    num = int(index[0])
        
    if num == 1:       
        lst[0] += 1
    if num == 2:       
        lst[1] += 1
    if num == 3:        
        lst[2] += 1
    if num == 4:       
        lst[3] +=1
    if num == 5:
        lst[4] += 1
    if  num == 6:
        lst[5] += 1
    if num == 7:
        lst[6] += 1
    if num == 8:
        lst[7] += 1
    if num == 9:
        lst[8] += 1
            
    lst_count = sum(lst)
    i = index
   
print('Digit Percent Benford')
for i in range(0,9):
    print(format_display(i,lst_count))
    
#print(lst_count)
#print(lst)