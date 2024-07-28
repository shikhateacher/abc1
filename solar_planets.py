import cv2

img = cv2.imread('solar-system.jpg')
#cv2.imshow('Output', img)
#cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (80,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (125,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (385,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (450,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (800,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (970,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg', img)