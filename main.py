# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Reorganize and rename music files for Plex
# author            : LikeToAccess
# email             : liketoaccess@protonmail.com
# date              : 02-28-2022
# version           : v1.0
# usage             : python main.py
# notes             : https://support.plex.tv/articles/200265296-adding-music-media-from-folders/
# license           : MIT
# py version        : 3.10.2 (must run on 3.6 or higher)
#==============================================================================
import os
from settings import *


class Song:
	def __init__(self, audio_file):
		self.audio_file = audio_file


def main():
	audio_files = os.listdir(os.path.abspath(MUSIC_PATH))
	for audio_file in audio_files:
		if audio_file.split(".")[-1] not in VALID_AUDIO_FILE_FORMATS:
			continue
		print(audio_file)



if __name__ == "__main__":
	main()
