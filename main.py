from src.api_client import APICoordinates, APIAircraft

if __name__ == '__main__':
    api = APICoordinates()
    api.get_response_api('Germany')
    api.get_coordinates()

    api_2 = APIAircraft()
    api_2.get_response_api(api.coordinates)
    data_1 = api_2.aeroplanes
    print(data_1)

## Сделать цикл для 10 стран и запрос от каждой.France.Germany.Italy.Spain.Sweden.Poland.Greece.Portugal.Netherlands.Austria.