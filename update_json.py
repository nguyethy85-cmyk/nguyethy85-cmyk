import json
from datetime import datetime


INPUT = "source.json"
OUTPUT = "channels.json"


def update():

    with open(
        INPUT,
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)


    result = {
        "update_time": datetime.utcnow().isoformat() + "Z",
        "channels": data
    }


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            result,
            f,
            ensure_ascii=False,
            indent=2
        )


    print("JSON updated")


if __name__ == "__main__":
    update()
