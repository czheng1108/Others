import cv2
import math
import os
# noinspection PyUnresolvedReferences
import numpy as np
from PIL import Image
from pathlib import Path
Image.MAX_IMAGE_PIXELS = None
IMAGES_FORMAT = ['.png']  # 图片格式
#IMAGES_FORMAT = ['.tif']
#src = input('请输入图片文件路径：')
src = r'E:\crop\png'
print(src)

#list = os.listdir(src)
#dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
dstpath = r'E:\crop\after'

image_names = [name for name in os.listdir(src) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]

for i, sample in enumerate(image_names):
        print(sample)
        file_name = src +'/'+ str(sample)
        save_path = dstpath + str(sample[:-4]) + '/'
        Path(save_path).mkdir(parents=True, exist_ok=True)

        # block size
        height = 1000
        width = 1000

        # overlap
        over_x = 0
        over_y = 0
        h_val = height - over_x
        w_val = width - over_y

        # Set whether to discard an image that does not meet the size
        mandatory = False
        print(str(file_name))
        img = cv2.imread(file_name)

        #print(img.shape)
        # original image size
        original_height = img.shape[0]
        original_width = img.shape[1]

        #max_row = float((original_height - height) / h_val)  # + 1
        #max_col = float((original_width - width) / w_val)  # + 1
        max_row = float(original_height/ h_val)  # + 1
        max_col = float(original_width/ w_val)  # + 1

        # block number
        max_row = math.ceil(max_row) if mandatory == False else math.floor(max_row)
        max_col = math.ceil(max_col) if mandatory == False else math.floor(max_col)

        print(max_row)
        print(max_col)

        images = []
        for i in range(max_row):
            images_temp = []
            for j in range(max_col):
                temp_path = save_path + '/' + str(i) + '_' + str(j) + '_'
                if ((width + j * w_val) > original_width and (
                        i * h_val + height) <= original_height):  # Judge the right most incomplete part
                    temp = img[i * h_val:i * h_val + height, j * w_val:original_width, :]
                    temp_path = temp_path + str(temp.shape[0]) + '_' + str(temp.shape[1]) + '.png'
                    #temp = temp[:, :, 0]
                    cv2.imwrite(temp_path, temp)
                    images_temp.append(temp)
                elif ((height + i * h_val) > original_height and (
                        j * w_val + width) <= original_width):  # Judge the incomplete part at the bottom
                    temp = img[i * h_val:original_height, j * w_val:j * w_val + width, :]
                    temp_path = temp_path + str(temp.shape[0]) + '_' + str(temp.shape[1]) + '.png'
                    #temp = temp[:, :, 0]
                    cv2.imwrite(temp_path, temp)
                    images_temp.append(temp)
                elif ((width + j * w_val) > original_width and (
                        i * h_val + height) > original_height):  # Judge the last slide
                    temp = img[i * h_val:original_height, j * w_val:original_width, :]
                    temp_path = temp_path + str(temp.shape[0]) + '_' + str(temp.shape[1]) + '.png'
                    #temp = temp[:, :, 0]
                    cv2.imwrite(temp_path, temp)
                    images_temp.append(temp)
                else:
                    temp = img[i * h_val:i * h_val + height, j * w_val:j * w_val + width, :]
                    temp_path = temp_path + str(temp.shape[0]) + '_' + str(temp.shape[1]) + '.png'
                    #temp = temp[:, :, 0]
                    cv2.imwrite(temp_path, temp)
                    images_temp.append(temp)  # The rest of the complete

            images.append(images_temp)

        print(len(images))


#file_name = "/Users/liuhongyan/xiangmu/data/gjb_bandao.png"#输入图像路径
#save_path = '/Users/liuhongyan/xiangmu/data/small_0/'  # 输出图像的路径
#Path(save_path).mkdir(parents=True, exist_ok=True)



