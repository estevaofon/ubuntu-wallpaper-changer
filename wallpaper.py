#!/usr/bin/python3
import os
import glob
import random

# Para saber qual comando usar digite no terminal
# gnome-session --version
# Isso retonara sua versao gnome, se inicia com 3, entao pode usar gsettings,
# se iniciar com 2 use gconftool

directory = (os.path.dirname(os.path.abspath(__file__)))
png_files = glob.glob(os.path.join(directory, '*.png'))
jpg_files = glob.glob(os.path.join(directory, '*.jpg'))
wallpapers = png_files + jpg_files
img_file = random.choice(wallpapers)
filepath = "file://"+os.path.join(directory, img_file)
command = "gsettings set org.gnome.desktop.background picture-uri {}".format(filepath)
os.system(command)
