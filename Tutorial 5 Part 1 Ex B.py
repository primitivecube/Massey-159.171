# Use nested loops and these lists to print the following pairs of strings as output:
# nuts = ["Peanut", "Walnut", "Almond", "Pecan"]
# products = ["Butter", "Cake", "Praline", "Pie"]
# Peanut Butter
# Peanut Cake
# Peanut Praline
# Peanut Pie
# Walnut Butter
# Walnut Cake
# Walnut Praline
# Walnut Pie
# Almond Butter
# Almond Cake
# Almond Praline
# Almond Pie
# Pecan Butter
# Pecan Cake
# Pecan Praline
# Pecan Pie

nuts = ["Peanut", "Walnut", "Almond", "Pecan"]
products = ["Butter", "Cake", "Praline", "Pie"]
for nut in nuts:
    for product in products:
        print (nut, product)
