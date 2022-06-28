import ctypes

lib_unary = ctypes.CDLL("./libunary.dll")

# TODO: comment

def unary_encode(input_file, output_file):
    return lib_unary.unary_encode(input_file.encode("utf8"), output_file.encode("utf8"))


def unary_decode(input_file, output_file):
    return lib_unary.unary_decode(input_file.encode("utf8"), output_file.encode("utf8"))
