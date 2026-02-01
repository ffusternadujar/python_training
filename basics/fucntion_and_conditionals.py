def weather_condition(temperature : float) -> str:
  if temperature > 7:
    return "Warm"
  else:
    return "Cold"
  

user_input = input("Enter the temperature: ")
print(weather_condition(float(user_input)))
