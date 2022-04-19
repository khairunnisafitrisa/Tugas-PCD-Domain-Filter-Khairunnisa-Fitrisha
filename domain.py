# Mengimpor Library yang diperlukan
import numpy as np
import pandas as pd
import cv2

# Program Membaca Gambar
img_root='images'
img_name='Nisfit2.jpg'
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

# Program Filter Domain
domainFilter = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6)

# Program Output
cv2.imshow('Domain Filter',np.hstack((img,domainFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()

