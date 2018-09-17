#Computer Project #1
#use input and print with math conversions
Rod = float(input('Input rods: '))
print('You input', float(Rod), 'rods.')

#Conversions
Meters = Rod*5.0292 #1 rod=5.0292 meters
Feet = Meters/0.3048 #1 foot=.3048 meters
Miles = Meters/1609.34 #1 mile= 1609.34 meters
Furlongs = Rod/40 #1 furlong= 40 rods
Minutes = Miles/3.1*60 #avg walking speed = 3.1 mi/hr
 
#Print
print('Conversions')
print('Meters:', round(Meters,3))
print('Feet:', round(Feet,3))
print('Miles:', round(Miles,3))
print('Furlongs:', round(Furlongs,3))
print('Minutes to walk', float(Rod), 'rods:', round(Minutes,3))

#dean uses this for debugging - it will tell what kind of value it is
print(type(Rod))