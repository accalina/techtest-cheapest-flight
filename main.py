
from src.algo import findCheapestPrice
from src.utils import read_json_file


def spread_data_from_json(item):
    n = item['n']
    flights = item['flights']
    src = item['src']
    dst = item['dst']
    k = item['k']
    return n, flights, src, dst, k

def main():
    json_data = read_json_file('question.json')
    for item in json_data:
        n, flights, src, dst, k = spread_data_from_json(item)
        result = findCheapestPrice(n, flights, src, dst, k)
        print(f"The cheapest price from {src} to {dst} with at most {k} stops is: {result}")

if __name__ == '__main__':
    main()