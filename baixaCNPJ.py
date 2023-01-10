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

    # extract files to estabelecimentos directory inside base
    with zipfile.ZipFile(f"base/Estabelecimentos{i}.zip", "r") as zip_ref:
        zip_ref.extractall("base/estabelecimentos")
    os.remove(f"base/Estabelecimentos{i}.zip")
    log_file.write(
        f"Extracted and moved Estabelecimentos{i}.zip to base/estabelecimentos directory at {datetime.datetime.now()}\n")
    print(f"Extracted and moved Estabelecimentos{i}.zip to base/estabelecimentos directory")

log_file.close()
