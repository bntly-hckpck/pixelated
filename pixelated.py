from PIL import Image

# image uploading method
def img_upload(path):

    img = Image.open(path) # loads image from given path
    return img

# pixelated image method
def pixelated_img(img, blocks = 64, n_colors = 64):

    width, height = img.size # save original image x and y
    scale_factor = min(width, height) / blocks # "take shortest side and divide into blocks"
    new_width = int(width / scale_factor) # new x
    new_height = int(height / scale_factor) # new y
    img_resized = img.resize((new_width, new_height)) # downscale image
    img_posterized = img_resized.quantize(colors = n_colors) # keep most representative colors, avoids blur
    final_img = img_posterized.resize((width, height), Image.Resampling.NEAREST) # upscale back + nearest-neighbor resampling
    return final_img

if __name__ == "__main__":
    img = img_upload("photo_input.png") # open input image
    converted_img = pixelated_img(img, 64, 64) # pixelation, 64 blocks, 64 colors
    converted_img.save("photo_output.png") # save output as new image
