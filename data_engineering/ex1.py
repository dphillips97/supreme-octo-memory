from concurrent.futures import ThreadPoolExecutor
import urllib.request
import zipfile
import os

"""
TODO
---

- create download_file()
- create process_file()

"""

DOWNLOAD_DIR = 'downloads'

URLS = [
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
      ]

def is_valid_url(url):
    """Check that URL is valid before processing"""
    
    try:
        response = urllib.request.urlopen(url)
        return response.status == 200
    
    except urllib.error.URLError as e:
        return False
    
    except urllib.error.HTTPError as e:
        return False
    

def create_paths(url):
    """Make paths or path-like objects from url (and ZIP file name)"""

    # Make destination folder to hold ZIP and member files
    destination_folder = os.path.join(os.getcwd(), DOWNLOAD_DIR)

    # Get ZIP file name from url
    zip_filename = os.path.basename(url)

    # Point to where ZIP file will be saved (incl filename)
    destination_filename = os.path.join(destination_folder, zip_filename)

    return destination_filename, destination_folder



def download_file(url, destination_filename):
    """Create paths and retreive file from valid url"""

    try:
        urllib.request.urlretrieve(url, destination_filename)

    except Exception as e:
        print(f"Error in downloading file from {url}")


def extract_and_delete(destination_filename, destination_folder):
    """Extracts the csv from the ZIP file"""

    with zipfile.ZipFile(destination_filename, mode="r") as archive:
        archive.extractall(destination_folder)

    os.remove(destination_filename)


def process_file(url):

    if is_valid_url(url):
       
       destination_filename, destination_folder = create_paths(url)

       download_file(url, destination_filename)

       extract_and_delete(destination_filename, destination_folder)

if __name__ == "__main__":
    
    # Create directory for urllib
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        executor.map(process_file, URLS)