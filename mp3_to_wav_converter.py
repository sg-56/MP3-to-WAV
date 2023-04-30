import os
import argparse
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, output_folder):
    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # convert each mp3 file in the folder to wav format
    for mp3_file in os.listdir(mp3_folder):
        if mp3_file.endswith('.mp3'):
            mp3_path = os.path.join(mp3_folder, mp3_file)
            wav_file = os.path.splitext(mp3_file)[0] + '.wav'
            wav_path = os.path.join(output_folder, wav_file)
            sound = AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MP3 files to WAV format.')
    parser.add_argument('mp3_folder', type=str, help='Folder containing MP3 files.')
    parser.add_argument('output_folder', type=str, help='Folder to save WAV files.')
    args = parser.parse_args()

    convert_mp3_to_wav(args.mp3_folder, args.output_folder)
