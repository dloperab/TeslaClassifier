# NOTE: This code is based on blog post https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/

# Import the necessary packages
from requests import exceptions
import requests
import cv2
import os

class SearchBingApi:
    @staticmethod
    def search(query, output, maxResults, groupSize):
        # Set your Microsoft Cognitive Services API key
        API_KEY = "<YOUR_API_KEY_GOES_HERE>"

        # Set the endpoint API URL
        URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

        # When attempting to download images from the web both the Python
        # programming language and the requests library have a number of
        # exceptions that can be thrown so let's build a list of them now
        # so we can filter on them
        EXCEPTIONS = set([IOError, FileNotFoundError,
            exceptions.RequestException, exceptions.HTTPError,
            exceptions.ConnectionError, exceptions.Timeout])

        # Store the search term in a convenience variable then set the
        # headers and search parameters
        term = query
        headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
        params = {"q": term, "offset": 0, "count": groupSize}

        # Make the search
        print("[INFO] Searching Bing API for '{}'".format(term))
        search = requests.get(URL, headers=headers, params=params)
        search.raise_for_status()

        # Grab the results from the search, including the total number of
        # estimated results returned by the Bing API
        results = search.json()
        estNumResults = min(results["totalEstimatedMatches"], maxResults)
        print("[INFO] {} total results for '{}'".format(estNumResults, term))

        # Initialize the total number of images downloaded thus far
        total = 0

        # Loop over the estimated number of results in 'groupSize' groups
        for offset in range(0, estNumResults, groupSize):
            # Update the search parameters using the current offset, then
            # make the request to fetch the results
            print("[INFO] making request for group {}-{} of {}...".format(
                offset, offset + groupSize, estNumResults))
            params["offset"] = offset
            search = requests.get(URL, headers=headers, params=params)
            search.raise_for_status()
            results = search.json()
            print("[INFO] Saving images for group {}-{} of {}...".format(
                offset, offset + groupSize, estNumResults))

            # Loop over the results
            for v in results["value"]:
                # Try to download the image
                try:
                    # Make a request to download the image
                    print("[INFO] Fetching: {}".format(v["contentUrl"]))
                    r = requests.get(v["contentUrl"], timeout=30)

                    # Build the path to the output image
                    ext = v["contentUrl"][v["contentUrl"].rfind("."):]
                    p = os.path.sep.join([output, "{}{}".format(
                        str(total).zfill(3), ext)])

                    # Write the image to disk
                    f = open(p, "wb")
                    f.write(r.content)
                    f.close()
                except Exception as e:
                    # Catch any errors that would not unable us to download the image
                    # check to see if our exception is in our list of
                    # exceptions to check for
                    if type(e) in EXCEPTIONS:
                        print("[INFO] Skipping: {}".format(v["contentUrl"]))
                        continue

                # Try to load the image from disk
                image = cv2.imread(p)

                # If the image is `None` then we could not properly load the
                # image from disk (so it should be ignored)
                if image is None:
                    print("[INFO] Deleting: {}".format(p))
                    os.remove(p)
                    continue

                # Update the counter
                total += 1
