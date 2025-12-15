import sys
from PIL import Image

images = []  # list to store images

for arg in sys.argv[1:]:
    img = Image.open(arg)
    images.append(img)

# save as animated GIF
images[0].save(
    "output.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
)
