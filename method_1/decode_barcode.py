from pyzbar import pyzbar
import time
import cv2

def decode(image_name):
    start_time = time.time()

    image = cv2.imread(cv2.samples.findFile(image_name), cv2.IMREAD_COLOR)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        src = cv2.GaussianBlur(image, (3, 3), 0)
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(src_gray, 20, 30)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imwrite("result.png", image)
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        finish_time = time.time()
        print("Time:", finish_time-start_time)
        cv2.imshow("Image", image)
        cv2.waitKey(0)



if __name__ == '__main__':
    decode("barcode.jpg")