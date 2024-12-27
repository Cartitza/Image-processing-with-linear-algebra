from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def grayscale_image(file: str):

    grayscale = ([0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33])
    grayscale_matrix = np.asarray(grayscale)
    #test = [65, 90, 20]
    #test_vector = np.asarray(test)
    #file = input()
    #print(np.dot(grayscale_matrix, test_vector).round())
    image = Image.open('./' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    for i in range(img.shape [1]):
        for j in range(img.shape [0]):
            img[j, i] = np.dot(grayscale_matrix, img[j, i]).round()

    #print(img)
    #plt.imshow(img)
    #plt.show()
    img_grayscale = Image.fromarray(img)
    img_grayscale = img_grayscale.convert('L')
    img_grayscale.save('./' + file + '_grayscale.png')
    return img_grayscale
