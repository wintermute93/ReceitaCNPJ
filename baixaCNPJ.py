import requests
import tqdm
import zipfile
import os
import datetime

BASE_DIR = "base"
ESTABELECIMENTOS_DIR = os.path.join(BASE_DIR, "estabelecimentos")


def ensure_directories_exist():
    os.makedirs(ESTABELECIMENTOS_DIR, exist_ok=True)


def write_log(message, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] {message}\n")
    print(message)


def download_file(url, filename, log_file):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading {filename}")
    with open(filename, "wb") as f:
        for data in response.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    write_log(f"Downloaded {filename} to {BASE_DIR} directory", log_file)


def extract_and_move(zip_filename, dest_dir, log_file):
    with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        zip_ref.extractall(dest_dir)
    os.remove(zip_filename)
    write_log(f"Extracted and moved {zip_filename} to {dest_dir} directory", log_file)


def main():
    ensure_directories_exist()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{BASE_DIR}/log_{timestamp}.txt", "w") as log_file:
        # Download Estabelecimentos ZIP files
        for i in range(10):
            url = f"https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos{i}.zip"
            download_file(url, f"{BASE_DIR}/Estabelecimentos{i}.zip", log_file)
            extract_and_move(f"{BASE_DIR}/Estabelecimentos{i}.zip", ESTABELECIMENTOS_DIR, log_file)

        # Download Cnaes ZIP file
        cnaes_url = "https://dadosabertos.rfb.gov.br/CNPJ/Cnaes.zip"
        download_file(cnaes_url, f"{BASE_DIR}/Cnaes.zip", log_file)
        extract_and_move(f"{BASE_DIR}/Cnaes.zip", BASE_DIR, log_file)


if __name__ == "__main__":
    main()
