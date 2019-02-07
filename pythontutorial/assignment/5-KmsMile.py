# Collect input from the user
kilometers = float(input('How many kilometers?: '))
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))