# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 12:12:15 2025

@author: sai manogna
"""


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)
print(img_array)
y1, x1 = 100, 100  # Top-left corner of ROI
y2, x2 = 250, 200  # Bottom-right corner of ROI
cropped_img = img_array[y1:y2, x1:x2]
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cropped_img)
plt.title('Cropped Image')
plt.axis('off')
plt.tight_layout()
plt.show()

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)
rotated_img = np.rot90(img_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rotated_img )
plt.title('Rotated Image (90 degrees)')
plt.axis('off')

plt.tight_layout()
plt.show()


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)
flipped_img = np.fliplr(img_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(flipped_img )
plt.title('Flipped Image')
plt.axis('off')
plt.tight_layout()
plt.show()


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)
is_grayscale = len(img_array.shape) < 3

def create_negative(image):
    if is_grayscale:
       
        negative_image = 255 - image
    else:
     
        negative_image = 255 - image
    return negative_image

negative_img = create_negative(img_array)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(negative_img)
plt.title('Negative Image')
plt.axis('off')
plt.tight_layout()
plt.show()

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)

threshold = 128
binary_img = np.where(img_array < threshold, 0, 255).astype(np.uint8)

plt.figure(figsize= (10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(binary_img, cmap='gray')
plt.title('Binarized Image (Threshold = 128)')
plt.axis('off')
plt.tight_layout()
plt.show()

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)

gray_img = np.dot (img_array[..., :3], [0.299, 0.587, 0.114])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.tight_layout()
plt.show()

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img = Image.open(r"C:\Users\Sai Manogna\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)

hist, bins = np.histogram(img_array.flatten(), bins=256, range= (0, 256))

plt.figure(figsize=(10, 5))
plt.hist(img_array.flatten(), bins=256, range= (0, 256), density=True, color='gray')
plt.xlabel('Pixel Intensity')
plt.ylabel('Normalized Frequency')
plt.title('Histogram of Grayscale Image')
plt.grid(True)
plt.show()

