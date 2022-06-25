import ctypes

libunary = ctypes.CDLL("./libunary.dll")


def unary_encode(input_file, output_file):
    return libunary.unary_encode(input_file.encode("utf8"), output_file.encode("utf8"))


def unary_decode(input_file, output_file):
    return libunary.unary_decode(input_file.encode("utf8"), output_file.encode("utf8"))
