import time

from Processor import Processor
from PIL import Image
import numpy as np
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


if __name__ == '__main__':
    pass
    # images_folder_path = r'C:\Users\Aviv\Downloads\prototype 02'
    # start = time.time()
    # process_folder(images_folder_path)
    # print("all execution took: ", time.time()-start, " sec")
