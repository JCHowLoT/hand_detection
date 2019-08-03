import cv2
import os


data_path = '/media/j/DA18EBFA09C1B27D/1/dep_r1000_n357'
save_path = '/media/j/DA18EBFA09C1B27D/1/gbr_r1000_n357'
filename = os.listdir(data_path)
i = 0


for fname in filename:
    path = data_path + "/" + fname
    save_path = save_path
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    im_gray = im_gray * 16
    im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
    cv2.imshow('img', im_color)
    save_img = save_path + "/" + fname
    print(save_img)
    cv2.imwrite(save_img, im_color)
    cv2.waitKey(0)
    i += 1
    print('num = ', i)
