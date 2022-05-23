import tkinter
from PIL import Image, ImageTk
import random
import os

currentDirectory = os.getcwd()

waitTimes = [100,100,100,100,100,250,250,250,250,300,300,500,500]
cycles = 13

# Top level
root = tkinter.Tk()
root.geometry('400x400')
root.title("DnD Roller")

# Frame Label
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# Label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello!", font= "Heveltica 16")
HeadingLabel.pack()

# Image array

d2 = os.listdir(currentDirectory+"\\d2")
d4 = os.listdir(currentDirectory+"\\d4")
d6 = os.listdir(currentDirectory+"\\d6")
d8 = os.listdir(currentDirectory+"\\d8")
d10 = os.listdir(currentDirectory+"\\d10")
d12 = os.listdir(currentDirectory+"\\d12")
d20 = os.listdir(currentDirectory+"\\d20")
d100 = os.listdir(currentDirectory+"\\d100")

