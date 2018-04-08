def bmi_calc():
    """Calculates BMI by requesting input for kg and height, then prints the result and a graded string"""
    kg = float(input("Enter your weight in kilograms: "))
    m = float(input("Enter your height in meters: "))
    bmi = kg / (m ** 2) # this is the formula for BMI
    grade = "" # this is a place holder for the grade string, which is determined by the if-else test
    if 18.5 <= bmi and bmi <= 25.0:
        grade = ". This is within the healthy range." # The full stop comes first, as this string is intended as the final print statement
    else:
        grade = ". This is outside the healthy range."
    string = "Your BMI is" # This is the first string statement in the print function
    print (string, bmi, grade)

bmi_calc() # no arguments are required for the function, because they are based on input calls within the function


