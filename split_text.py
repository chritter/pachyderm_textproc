import os


def split_text(file):
    '''
    Splits first line in file into entries separated by comma and writes into csv file.
    :param file: filename from which to read first line
    :return: None
    '''
    with open(file) as f:
        line = f.readline()
    line_split = ','.join(line.split())

    save_path_file = os.path.join("/pfs/out", file.replace('.txt', '') + '_processed.csv')

    with open(save_path_file, 'w') as f:
        f.write(line_split)


# walk /pfs/images and call make_edges on every file found
for dirpath, dirs, files in os.walk("/pfs/texts"):
    for file in files:
        split_text(os.path.join(dirpath, file))
