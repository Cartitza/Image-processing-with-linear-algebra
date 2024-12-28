from Grayscale import grayscale_image
from Shear_Mirror import *

if __name__ == '__main__':
    file = input("Enter file name: ")
    image = shear_image(file, 0.5, 1)

    plt.imshow(np.array(image))
    plt.show()

#TODO
#create interface, since most of the "photoshopping" part is done