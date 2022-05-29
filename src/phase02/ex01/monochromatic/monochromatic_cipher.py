from matplotlib import image
import random

GRAYSCALE_MAX = 255
GRAYSCALE_MIN = 0

RECT_TOP_INDEX = 0
RECT_BOTTOM_INDEX = 1
RECT_LEFT_INDEX = 2
RECT_RIGHT_INDEX = 3


def monochromatic_cipher(input_file, output_file, rect):
    """
    Ciphers an image using a monochromatic cipher.

    :param input_file: the input image file to cipher
    :param output_file: the output image file to write the ciphered image to
    :param rect: the rectangular region of the image to cipher (in the format [top, bottom, left, right])

    :return: cipher key
    """

    img = image.imread(input_file)

    img_height = len(img)
    img_width = len(img[0])

    key = [random.randint(GRAYSCALE_MIN, GRAYSCALE_MAX) for _ in range(img_width * img_height * 3)]

    key_c = -1

    rect_height = range(int(rect[RECT_TOP_INDEX] * img_height), int((1 - rect[RECT_BOTTOM_INDEX]) * img_height + 1))
    rect_width = range(int(rect[RECT_LEFT_INDEX] * img_width), int((1 - rect[RECT_RIGHT_INDEX]) * img_width + 1))

    for y in range(img_height):
        for x in range(img_width):
            if y in rect_height and x in rect_width:
                pixel = img[y][x]
                pixel_key = key[key_c := key_c + 1]

                ciphered_pixel = pixel ^ pixel_key
                img[y][x] = ciphered_pixel

    image.imsave(output_file, img, cmap='gray')

    return key


# Cipher lena.bmp
if __name__ == '__main__':
    rectangular_region = (0.2, 0.2, 0.2, 0.2)

    cipher_key = monochromatic_cipher('../../../../docs/CD_TestFiles/lena.bmp', 'lena_cipher.bmp', rectangular_region)
