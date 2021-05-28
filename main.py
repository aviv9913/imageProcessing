from Processor import Processor, Consts
from PIL import Image
import numpy as np

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



if __name__ == '__main__':
    # test_processor()

    p = Processor("images/Prototype.png")
