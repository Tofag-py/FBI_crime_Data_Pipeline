import pandas as pd
import requests
import json

def get_data(url: str):
    try:
        raw_data = requests.get(url)
        raw_data.raise_for_status() 
        
        data = raw_data.json()
        return data

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

    return None  

def download_local(data: dict, local_path: str):
    try:
        # Save the JSON data to a local file
        with open(local_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Data downloaded and saved to {local_path}")
        return data

    except IOError as e:
        print(f"Error writing to file: {e}")

    return None

def download_and_extract_fields(data: dict, local_path: str):
    try:
        # Extract fields from the data
        extracted_data = []
        for entry in data:
            extracted_entry = {
                "id": entry.get("id"),
                "case_number": entry.get("case_number"),
                "date": entry.get("date"),
                "block": entry.get("block"),
                "iucr": entry.get("iucr"),
                "primary_type": entry.get("primary_type"),
                "description": entry.get("description"),
                "location_description": entry.get("location_description"),
                "arrest": entry.get("arrest"),
                "domestic": entry.get("domestic"),
                "beat": entry.get("beat"),
                "district": entry.get("district"),
                "ward": entry.get("ward"),
                "community_area": entry.get("community_area"),
                "fbi_code": entry.get("fbi_code"),
                "year": entry.get("year"),
                "updated_on": entry.get("updated_on"),
            }
            extracted_data.append(extracted_entry)

        # Convert the extracted data to a DataFrame
        df = pd.DataFrame(extracted_data)

        # Save the DataFrame to a CSV file
        df.to_csv(local_path, index=False)

        print(f"Data extracted and saved to {local_path}")
        return df

    except IOError as e:
        print(f"Error writing to file: {e}")

    return None

if __name__ == "__main__":
    url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

    data = get_data(url)
    
    if data:
        local_path = "/Users/tofag/Desktop/ReadWrite Assignments/FBI_data/extracted_chicago_crime_data.csv"  
        download_local(data, local_path)
        download_and_extract_fields(data, local_path)
    else:
        print("Data retrieval failed.")
