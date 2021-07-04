import time

from Processor import Processor
from PIL import Image
import numpy as np
import os
import shutil
import os


def test_processor(path):
    i = 0
    not_images = 0
    numOfImages = 100
    for filename in os.listdir(path):
        if i % numOfImages != 0:
            i += 1
            continue

        if filename.endswith(".png"):
            filename_without_suffix = os.path.splitext(filename)[0]
            image_path = os.path.join(path, filename)
            final_folder = os.path.join(path, "TestExamples")

            try:
                os.mkdir(final_folder)
            except FileExistsError:
                pass

            final_path = os.path.join(final_folder, filename_without_suffix + "_processed.png")
            Processor(image_path, final_path=final_path, TransparentColor=[255, 255, 255, 100])
        else:
            not_images += 1
        i += 1

def process_folder(path):
    not_images = 0
    for filename in os.listdir(path):
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
        image_path = os.path.join(path, filename)
        final_folder = os.path.join(path, "Processed_with_renaming")

        try:
            os.mkdir(final_folder)
        except FileExistsError:
            pass

        str_index = f'{index:05}'
        prefix = 'prototype_'
        final_path = os.path.join(final_folder, prefix + str_index + ".png")
        shutil.copyfile(image_path, final_path)
        index += 1
    print("total number of files processed:", index+1)



if __name__ == '__main__':
    images_folder_path = r'C:\Users\Aviv\Downloads\TmpForMOP\part 2'
    start = time.time()
    process_folder(images_folder_path)
    # test_processor(images_folder_path)
    print("Processing Time: ", time.time()-start, " sec")
    start = time.time()
    processed_folder_path = os.path.join(images_folder_path, "Processed")
    rename_images(processed_folder_path)
    print("Renaming Time: ", time.time() - start, " sec")
