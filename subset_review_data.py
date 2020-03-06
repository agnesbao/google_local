import pandas as pd

places = pd.read_csv("data/places_sub.csv")
reviews = pd.read_csv("data/reviews.csv", header=None, usecols=[0, 3, 4, 5, 7])
reviews.columns = [
    "rating",
    "categories",
    "gPlusPlaceId",
	"unixReviewTime",
    "gPlusUserId",
]
reviews["first_category"] = reviews["categories"].apply(
    lambda x: eval(x)[0] if type(x) == str else None
)
reviews_subset = reviews[reviews["gPlusPlaceId"].isin(places["gPlusPlaceId"])][
    ["rating", "first_category", "gPlusPlaceId", "gPlusUserId", "unixReviewTime"]
]
reviews_subset.to_csv("data/reviews_sub.csv", index=False)
