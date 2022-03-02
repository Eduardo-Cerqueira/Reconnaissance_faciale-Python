import cv2

classifier = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Impossible d'ouvrir l'appareil vidéo")


cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) # Résolution en Largeur
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # Résolution en Hauteur

while (cap.isOpened()):
    ret, frame=cap.read()
    Image_Noir_Blanc = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Conversion en Noir et Blanc
    visage = classifier.detectMultiScale(Image_Noir_Blanc, scaleFactor=1.2, minNeighbors=3) # Détection

    for x,y,w,h in visage:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Dessin du carré/rectangle
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow("Reconnaissance Faciale :D", frame)

cap.release()
cv2.destroyAllWindows() # Ferme les fênetres