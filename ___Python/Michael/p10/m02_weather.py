from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Moormerland')
condition = location.condition
print(condition.text)
print(condition.temp)
