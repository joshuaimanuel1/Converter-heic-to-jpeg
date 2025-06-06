```markdown
# 📷 HEIC to JPEG Batch Converter with ZIP Support

## Overview

This Python-based tool automates the batch conversion of `.HEIC` (High Efficiency Image Coding) images—commonly used by iPhones—into the more widely supported `.JPEG` format. It works directly from a `.zip` archive containing your `.HEIC` files, converts them all, and compresses the output into a new `.zip` file ready for download.

> 💡 This is perfect for users who want to convert entire folders of iPhone photos for compatibility on non-Apple systems (Windows, Linux, Android, web, etc.).

---

## 🔧 Features

- ✅ Extracts a `.zip` file containing `.HEIC` images
- ✅ Converts each `.HEIC` file to `.JPEG` using `pyheif` and `Pillow`
- ✅ Packages the converted images into a new downloadable `.zip`
- ✅ Cleans up temporary folders to keep your workspace tidy
- ✅ Cross-platform (Windows/macOS/Linux)

---

## 📁 Project Structure

```

heic-to-jpeg-converter/
│
├── jojo.zip                  # Input ZIP file (user-provided)
├── convert\_heic\_zip.py       # Main conversion script
├── converted\_images.zip      # Output ZIP with JPEGs (generated)
└── README.md                 # This file

````

---

## 🚀 How to Use

### 1. 🔧 Install Requirements

Make sure you have Python 3.6+ installed.

Then, install dependencies:
```bash
pip install pyheif pillow
````

### 2. 📦 Prepare Your ZIP

Place your `.HEIC` photos inside a zip file. Example: `jojo.zip`.

> The ZIP file should only contain image files or folders of `.heic` images.

### 3. ▶️ Run the Script

```bash
python convert_heic_zip.py
```

### 4. 📁 Output

* All `.HEIC` images inside `jojo.zip` will be converted to `.JPEG`.
* A file named `converted_images.zip` will be created containing all the `.JPEG` images.
* Temporary files will be automatically deleted.

---

## 🧠 How It Works (Under the Hood)

1. **Extract ZIP**:

   * The script first extracts the `jojo.zip` archive to a temporary directory.

2. **Convert HEIC to JPEG**:

   * It scans all folders and subfolders for `.heic` files.
   * Each `.heic` image is decoded using `pyheif.read()` and converted to a JPEG using `Pillow`.

3. **Repack JPEGs into ZIP**:

   * After all conversions, the `.jpg` files are zipped into `converted_images.zip`.

4. **Cleanup**:

   * Temporary folders (`temp_extracted` and `converted`) are deleted automatically.

---

## 🔐 Dependencies

* [pyheif](https://pypi.org/project/pyheif/) — To decode `.heic` files
* [Pillow](https://pypi.org/project/Pillow/) — For image processing and saving JPEGs
* Built-in Python modules: `os`, `zipfile`, `shutil`

---

## 💡 Example Use Case

You have a ZIP file named `jojo.zip` exported from your iPhone containing `.HEIC` images. You want to:

* Convert all photos to `.JPG`
* Send or use them on platforms that don’t support `.HEIC`
* Package them again into a clean `.zip` for download or sharing

Just run the script and you're done.

---

## 🧪 Future Improvements

* Add GUI support using Tkinter or PyQt
* Drag-and-drop zip file interface
* Support for converting to `.png` or `.webp`
* Upload and download support via web dashboard (Flask/Streamlit)

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests to improve performance, add features, or fix bugs!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Joshua
