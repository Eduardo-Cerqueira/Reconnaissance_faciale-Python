import cv2

# Ouvre appareil à l'id 0
cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Impossible d'ouvrir l'appareil vidéo")

# Résolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) # Résolution en Largeur

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # Résolution en Hauteur

while(True):
    ret,frame = cap.read() # Capture image par image (frame-by-frame)
    cv2.imshow('preview',frame) # Affichage de l'image finale (frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Touche de l'utilisateur pour arrêter le programme
        break

cap.release()
cv2.destroyAllWindows


