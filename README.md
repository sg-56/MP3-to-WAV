# MP3-to-WAV


Here is a Python script that converts MP3 files to WAV format and saves them to the destination folder specified as the second argument. 



This script uses the PyDub library to convert MP3 files to WAV format. PyDub is a Python library for processing audio files. It is a simple and easy-to-use library that supports a wide range of audio formats.

To run this script, you will need to have PyDub installed. You can install it using pip:

```
pip install pydub
```

Save the script as `mp3_to_wav_converter.py` and run it from the command line with the following arguments:

```
python mp3_to_wav_converter.py <mp3_folder> <output_folder>
```

For example:

```
python mp3_to_wav_converter.py mp3_files output_folder
```

This will convert all the MP3 files in the `mp3_files` folder and save the resulting WAV files in the `output_folder`.
