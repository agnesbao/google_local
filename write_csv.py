# convert to csv file
import gzip
import pandas as pd
from itertools import islice


def write_csv(fname, colnames, csv_path, batch_size=1000):
    print(f"Writing to {csv_path}...")
    with gzip.open(fname, "rb") as f:
        ct = 0
        for lines in iter(lambda: tuple(islice(f, batch_size)), ()):
            dat = [eval(line) for line in lines]
            pd.DataFrame(dat)[colnames].to_csv(
                csv_path, index=False, header=False, mode="a"
            )
            ct += 1
            if ct % 100 == 0:
                print(f"Processed {ct*batch_size} lines...")
    print(f"Done processing.")


fname = "data/places.clean.json.gz"
colnames = ["name", "price", "closed", "gPlusPlaceId", "gps"]
csv_path = "data/places.csv"
write_csv(fname, colnames, csv_path)

fname = "data/reviews.clean.json.gz"
colnames = [
    "rating",
    "reviewerName",
    "reviewText",
    "categories",
    "gPlusPlaceId",
    "unixReviewTime",
    "reviewTime",
    "gPlusUserId",
]
csv_path = "data/reviews.csv"
write_csv(fname, colnames, csv_path)
