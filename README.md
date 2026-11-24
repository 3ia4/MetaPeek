# MetaPeek

**image metadata inspector built with Python.**

MetaPeek extracts useful information from image files, including EXIF metadata, camera details, timestamps, and GPS information when available.

---

### Overview

Images can contain more information than what is visible. MetaPeek makes that information easier to inspect through a simple command-line interface.

### Features

- **Image Information** — View image format, resolution, and file size.
- **Camera Details** — Inspect camera manufacturer and model.
- **Timestamps** — Retrieve the original date and time when available.
- **GPS Metadata** — Check for embedded location information.
- **EXIF Extraction** — Read available metadata directly from image files.

### Preview

```text
File: photo.jpg
Format: JPEG
Resolution: 4032 x 3024
Size: 3420.50 KB

Camera Information
Make: Apple
Model: iPhone
Date: 2026:11:20 14:32:10

GPS Information
GPS metadata: Available
```

### Installation

Clone the repository:

```bash
git clone https://github.com/3ia4/MetaPeek.git
cd MetaPeek
```

Install dependencies:

```bash
pip install Pillow
```

### Usage

Run MetaPeek with an image path:

```bash
python peek.py "path/to/image.jpg"
```

### Requirements

- Python 3.9+
- Pillow

### Notes

- Not all images contain EXIF metadata.
- GPS information is only available when embedded in the image.
- MetaPeek reads metadata locally and does not upload images anywhere.
- GPS values are displayed in their original EXIF format.

### License

MIT License.

---

*Built with Python and Pillow.*
