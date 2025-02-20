from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load and convert image

def rotate_image(file: str, degrees_clockwise: float):

    image = Image.open('./static/images/' + file + '.png')
    image = image.convert('RGB')
    img = np.array(image)

    t = degrees_clockwise * np.pi / 180

    rotation_matrix = np.array([[np.cos(t), -np.sin(t)],
                                [np.sin(t), np.cos(t)]])

    height, width = img.shape[:2]

    corners = np.array([[0, 0], [0, width-1], [height-1, 0], [height-1, width-1]])
    rotated_corner_j = []
    rotated_corner_i = []

    for corner in corners:
        rotated_corner_j.append(np.dot(rotation_matrix, corner)[0])
        rotated_corner_i.append(np.dot(rotation_matrix, corner)[1])


    max_H = int(max(rotated_corner_j) - min(rotated_corner_j)) + 1
    max_W = int(max(rotated_corner_i) - min(rotated_corner_i)) + 1

    rotated_image = np.zeros((max_H, max_W, 3))
    rotated_image.setflags(write=True)

    for i in range(max_W):
        for j in range(max_H):
            new_j, new_i = np.dot(rotation_matrix, [j - max_H / 2, i - max_W / 2]) + [height / 2, width / 2]

            if 0 <= new_j < height and 0 <= new_i < width:
                rotated_image[j, i] = img[int(new_j), int(new_i)]

    rotated = Image.fromarray(rotated_image.astype('uint8'))
    return rotated