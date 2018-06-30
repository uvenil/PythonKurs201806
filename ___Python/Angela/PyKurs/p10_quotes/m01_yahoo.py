# Wetterdaten ueber die Yahoo API ermitteln
# https://pypi.org/project/weather-api/

from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('bielefeld')
condition = location.condition
print(condition.text)

forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)