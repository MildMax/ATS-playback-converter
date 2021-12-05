import os
from pygame import mixer
from mutagen.mp3 import MP3
import time
import os
from argparse import ArgumentParser
import signal
import sys
import platform

files = []

def write_files_played():
    result_file = 'files_played.txt'
    with open(result_file, 'w') as f:
        for file_name in files:
            f.write(f'{file_name}\n')
    print(f'Captured files written to {result_file}')


def signal_handler(sig, frame):
    mixer.music.stop()
    mixer.music.unload()

    write_files_played()

    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

def main(delay_arg, source_arg, is_win):

    print("Playing Audio")
    print()
    mixer.init()

    for file_name in os.listdir(source_arg):
        files.append(file_name)
        mp3_file = f'{source_arg}/{file_name}'
        if is_win:
            mp3_file = f'{source_arg}\\{file_name}'

        # play files
        audio_file = MP3(mp3_file)
        play_time = audio_file.info.length
        print(f'Playing {mp3_file}')
        print()

        mixer.music.load(mp3_file)
        mixer.music.play()

        # wait for file to finish playing
        time.sleep(play_time + delay_arg)

        mixer.music.stop()
        mixer.music.unload()

    print('All audio played')

    write_files_played()


def parse_args(is_win):
    # set correct path based on operating system
    default_dir = f'{os.getcwd()}/source'
    if is_win:
        default_dir = f'{os.getcwd()}\\source'

    parsed_args = ArgumentParser(description='Run automatic transcription experiment')
    parsed_args.add_argument('--source', help='directory containing mp3 source files', type=str, default=default_dir)
    parsed_args.add_argument('--delay', help='delay in seconds between recordings', type=int, default=30)
    return parsed_args.parse_args()


if __name__ == "__main__":
    # determine os for path creation
    is_win = False
    if platform.system().lower() == 'windows':
        is_win = True
    parsed_args = parse_args(is_win)
    input('press enter key to continue')
    main(parsed_args.delay, parsed_args.source, is_win)
