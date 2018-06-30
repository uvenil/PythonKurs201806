# Wetterdaten über die Yahoo API ermitteln

from weather import Weather, Unit


weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Hannover')
condition = location.condition
print(condition.text)


location = weather.lookup_by_location('Hannover')
forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print("Tageshoechsttemp. " + (forecast.high) + "°C")
    print(forecast.low)