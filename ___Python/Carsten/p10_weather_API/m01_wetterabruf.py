from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('vaals')
condition = location.condition
print(condition.temp)


forecasts = location.forecast
for forecast in forecasts:
    #print(forecasts)
    print(forecast.text)
    #print(forecast.date)
    #print(forecast.high)
    #print(forecast.low)
