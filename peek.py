
import argparse
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

print("meow :3")

def getExif(image):
    exifData = image.getexif()
    metadata = {}

    for tagId, value in exifData.items():
        tagName = TAGS.get(tagId, tagId)
        metadata[tagName] = value

    return metadata


def getGps(metadata):
    gpsInfo = metadata.get("GPSInfo")

    if not gpsInfo:
        return None

    gpsData = {}

    for tagId, value in gpsInfo.items():
        tagName = GPSTAGS.get(tagId, tagId)
        gpsData[tagName] = value

    return gpsData


def main():
    parser = argparse.ArgumentParser(
        description="Simple image metadata inspector"
    )
    parser.add_argument("image", help="Path to an image")
    args = parser.parse_args()

    imagePath = Path(args.image)

    if not imagePath.is_file():
        print("File not found.")
        return

    try:
        with Image.open(imagePath) as image:
            metadata = getExif(image)

            print(f"\nFile: {imagePath.name}")
            print(f"Format: {image.format}")
            print(f"Resolution: {image.width} x {image.height}")
            print(f"Size: {imagePath.stat().st_size / 1024:.2f} KB")

            print("\nCamera Information")
            print(f"Make: {metadata.get('Make', 'Unknown')}")
            print(f"Model: {metadata.get('Model', 'Unknown')}")
            print(f"Date: {metadata.get('DateTimeOriginal', 'Unknown')}")

            gpsData = getGps(metadata)

            print("\nGPS Information")

            if gpsData:
                print("GPS metadata: Available")
                print(f"Latitude: {gpsData.get('GPSLatitude', 'Unknown')}")
                print(f"Longitude: {gpsData.get('GPSLongitude', 'Unknown')}")
            else:
                print("No GPS metadata found.")

    except Exception as error:
        print(f"Could not read image: {error}")


if __name__ == "__main__":
    main()
