import requests
import tqdm
import zipfile
import os
import datetime

# Create the "base" directory if it doesn't exist
if not os.path.exists("base"):
    os.mkdir("base")

# Create the "estabelecimentos" directory inside "base" if it doesn't exist
if not os.path.exists("base/estabelecimentos"):
    os.mkdir("base/estabelecimentos")

# Create log file with current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = open(f"base/log_{timestamp}.txt", "w")

# Download Estabelecimentos ZIP files
for i in range(10):
    url = f"https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos{i}.zip"
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading Estabelecimentos{i}.zip")
    with open(f"base/Estabelecimentos{i}.zip", "wb") as f:
        for data in response.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    log_file.write(f"Downloaded Estabelecimentos{i}.zip to base directory at {datetime.datetime.now()}\n")
    print(f"Downloaded Estabelecimentos{i}.zip to base directory")

# Download Cnaes ZIP file
cnaes_url = "https://dadosabertos.rfb.gov.br/CNPJ/Cnaes.zip"
cnaes_response = requests.get(cnaes_url, stream=True)
cnaes_total_size = int(cnaes_response.headers.get("Content-Length", 0))
cnaes_t = tqdm.tqdm(total=cnaes_total_size, unit='B', unit_scale=True, desc="Downloading Cnaes.zip")
with open("base/Cnaes.zip", "wb") as cnaes_file:
    for data in cnaes_response.iter_content(block_size):
        cnaes_t.update(len(data))
        cnaes_file.write(data)
cnaes_t.close()
log_file.write(f"Downloaded Cnaes.zip to base directory at {datetime.datetime.now()}\n")
print("Downloaded Cnaes.zip to base directory")

# Extract and move Estabelecimentos ZIP files
for i in range(10):
    with zipfile.ZipFile(f"base/Estabelecimentos{i}.zip", "r") as zip_ref:
        zip_ref.extractall("base/estabelecimentos")
    os.remove(f"base/Estabelecimentos{i}.zip")
    log_file.write(
        f"Extracted and moved Estabelecimentos{i}.zip to base/estabelecimentos directory at {datetime.datetime.now()}\n")
    print(f"Extracted and moved Estabelecimentos{i}.zip to base/estabelecimentos directory")

# Extract Cnaes ZIP file
with zipfile.ZipFile("base/Cnaes.zip", "r") as cnaes_zip_ref:
    cnaes_zip_ref.extractall("base")
os.remove("base/Cnaes.zip")
log_file.write(f"Extracted and moved Cnaes.zip to base directory at {datetime.datetime.now()}\n")
print("Extracted and moved Cnaes.zip to base directory")

log_file.close()
