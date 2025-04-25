import requests
import json

# Replace with your actual API URL
url = "https://api.cricapi.com/v1/currentMatches?apikey=85036824-3f91-4bcf-9f55-7d1b137f670a&offset=0"

response = requests.get(url)

if response.status_code == 200:
    print("Status Code:", response.status_code)
    data = response.json()
    print("Live Cricket Match Summary:\n")

    for match in data.get("data", []):
        print("🏏 Match:", match.get("name", "N/A"))
        print("📍 Venue:", match.get("venue", "N/A"))
        print("📅 Date:", match.get("date", "N/A"))
        print("🔄 Status:", match.get("status", "N/A"))
        print("👥 Teams:", " vs ".join(match.get("teams", [])))
        print("📊 Scores:")

        for inning in match.get("score", []):
            print(f"  - {inning.get('inning')}: {inning.get('r')}/{inning.get('w')} in {inning.get('o')} overs")

        print("-" * 40)

else:
    print("Failed to fetch data. Status Code:", response.status_code)
