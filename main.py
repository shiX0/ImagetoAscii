import cv2 as cv
from tqdm import tqdm
import argparse

def imgtoascii(filepath):
    img = cv.imread(filepath)
    stri = ""
    height=200
    width=300
    dim=(width,height)
    resizedimg=cv.resize(img,dim,interpolation=cv.INTER_AREA)
    print(resizedimg.shape)

    gray_img=cv.cvtColor(resizedimg,cv.COLOR_BGR2GRAY)
    for x in tqdm(range(gray_img.shape[0])):
        for y in range(gray_img.shape[1]):
            brightness = gray_img[x,y]
            if brightness < 50:
                stri = stri + "_"
            elif 50 <= brightness < 100:
                stri = stri + "░"
            elif 100 <= brightness < 150:
                stri = stri + "▓"
            else:
                stri = stri + "."
        stri = stri + "\n"
    with open(f"{filepath}.txt","w",encoding="utf-8") as a:
        a.write(stri)
        print(f"written the ascii into {filepath}.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to ASCII art.')
    parser.add_argument('input_file', help='Input image file path')
    args = parser.parse_args()
    imgtoascii(args.input_file)