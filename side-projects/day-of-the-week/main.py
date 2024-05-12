def main():

  import requests
  from datetime import datetime, timedelta

  def get_weather_forecast(city, api_key):
      url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
      response = requests.get(url)
      data = response.json()
      return data

  def main():
      # Ask the user for the day of the week
      day = input("Please enter a day of the week: ").lower()

      # Depending on the day, ask a specific question
      if day == "monday":
          question = "What is your plan for the week ahead?"
      elif day == "tuesday":
          question = "What tasks do you have scheduled for today?"
      elif day == "wednesday":
          question = "How is your week going so far?"
      elif day == "thursday":
          question = "Any plans for the upcoming weekend?"
      elif day == "friday":
          question = "How are you wrapping up your week?"
      elif day == "saturday":
          question = "What are your plans for the weekend?"
      elif day == "sunday":
          question = "How are you preparing for the week ahead?"
      else:
          print("Sorry, I don't recognize that day.")
          return

      print(question)

      # Get the weather forecast for the specified city
      city = input("Enter the name of the city: ")
      api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap

      data = get_weather_forecast(city, api_key)

      if "list" in data:
          for item in data["list"]:
              # Extract the date and temperature for the specified day
              date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
              date_str = date.strftime("%A").lower()
              if date_str == day:
                  temp = item["main"]["temp"]
                  description = item["weather"][0]["description"]
                  print(f"The weather forecast for {day.capitalize()} in {city} is {temp}°C with {description}.")
                  break
      else:
          print("Unable to retrieve weather forecast.")

    
    # day = input("Please enter a day of the week: ").lower()
    # if day == "monday":
    #     print("What is your plan for the week ahead?")
    # elif day == "tuesday":
    #     print("What tasks do you have scheduled for today?")
    # elif day == "wednesday":
    #     print("How is your week going so far?")
    # elif day == "thursday":
    #     print("Any plans for the upcoming weekend?")
    # elif day == "friday":
    #     print("How are you wrapping up your week?")
    # elif day == "saturday":
    #     print("What are your plans for the weekend?")
    # elif day == "sunday":
    #     print("How are you preparing for the week ahead?")
    # else:
    #     print("Sorry, I don't recognize that day.")


# import requests
# from datetime import datetime, timedelta

# def get_weather_forecast(city, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
#     return data

# def main():
#     city = input("Enter the name of the city: ")
#     api_key = "YOUR_API_KEY"  

#     data = get_weather_forecast(city, api_key)

#     if "list" in data:
#         print(f"Weather forecast for {city}:")
#         for item in data["list"]:
#             # Extract the date and temperature
#             date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
#             date_str = date.strftime("%A, %b %d")
#             temp = item["main"]["temp"]
#             description = item["weather"][0]["description"]

#             print(f"{date_str}: {temp}°C, {description}")
#     else:
#         print("Unable to retrieve weather forecast.")

if __name__ == "__main__":
    main()