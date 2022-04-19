# Mengimpor Library yang diperlukan
import numpy as np
import pandas as pd
import cv2

# Membaca gambar
img_root='images'
img_name='Nisfit2.jpg'
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

# Program Filter Bilateral
print("Bilateral Filter")
bilFil = cv2.bilateralFilter(img, 60, 60, 60)

# Program Menampilkan Hasil
cv2.imshow("Filter Bilateral",np.hstack((img, bilFil)))
cv2.waitKey(0)
cv2.destroyAllWindows()

