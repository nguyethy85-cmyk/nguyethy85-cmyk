import requests

URL = "https://freem3u.xyz/api/channels/x_1.0.1/app.json"

OUTPUT = "source.json"

headers = {
    "User-Agent": "okhttp/4.12.0"
}


def download():

    response = requests.get(
        URL,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(response.text)

    print("Downloaded JSON")


if __name__ == "__main__":
    download()
