def estimate_arrival(distance_km, weather_condition):
    base_time = distance_km * 3
    if weather_condition == "rainy":
        return base_time + 10
    else:
        return base_time

time_rainy = estimate_arrival(5, "rainy")
print("Arrival time in rainy weather:", time_rainy, "minutes")

time_sunny = estimate_arrival(5, "sunny")
print("Arrival time in sunny weather:", time_sunny, "minutes")
