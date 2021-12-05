import os
from argparse import ArgumentParser
import platform

def main(source: str, dest: str, is_win):    
    # remove any added slashes
    source = source.rstrip('/').rstrip('\\')
    dest = dest.rstrip('/').rstrip('\\')
    for file_name in os.listdir(source):
        full_in_path = f'{source}/{file_name}'
        full_out_path = f'{dest}/{"".join(file_name.split(".")[:-1])}.mp3'
        if is_win:
            full_in_path = f'{source}\\{file_name}'
            full_out_path = f'{dest}\\{"".join(file_name.split(".")[:-1])}.mp3'
        print(f'***************** Processing {file_name} ******************')
        os.system(f"ffmpeg -i {full_in_path} {full_out_path}")

def parse_args(is_win):
    # set correct path based on operating system
    out_dir = f'{os.getcwd()}/source'
    in_dir = f'{os.getcwd()}/raw'
    if is_win:
        out_dir = f'{os.getcwd()}\\source'
        in_dir = f'{os.getcwd()}\\raw'

    parsed_args = ArgumentParser(description='Run automatic transcription experiment')
    parsed_args.add_argument('--dest', help='destination directory for mp3 files', type=str, default=out_dir)
    parsed_args.add_argument('--source', help='source directory containing raw non-mp3 files', type=str, default=in_dir)
    return parsed_args.parse_args()


if __name__ == "__main__":
    # determine os for path creation
    is_win = False
    if platform.system().lower() == 'windows':
        is_win = True
    parsed_args = parse_args(is_win)
    main(parsed_args.source, parsed_args.dest, is_win)
