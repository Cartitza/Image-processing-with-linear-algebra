from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


def shear_image(file: str, up: float, left:float):

    image = Image.open('./Images/' + file + '.png')
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
#fa sa nu mai apara pixeli negri random
#MAYBE turn it all into a class, idk


def mirror_image(file: str, axis: str):

    image = Image.open('./Images/' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    if axis == 'x':
        test = [[1, 0], [0, -1]]
    elif axis == 'y':
        test = [[-1, 0], [0, 1]]
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


def shear_image_right(file: str, right: float):

    image = Image.open('./Images/' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    temp = mirror_image(file, 'x')
    temp.save('./' + file + '_temp.png')

    temp_2 = shear_image(file + '_temp', 0, right)
    temp_2.save('./' + file + '_temp.png')

    sheared_image = mirror_image(file + '_temp', 'x')

    os.remove('./' + file + '_temp.png')
    return sheared_image


def shear_image_down(file: str, down: float):

    image = Image.open('./Images/' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)
    img.setflags(write=True)

    temp = mirror_image(file, 'y')
    temp.save('./' + file + '_temp.png')

    temp_2 = shear_image(file + '_temp', down, 0)
    temp_2.save('./' + file + '_temp.png')

    sheared_image = mirror_image(file + '_temp', 'y')

    os.remove('./' + file + '_temp.png')
    return sheared_image