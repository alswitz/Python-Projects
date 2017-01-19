#Python Recipe Converter
#Version 1.0
#By Alexander Switzer

#input, storing the inputs as float values to save time further down the line
#since they all will potentially have decimals in them.
print ("-- Original Recipe --")
flour_c = float(raw_input("Enter the amount of flower (cups): "))
water_c = float(raw_input("Enter the amount of water (cups): "))
salt_c = float(raw_input("Enter the amount of salt (teaspoons): "))
yeast_c = float(raw_input("Enter the amount of salt (teaspoons): "))
factor = float(raw_input("Enter the loaf adjustment factor (e.g. 2.0 double the size): "))

#Variables and math
flour_m = flour_c * factor
water_m = water_c * factor
salt_m = salt_c * factor
yeast_m = yeast_c * factor

#Bonuses
cup_g_flour         = int(120)  * flour_m
cup_g_water         = float(236.59) * water_m
teaspoon_g_salt     = float(5.69) * salt_m
teaspoon_g_yeast    = float(3.15) * yeast_m

#Outputs
print ("\n-- Modified Recipe --")
print flour_m
print water_m
print salt_m
print yeast_m

print ("\n-- Modified Recipe in Grams --")
print cup_g_flour
print cup_g_water
print teaspoon_g_salt
print teaspoon_g_yeast
