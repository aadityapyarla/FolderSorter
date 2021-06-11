import os
import sys
import shutil
from time import sleep
from extensions import extension_paths

image_ext = [".png", ".jpg", ".jpeg"]
doc_ext = [".txt", ".docx", ".doc", ".pdf"]
media_ext = [".mp4", ".mp3", ".MOV", ".flv", ".aviv"]



def ifNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)



files = os.
