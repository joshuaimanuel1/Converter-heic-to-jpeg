import pyheif
from PIL import Image
import os
import zipfile
import shutil

def extract_zip(zip_path, extract_to):
    """ Ekstrak file ZIP ke folder tujuan """
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"File diekstrak ke: {extract_to}")

def convert_heic_folder(input_folder, output_folder):
    """ Konversi semua file HEIC dalam folder ke JPEG """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(".heic"):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_folder, filename.replace(".heic", ".jpg"))

                # Konversi HEIC ke JPEG
                heif_file = pyheif.read(input_path)
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data, 
                    "raw", 
                    heif_file.mode, 
                    heif_file.stride
                )
                image.save(output_path, "JPEG")
                print(f"File dikonversi: {output_path}")

def create_zip(output_folder, zip_name):
    """ Buat ZIP dari folder hasil konversi """
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.basename(file_path))
    print(f"Semua gambar dikompresi ke {zip_name}")

if __name__ == "__main__":
    zip_file = "jojo.zip"  # Nama file ZIP input
    extract_folder = "temp_extracted"  # Folder sementara untuk ekstrak
    output_folder = "converted"  # Folder untuk menyimpan hasil konversi
    output_zip = "converted_images.zip"  # Nama ZIP hasil akhir
    
    # 1. Ekstrak file ZIP
    extract_zip(zip_file, extract_folder)
    
    # 2. Konversi file HEIC ke JPEG
    convert_heic_folder(extract_folder, output_folder)
    
    # 3. Kompres semua hasil ke satu file ZIP
    create_zip(output_folder, output_zip)

    # 4. Hapus folder sementara setelah selesai
    shutil.rmtree(extract_folder)
    shutil.rmtree(output_folder)
    
    print(f"Proses selesai! Unduh hasilnya: {output_zip}")
