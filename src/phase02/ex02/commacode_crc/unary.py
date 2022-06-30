import ctypes

lib_unary = ctypes.CDLL("./libunary.dll")


def unary_encode(input_file_path, output_file_path):
    """
    Encodes the file @ input_file_path with comma code encoding and
    writes the result to a new file @ output_file_path
    """

    return lib_unary.unary_encode(input_file_path.encode("utf8"), output_file_path.encode("utf8"))


def unary_decode(input_file_path, output_file_path):
    """
    Encodes the file @ input_file_path with comma code encoding and
    writes the result to a new file @ output_file_path
    """
    return lib_unary.unary_decode(input_file_path.encode("utf8"), output_file_path.encode("utf8"))
