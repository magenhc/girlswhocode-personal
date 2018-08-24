from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im

def show_img(im):
    is.show()

def save_img(im, filename):
    im.save(filename, "jpg")
    show_img(im)
