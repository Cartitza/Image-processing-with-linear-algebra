from Grayscale import grayscale_image
from Shear_Mirror import *

if __name__ == '__main__':
    file = input("Enter file name: ")
    image = shear_image(file, 0, 0.5)
    image.save('./test.png')

    image_2 = mirror_image('test')
    plt.imshow(np.array(image_2))
    plt.show()
