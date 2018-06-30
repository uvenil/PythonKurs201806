# Wetterdaten über die Yahoo API

from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('loehne')


forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)
