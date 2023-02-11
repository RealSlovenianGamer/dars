##essentials
from PIL import Image
import urllib.request
import datetime
import time
##detector
import cv2
import glob
from vehicle_detector import VehicleDetector

url = 'https://kamere.dars.si/kamere/Sentvid_Jug/cam13.jpg'
#i = 0
while True:
    now = datetime.datetime.now() - datetime.timedelta(seconds=5)
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")

    path = "test/" + str(dt_string) + ".jpg"
    urllib.request.urlretrieve(url, path)
    print(dt_string)
    vd = VehicleDetector()

    img = cv2.imread(path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    for box in vehicle_boxes:
            x, y, w, h = box
            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
            cv2.putText(img, "Vozil: " + str(vehicle_count), (20, 50), 0, 2, (300, 200, 0), 3)
    ##cv2.imshow("Cars", img)
    ##img_path.replace("images", "render")
    cv2.imwrite(path, img)
    #i += 1
    #if i > 60:
    #    break
