import requests
import argparse
from datetime import datetime, timedelta
parser = argparse.ArgumentParser()

# Parser Work
parser.add_argument(
    "--duration",
    choices=["day", "week", "month", "year"],
    default="week"
)

parser.add_argument(
    "--limit",
    type=int,
    default=10
)

args = parser.parse_args()

# Calculating Startdate
duration_days = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365
}

start_date = datetime.now() - timedelta(
    days=duration_days[args.duration]
)
formatted_date = start_date.strftime("%Y-%m-%d")

# Fetching Github url
url = "https://api.github.com/search/repositories"

params = {
    "q": f"created:>{formatted_date} language:python",
    "sort": "stars",
    "order": "desc",
    "per_page": args.limit
}

response = requests.get(url, params=params, timeout=10)

# Displaying the results
if response.status_code == 200:
    data = response.json()

    for repo in data["items"]:
        print("repo:",repo["full_name"])
        print("stars:",repo["stargazers_count"])
        print("-" * 40)

else:
    print("API Error:", response.status_code)
    print(response.json())