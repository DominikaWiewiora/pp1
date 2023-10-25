bmi_calculation = lambda kg, cm: kg / ((cm / 100) ** 2)
x = bmi_calculation(81, 182)
print(f"Peter's BMI is {x}")