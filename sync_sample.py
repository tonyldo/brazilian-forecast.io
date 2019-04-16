import brazilianforecast

if __name__ == "__main__":
    current_conditions = brazilianforecast.load_current(-10.979968, -37.055018)
    print(current_conditions.get_reading('temperature'))
    print(current_conditions.get_formated_icon_URL(current_conditions.get_reading('weather')))