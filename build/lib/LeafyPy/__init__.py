import math
import cv2
import numpy

def p(input):
    return input

def aNums(num1, num2):
    return num1 + num2

def sNums(num1, num2):
    return num1 - num2

def dNums(num1, num2):
    return num1 / num2

def mNums(num1, num2):
    return num1 * num2

def pNum(num1, num2):
    return num1**num2

def rtNum(num1, num2):
    return sqrt(num1, num2)

def cNum(num1, num2):
    return num1 % num2

def cam(device):
    cap = cv2.VideoCapture(device)

    while True:
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Camera', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
