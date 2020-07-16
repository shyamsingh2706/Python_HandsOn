from PIL import Image

''' Open Images through PIL library'''
matrix_image = Image.open('C:\\Users\\shyam\\Downloads\\word_matrix.png','r')
mask_image = Image.open('C:\\Users\\shyam\\Downloads\\mask.png','r')

# Check size of each image
matrix_size = matrix_image.size
mask_size = mask_image.size

# Re-size one of the image to match the other so that it can overlap
mask_resize_image = mask_image.resize(matrix_size)
# Confirm that after resizing both images of same pixel
mask_resize_image_size = mask_resize_image.size

print (f"martix Image size is {matrix_size}")
print (f"mask Image original size is {mask_size}")
print (f"mask Image re-size is {mask_resize_image_size}")

# increase the transparency of the image
mask_resize_image.putalpha(200)

# overlap image to see the end result
matrix_image.paste(im=mask_resize_image,box =(0,0),mask=mask_resize_image)
matrix_image.save('C:\\Users\\shyam\\Downloads\\Overlap_image.png')