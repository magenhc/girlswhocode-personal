import filters

def main():
filename = input("Enter the name of the image to edit: ")

img = filters.load_img(filename)

filters.save_img(img, "recolored.jpg")

if __name__=='__main__'
    main()
