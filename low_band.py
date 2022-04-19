# Mengimpor Library yang diperlukan
import numpy as np
import pandas as pd
import cv2

# Membaca Gambar
img_root='images'
img_name='Nisfit2.jpg'
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

# Program Filter Mean
kernel = np.ones((10,10),np.float32)/25
lowPass = cv2.filter2D(img,-1, kernel)
lowPass = img - lowPass

# Program Menampilkan Output
cv2.imshow("Low Pass",np.hstack((img, lowPass)))
cv2.waitKey(0)
cv2.destroyAllWindows()


