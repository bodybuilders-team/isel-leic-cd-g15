from matplotlib import image

from src.phase02.ex01.monochromatic.monochromatic_cipher import monochromatic_cipher, RECT_TOP_INDEX, RECT_LEFT_INDEX, \
    RECT_BOTTOM_INDEX, RECT_RIGHT_INDEX


# TODO FIX 32 BIT-COLOR -> SHOULD BE 8 BIT-COLOR
def monochromatic_decipher(input_file, output_file, rect, key):
    """
    Deciphers an image using a monochromatic cipher.

    :param input_file: the input image file to decipher
    :param output_file: the output image file to write the deciphered image to
    :param rect: the rectangular region of the image to decipher (in the format [top, bottom, left, right])
    :param key: the cipher key
    """

    img = image.imread(input_file)

    img_height = len(img)
    img_width = len(img[0])

    key_c = -1

    rect_height = range(int(rect[RECT_TOP_INDEX] * img_height), int((1 - rect[RECT_BOTTOM_INDEX]) * img_height + 1))
    rect_width = range(int(rect[RECT_LEFT_INDEX] * img_width), int((1 - rect[RECT_RIGHT_INDEX]) * img_width + 1))

    for y in range(img_height):
        for x in range(img_width):
            if y in rect_height and x in rect_width:
                pixel = img[y][x]
                key1 = key[key_c := key_c + 1]

                deciphered_pixel = pixel ^ key1
                img[y][x] = deciphered_pixel

    image.imsave(output_file, img, cmap='gray')


# Cipher and decipher lena.bmp
if __name__ == '__main__':
    rectangular_region = (0.2, 0.2, 0.2, 0.2)

    cipher_key = monochromatic_cipher('../../../../docs/CD_TestFiles/lena.bmp', 'lena_cipher.bmp', rectangular_region)

    monochromatic_decipher('lena_cipher.bmp', 'lena_decipher.bmp', rectangular_region, cipher_key)
