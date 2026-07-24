import json
from datetime import datetime

INPUT_FILE = "source.json"
OUTPUT_FILE = "channels.json"


def update_json():
    # Đọc JSON gốc
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Tạo JSON mới
    output = {
        "update_time": datetime.utcnow().isoformat() + "Z",
        "channels": data
    }

    # Ghi file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("JSON updated successfully!")


if __name__ == "__main__":
    update_json()
