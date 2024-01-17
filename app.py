import requests

def fetch_second_array(url):
    try:
        # Fetch JSON data from the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            json_data = response.json()

            # Removing the 1st Element, so that we get a good json data for ordering
            if isinstance(json_data, list) and len(json_data) >= 2:
                second_array = json_data[1]
                return second_array
            else:
                print("JSON data does not contain a second array or has insufficient elements.")
                return None
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Adding the api_url variable that provides JSON data
api_url = 'https://api.worldbank.org/v2/region?format=json'
second_array_data = fetch_second_array(api_url)

# Sorting the data based on the 'iso2code' field
sorted_data = sorted(second_array_data, key=lambda x: x.get('iso2code', ''))

# Display the top 5 entries
ordered_list = sorted_data[:5]

# Write JSON content to a file
output_file = 'index.html'

with open("output_file_path", "w") as output_file:
    for entry in ordered_list:
        print(entry, file=output_file)
    output_file.close()
