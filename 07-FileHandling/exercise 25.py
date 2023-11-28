import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall(r'\d+\.?\d*', message)
temperatures = [int(temp) for temp in temperatures]
average_temperature = sum(temperatures) / len(temperatures)
print(f"The extracted temperatures: {temperatures}")
print(f"The average temperature: {average_temperature:.2f}C")