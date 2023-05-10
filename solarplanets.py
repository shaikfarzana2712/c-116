import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(
    img,
    "SUN",
    (50,100),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     2,
    (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (100,250),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (180,180),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (280,270),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (380,180),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (550,400),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     1,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (700,100),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     1,
    (255,255,255)
)

cv2.putText(
    img,
    "Uranus",
    (960,290),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     1,
    (255,255,255)
)

cv2.putText(
    img,
    "Neptune",
    (1080,150),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
     1,
    (255,255,255)
)



cv2.imshow("planets",img)
cv2.waitKey(0)