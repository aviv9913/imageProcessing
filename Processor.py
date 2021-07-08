from PIL import Image
import numpy as np
import time


class Consts:
    BACKGROUND_COLOR = [0, 0, 0, 0]
    TRANSPARENT_COLOR = [255, 255, 255, 100]
    TRANSPARENT_ALPHA_VALUE = 0
    SOLID_ALPHA_VALUE = 255

class Processor():
    def __init__(self, img_path, final_path=None, override=0, rotate=None):
        self.img_path = img_path
        self.final_path = final_path
        if override == 1:
            self.final_path = img_path
        elif not final_path:
            self.final_path = "".join(img_path.split('.')[0: -1]) + "_processed.png"
        self.rotate = rotate
        image = Image.open(img_path)
        self.img_array = np.array(image, dtype=np.uint8)
        self.before = self.img_array
        if len(self.img_array.shape) < 3:
            raise NameError(img_path, "is not an image, has only", len(self.img_array.shape), " dimensions")

        self.h = self.img_array.shape[0]
        self.w = self.img_array.shape[1]
        self.c = self.img_array.shape[2]
        if self.c < 3 or self.c > 4:
            raise NameError(img_path, "is not a valid RGB or RGBA image")

        self.StartProcess()


    def PreProcessing(self):
        self.img_array = self.img_array.reshape(self.h*self.w, self.c)
        if self.c == 3:
            print(self.img_path, "is RGB image, adding alpha channel")
            alpha_col = np.zeros((self.h*self.w, 1), dtype=np.uint8)
            np.append(self.img_array, alpha_col, axis=1)


    def Process(self):
        # setting whole image alpha to 0
        self.img_array[:, 3] = Consts.SOLID_ALPHA_VALUE
        tmp_col = self.img_array[:, 0].reshape(self.img_array.shape[0], 1)
        result = np.all(self.img_array[:, :-1] == tmp_col, axis=1)
        self.img_array[result, 3] = Consts.TRANSPARENT_ALPHA_VALUE
        tmp_col = np.squeeze(tmp_col, axis=1) != 0
        self.img_array[np.logical_and(result, tmp_col)] = Consts.TRANSPARENT_COLOR



    def PostProcessing(self):
        self.img_array = self.img_array.reshape(self.h, self.w, 4)
        if self.rotate is not None:
            # self.img_array = rotate(self.img_array, angle=45)
            self.img_array = np.rot90(self.img_array, self.rotate['axes'])
        final_img = Image.fromarray(self.img_array)
        final_img.save(self.final_path)
        # final_img.show()


    def StartProcess(self):
        self.PreProcessing()
        self.Process()
        self.PostProcessing()
        self.end = time.time()

