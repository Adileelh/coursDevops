import requests


def fetch_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            print(f"Quote: {data['content']}\nAuthor: {data['author']}")
        else:
            print(f"Failed to get quote. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_random_quote()
