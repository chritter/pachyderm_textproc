import os
import argparse

if __name__ == '__main__':

    # parse command line arguments
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('--input_path', type=str, help='Path to input txt data to process')
    arg('--output_path', type=str, help='Path to write processed output data')
    args = parser.parse_args()


    def split_text(file):
        '''
        Splits first line in file into entries separated by comma and writes into csv file.
        :param file: filename from which to read first line
        :return: None
        '''
        with open(file) as f:
            line = f.readline()
        line_split = ','.join(line.split())

        # input_path "/pfs/out"
        file_name = file.split('/')[-1].replace('.txt', '') + '_processed.csv'
        save_path_file = os.path.join(args.output_path, file_name)
        print(save_path_file)
        with open(save_path_file, 'w') as f:
            f.write(line_split)


    # walk /pfs/images and call make_edges on every file found; "/pfs/texts"
    for dirpath, dirs, files in os.walk(args.input_path):
        for file in files:
            print(file)
            split_text(os.path.join(dirpath, file))
