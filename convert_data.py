import gzip
import pandas as pd
from itertools import islice


def convert_data(fname, colnames, datadir, batch_size=100000):
    print(f"Writing to {datadir}...")
    with gzip.open(fname, "rb") as f:
        ct = 0
        for lines in iter(lambda: tuple(islice(f, batch_size)), ()):
            dat = [eval(line) for line in lines]
            df = pd.DataFrame(dat)
            if "gps" in df.columns:
                gps_df = pd.DataFrame(
                    df["gps"].dropna().to_list(),
                    df["gps"].dropna().index,
                    columns=["lat", "long"],
                )
                df = df.join(gps_df)
            df[colnames].to_parquet(
                f"{datadir}_{ct}.parquet", index=False, compression=None
            )
            ct += 1
            print(f"Processed {ct*batch_size} lines...")
    print("Done processing.")


fname = "data/places.clean.json.gz"
colnames = ["name", "price", "closed", "gPlusPlaceId", "lat", "long"]
datadir = "data/places"
convert_data(fname, colnames, datadir)

fname = "data/reviews.clean.json.gz"
colnames = [
    "rating",
    "reviewerName",
    "categories",
    "gPlusPlaceId",
    "unixReviewTime",
    "reviewTime",
    "gPlusUserId",
]
datadir = "data/reviews"
convert_data(fname, colnames, datadir)
