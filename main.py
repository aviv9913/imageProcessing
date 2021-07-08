import time

from Processor import Processor
import shutil
import os
from tqdm import tqdm

def test_processor(path):
    not_images = 0
    numOfImages = 1000
    files = os.listdir(path)
    print(files[0::numOfImages])
    for filename in tqdm(files[0::numOfImages]):
        if filename.endswith(".png"):
            filename_without_suffix = os.path.splitext(filename)[0]
            image_path = os.path.join(path, filename)
            final_folder = os.path.join(path, "TestExamples")

            try:
                os.mkdir(final_folder)
            except FileExistsError:
                pass

            final_path = os.path.join(final_folder, filename_without_suffix + "_processed.png")
            Processor(image_path, final_path=final_path, rotate={'axes': 1})
        else:
            not_images += 1


def process_folder(path):
    start = time.time()
    not_images = 0
    print("start processing files in: ", path)
    for filename in tqdm(os.listdir(path)):
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
    print("Processing Time: ", time.time()-start, " sec")


def rename_images(path, isReversed):
    start = time.time()
    index = 0
    prefix = 'bottom_stack_'
    images_in_path = [float((''.join(f.split('_')[0])[5:])) for f in os.listdir(path) if f.endswith(".png")]
    print("start renaming files in: ", path)
    for filename in tqdm(sorted(os.listdir(path), key=lambda f: float((''.join(f.split('_')[0])[5:])), reverse=isReversed)):
        image_path = os.path.join(path, filename)
        final_folder = os.path.join(path, "Processed_with_renaming")

        try:
            os.mkdir(final_folder)
        except FileExistsError:
            pass

        str_index = f'{index:05}'
        final_path = os.path.join(final_folder, prefix + str_index + ".png")
        shutil.copyfile(image_path, final_path)
        index += 1
    print("total number of files renamed:", index+1)
    print("Renaming Time: ", time.time() - start, " sec")


if __name__ == '__main__':
    images_folder_path = r'C:\Users\Aviv\Downloads\Outer sphere v7 20cm\ver 10\part 1'
    process_folder(images_folder_path)
    processed_folder_path = os.path.join(images_folder_path, "Processed")
    rename_images(processed_folder_path, False)
    # test_processor(images_folder_path)
