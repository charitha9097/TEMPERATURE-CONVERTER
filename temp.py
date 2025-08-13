def convert_temperature(temp, unit):
   if unit.upper() == 'F': # Fahrenheit to Celsius 
      converted = (temp - 32) * 5 / 9
   elif unit.upper() == 'C': # Celsius to Fahrenheit 
      converted = (temp * 9 / 5) + 32
   else:
      return "Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius."
   return round(converted, 2)

#Example usage
temperature = float(input("Enter temperature: "))
unit = input("Enter unit (F for Fahrenheit, C for Celsius): ")
result = convert_temperature(temperature, unit) 
print("Converted temperature:", result)
