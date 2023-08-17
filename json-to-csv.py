import csv
import requests

# Fetch data from the URL
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Prepare data for CSV
csv_data = []
csv_data.append(["userId", "id", "title", "body"])  # Header row

for entry in data:
    csv_data.append([entry["userId"], entry["id"], entry["title"], entry["body"]])

# Write data to CSV file
csv_filename = "posts.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print(f"CSV file '{csv_filename}' created successfully!")

