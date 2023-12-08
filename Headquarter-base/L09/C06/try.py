from PIL import Image

img = Image.open('M5KDAN44.jpg')
exif_data = img._getexif()  # Retrieve EXIF data

# Print all EXIF tags and their values
if exif_data:
    for tag, value in exif_data.items():
        print(f'Tag: {tag}, Value: {value}')
else:
    print('No EXIF data found.')
