from matplotlib import image
import random


def monochromatic_cipher(input_file, output_file, rect):
    img = image.imread(input_file)

    height = len(img)
    width = len(img[0])

    key = [random.randint(0, 255) for i in range(width * height * 3)]

    key_c = -1

    for y in range(height):
        for x in range(width):
            if rect[0] * height <= y <= (1 - rect[1]) * height and rect[2] * width <= x <= (1 - rect[3]) * width:
                pixel = img[y][x]

                key1 = key[key_c := key_c + 1]

                ciphered_pixel = pixel ^ key1

                img[y][x] = ciphered_pixel

    image.imsave(output_file, img, cmap='gray')

    return key

# TODO FIX 32 BIT-COLOR -> SHOULD BE 8 BIT-COLOR

def monochromatic_decipher(input_file, output_file, rect, key):
    img = image.imread(input_file)

    height = len(img)
    width = len(img[0])

    key_c = -1

    for y in range(height):
        for x in range(width):
            if rect[0] * height <= y <= (1 - rect[1]) * height and rect[2] * width <= x <= (1 - rect[3]) * width:
                pixel = img[y][x]

                key1 = key[key_c := key_c + 1]

                deciphered_pixel = pixel ^ key1

                img[y][x] = deciphered_pixel

    image.imsave(output_file, img, cmap='gray')


cipher_key = monochromatic_cipher('lena.bmp', 'lena_cipher.bmp', (0.2, 0.2, 0.2, 0.2))

monochromatic_decipher('lena_cipher.bmp', 'lena_decipher.bmp', (0.2, 0.2, 0.2, 0.2), cipher_key)
