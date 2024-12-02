import hashlib

def hash_file(file_path):
    """
    Generates a SHA-256 hash for the contents of a given file.

    :param file_path: Path to the file to hash.
    :return: Hexadecimal hash string.
    """
    hash_algorithm = hashlib.sha256()  # You can use sha1, sha256, etc.
    with open(file_path, "rb") as f:   # Read the file in binary mode
        while chunk := f.read(8192):  # Process the file in chunks to handle large files
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()
