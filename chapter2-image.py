from PIL import Image

# Memuat gambar
image = Image.open('cat.jpg')

# Menyimpan gambar
image.save('result.jpg')

#### Cropping

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

#### Resizing

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

#### Filtering

from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')