from function import fetch_weather


if __name__ == "__main__":
    fetch_weather.serve(name="deploy-params",parameters={"lat": 11, "lon": 12})
