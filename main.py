import time

from Processor import Processor
from PIL import Image
import numpy as np
import os
import shutil
import os


def test_processor():
    folder = "test_images/"
    fileprefix = "GershonExample"
    for i in range(1, 4):
        original_path = folder + fileprefix + str(i) + ".png"
        final_path = folder + fileprefix + str(i) + "_processed.png"

        Processor(original_path, final_path=final_path)
        original = Image.open(original_path)
        original = np.array(original, dtype=np.uint8)

        processed = Image.open(final_path)
        processed = np.array(processed, dtype=np.uint8)
        dif = original == processed
        if not dif.all():
            print(original_path, "test didn't passed, printing differences")


def process_folder(path):
    not_images = 0
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".png"):
            filename_without_suffix = os.path.splitext(filename)[0]
            image_path = os.path.join(path, filename)
            final_folder = os.path.join(path, "Processed")

            try:
                os.mkdir(final_folder)
            except FileExistsError:
                pass

            final_path = os.path.join(final_folder, filename_without_suffix + "_processed.png")
            Processor(image_path, final_path=final_path)
        else:
            not_images+=1
    print("total number of files processed:", len(os.listdir(path)) - not_images)


def rename_images(path):
    index = 0
    images_in_path = [float((''.join(f.split('_')[0])[5:])) for f in os.listdir(path) if f.endswith(".png")]
    for filename in sorted(os.listdir(path), key=lambda f: float((''.join(f.split('_')[0])[5:]))):
        print("renaming layer image ", filename)
        image_path = os.path.join(path, filename)
        final_folder = os.path.join(path, "Processed_with_renaming")

        try:
            os.mkdir(final_folder)
        except FileExistsError:
            pass

        str_index = f'{index:05}'
        prefix = 'prototype_'
        final_path = os.path.join(final_folder, prefix + str_index + ".png")
        if filename == "Value8.228_Top_processed.png":
            print("copying layer 8.228")
            for i in range(60):
                shutil.copyfile(image_path, final_path)
                index += 1
                str_index = f'{index:05}'
                final_path = os.path.join(final_folder, prefix + str_index + ".png")
        else:
            shutil.copyfile(image_path, final_path)
            index += 1
    print("total number of files processed:", index+1)



if __name__ == '__main__':
    path = r'C:\Users\aviv\Downloads\prototype 02\Processed\Processed_with_renaming'
    print(os.listdir(path))
    # start = time.time()
    # process_folder(images_folder_path)
    # print("all execution took: ", time.time()-start, " sec")
    # rename_images(path)
