import sys
import os
from PIL import Image

#get the source and the export folder from the terminal
source_folder = sys.argv[1]
export_folder = sys.argv[2]
#check if the folders are exist, if not creat them
def check_folder(folder):
    if not(os.path.isdir(folder)):
        os.mkdir(folder)
#start the convert function
def convert(source,export)->Image:
    files_list = os.listdir(source)
    if len(files_list) > 0:
        image_list = []
        for file in files_list:
            if file.split(".")[1] == 'jpg'.casefold():
                image_list.append(file)
        for image in image_list:
            png_image = Image.open(source+image)
            png_image.save((export+image.split('.')[0]+".png"),'png')
            print(f"Done With {image}")
    else:
        print("No Files found in the folder!")
try:
    check_folder(source_folder)
    check_folder(export_folder)
    convert(source_folder,export_folder)
except:
    print("Enter the name of the source and the output folders !")