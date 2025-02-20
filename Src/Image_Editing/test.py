from Src.Image_Editing.Shear_Mirror import *
from Rotation import *

if __name__ == '__main__':
    file = input("Enter file name: ")
    image = shear_image(file, 0.5, 1)
    #image = rotate_image(file, 120)
    plt.imshow(np.array(image))
    plt.show()

#TODO
#create interface, since most of the "photoshopping" part is done
#look into bilinear interpolation