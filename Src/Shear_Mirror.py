from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def shear_image(file: str, up: float, left:float):

    image = Image.open('./' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    test = [[1, up], [left, 1]]

    # [[1, 0], [0, -1]] for mirrored
    test_matrix = np.asarray(test)

    max_H, max_W = np.dot(abs(test_matrix), [img.shape[0], img.shape[1]]).round()

    sheared_image = np.zeros((abs(int(max_H)), abs(int(max_W)), 3))
    sheared_image.setflags(write=True)

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            new_j, new_i = np.dot(test_matrix, [j, i]).round()

            sheared_image[int(new_j.round()), int(new_i.round())] = img[j, i]

    #plt.imshow(sheared_image.astype('uint8'))
    #plt.show()
    sheared = Image.fromarray(sheared_image.astype('uint8'))
    return sheared

#TODO
#fa sa mearga shearul si pt dreapta/jos
#fa sa nu mai apara pixeli negri random


def mirror_image(file: str):

    image = Image.open('./' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    test = [[1, 0], [0, -1]]

    # [[1, 0], [0, -1]] for mirrored
    test_matrix = np.asarray(test)

    max_H, max_W = np.dot(abs(test_matrix), [img.shape[0], img.shape[1]]).round()

    mirrored_image = np.zeros((abs(int(max_H)), abs(int(max_W)), 3))
    mirrored_image.setflags(write=True)

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            new_j, new_i = np.dot(test_matrix, [j, i]).round()

            mirrored_image[int(new_j.round()), int(new_i.round())] = img[j, i]

    #plt.imshow(sheared_image.astype('uint8'))
    #plt.show()
    mirrored = Image.fromarray(mirrored_image.astype('uint8'))
    return mirrored