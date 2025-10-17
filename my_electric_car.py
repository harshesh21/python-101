from car import ElectricCar
#If you need to import a module from the standard library and a module that you wrote, 
# place the import statement for the standard library module first.
# Then add a blank line and the import statement for the module you wrote. 

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()