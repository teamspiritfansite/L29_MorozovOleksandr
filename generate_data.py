import csv
from pathlib import Path

from faker import Faker


DATA_DIR = Path(__file__).parent / "data"


def create_dataset(locale: str, seed: int, filename: str) -> None:
    fake = Faker(locale)
    Faker.seed(seed)
    fake.seed_instance(seed)
    output = DATA_DIR / filename

    with output.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["first_name", "last_name", "postal_code"],
        )
        writer.writeheader()
        for _ in range(10):
            writer.writerow(
                {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "postal_code": fake.postcode(),
                }
            )


if __name__ == "__main__":
    DATA_DIR.mkdir(exist_ok=True)
    create_dataset("ru_RU", 2801, "users.csv")
    create_dataset("ro_RO", 2901, "users_ro.csv")
    print("Created data/users.csv and data/users_ro.csv (10 rows each).")
