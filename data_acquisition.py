from Bio import Entrez
from urllib.request import urlretrieve
import os

# Enter your email address for NCBI Entrez API
Entrez.email = "your_email@example.com"

# Define search query to retrieve gene expression data
search_query = "homeobox genes AND Homo sapiens[ORGN]"

# Search Entrez database for GEO datasets matching the query
handle = Entrez.esearch(db="gds", term=search_query)
record = Entrez.read(handle)

# Retrieve the GEO dataset IDs
id_list = record["IdList"]
print(f"Found {len(id_list)} GEO datasets matching the query")

# Download the gene expression data files for each GEO dataset
for dataset_id in id_list:
    # Retrieve the GEO dataset information
    handle = Entrez.esummary(db="gds", id=dataset_id)
    record = Entrez.read(handle)
    title = record[0]["title"]
    print(f"Processing dataset {dataset_id}: {title}")

    # Find the GEO data files in the dataset
    handle = Entrez.esearch(db="gds", term=f"{dataset_id}[Accession]")
    record = Entrez.read(handle)
    file_id_list = record["IdList"]

    # Download the GEO data files
    for file_id in file_id_list:
        handle = Entrez.esummary(db="gds", id=file_id)
        record = Entrez.read(handle)
        file_name = record[0]["filename"]
        file_url = record[0]["url"]
        file_path = os.path.join("data", file_name)
        print(f"Downloading file {file_name}")
        urlretrieve(file_url, file_path)
