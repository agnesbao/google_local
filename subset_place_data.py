# subset data (I don't need the whole world)
import pandas as pd

# guess where it is
coord = (42.0480, -87.6843)
deg_range = 10


def get_lat_long(gps):
    if type(gps[0]) == str:
        return eval(gps[0])


places = pd.read_csv("data/places.csv", header=None)
places.columns = ["name", "price", "closed", "gPlusPlaceId", "gps"]

places[["lat", "long"]] = places[["gps"]].apply(
    get_lat_long, axis=1, result_type="expand"
)

places_subset = places[
    (places["lat"] > coord[0] - deg_range)
    & (places["lat"] < coord[0] + deg_range)
    & (places["long"] > coord[1] - deg_range)
    & (places["long"] < coord[1] + deg_range)
][["name", "price", "closed", "gPlusPlaceId", "lat", "long"]]

places_subset.to_csv("data/places_sub.csv", index=False)
