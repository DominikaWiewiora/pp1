#converting celsius to Kelvin and Fahrenheit
#reading temperature in Celsius
Celsius=float(input('Temperature in Celsius: \n'))
#calculating to Kelvin
Kelvin=Celsius+273.15
#calculating to Fahrenheit
Fahrenheit=(Celsius*9/5)+32
#displaying results
print(f'temperature in Kelvin: {Kelvin}, temperature in Fahrenheit: {Fahrenheit}')