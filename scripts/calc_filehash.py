import argparse
import hashlib

HASH_ALGORITHM = 'sha1'

def calc_hash(file):
    # ファイルのハッシュを計算する
    hash_obj = hashlib.new(HASH_ALGORITHM)
    length = hash_obj.block_size * 0x800
    '''
    with open(file, 'rb') as f:
        BinaryData = f.read(length)
        while BinaryData:
            h.update(BinaryData)
            BinaryData = f.read(length)
    '''
    BinaryData = file.read(length)
    while BinaryData:
        hash_obj.update(BinaryData)
        BinaryData = file.read(length)

    return hash_obj.hexdigest()


def parse_command_line_arguments():
    """
    コマンドラインの引数の受け取り
    """
    parser = argparse.ArgumentParser(description='calc file hash')
    parser.add_argument('file_path', nargs='+', type=argparse.FileType('rb'), default='', help='filepath')
    args = parser.parse_args()
    file_paths = args.file_path
    return file_paths


if __name__ == '__main__':
    file_paths = parse_command_line_arguments()
    for file_path in file_paths:
        filehash = calc_hash(file_path)
        print(filehash)
