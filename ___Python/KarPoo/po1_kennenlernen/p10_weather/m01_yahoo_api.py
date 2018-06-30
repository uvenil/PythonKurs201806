from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('bielefeld')
condition = location.condition
print(condition.text)
print(condition.temp)