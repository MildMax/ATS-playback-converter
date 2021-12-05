# Automatic Transcription Audio Player

The `run.py` tool is designed to automate the process of playing `.mp3` files in succession from your local machine. An additional `convert.py` tool has been included to assist in converting generic non-mp3 files to the `.mp3` format.

To install the necesssary dependencies from this project, run the following command from the terminal:

```
pip install -r requirements.txt
```

This software was written using Python v3.9.2.

## Playing audio files

The names of audio files played over the course of the experiments will be written to a local file `files_played.txt`. If multiple experiments are conducted, previous versions of this file *will be overwritten*. Either rename the file to prevent overwriting, or move the file to another location.

The program will run until all files in the source directory have been played. The experiment may be stopped prematurely with `ctrl-c`. Files played will still be written to `files_played.txt` including any interrupted file being played.

To play the audio with the default settings, run the following command from the terminal:

```
python run.py
```

### Source Files

Source files can be placed in the local `source` directory, or may be supplied with an absolute path to the `--source` command line argument. 

To provide a different source directory, run the following command from the terminal:

```
python run.py --source path/to/source/directory
```

### Delay

The delay between audio files is by default 30 seconds, though this value may be changed by supplying the delay in seconds to the `--delay` command line argument.

To provide a different delay value, run the following command from the terminal (in this instance, 20 seconds):

```
python run.py --delay 20
```

## Convert Non-MP3 -> MP3

Note:: If no optional command line arguments are supplied for `--source` and `--dest`, files will be read from the local `raw` directory and placed into the local `source` directory.

Note:: The source described for this tool is not the source described in the `run.py` tool!!! Source generically refers to the place from whence the original data came.

### Optional Source

To provide a custom source directory for raw non-mp3 files, run the following command in the terminal:

```
convert.py --source path/to/source/directory
```

### Optional Destination

To provide a custom destination for the resulting `.mp3` files, run the following command in the terminal:

```
convert.py --dest path/to/dest/directory
```