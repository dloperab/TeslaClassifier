# Import the necessary packages
from search_bing_api import SearchBingApi

# Set global params
MAX_RESULTS = 120
GROUP_SIZE = 40

# Roadster
query = "tesla roadster"
output = "../../dataset/teslas/train/roadster"
print("[INFO] Downloading images for Tesla Roadster")
SearchBingApi.search(query, output, MAX_RESULTS, GROUP_SIZE)

# Tesla Model 3
query = "tesla model 3"
output = "../../dataset/teslas/train/model_3"
print("[INFO] Downloading images for Tesla Model 3")
SearchBingApi.search(query, output, MAX_RESULTS, GROUP_SIZE)

# Tesla Model S
query = "tesla model s"
output = "../../dataset/teslas/train/model_s"
print("[INFO] Downloading images for Tesla Model S")
SearchBingApi.search(query, output, MAX_RESULTS, GROUP_SIZE)

# Tesla Model X
query = "tesla model x"
output = "../../dataset/teslas/train/model_x"
print("[INFO] Downloading images for Tesla Model X")
SearchBingApi.search(query, output, MAX_RESULTS, GROUP_SIZE)

# Tesla Semi
query = "tesla semi"
output = "../../dataset/teslas/train/semi"
print("[INFO] Downloading images for TTesla Semi")
SearchBingApi.search(query, output, MAX_RESULTS, GROUP_SIZE)
