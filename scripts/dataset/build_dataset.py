# Import the necessary packages
from search_bing_api import SearchBingApi

# Set global params
TRAIN_MAX_RESULTS = 60
TRAIN_GROUP_SIZE = 60
TEST_MAX_RESULTS = 20
TEST_GROUP_SIZE = 20

# Roadster
query = "tesla roadster"
output = "../../dataset/train/roadster"
print("[INFO] Downloading images for Tesla Roadster")
SearchBingApi.search(query, output, TRAIN_MAX_RESULTS, TRAIN_GROUP_SIZE)
output = "../../dataset/test/roadster"
SearchBingApi.search(query, output, TEST_MAX_RESULTS, TEST_GROUP_SIZE)
