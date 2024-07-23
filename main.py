# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import cmath

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def softmax(vec):
    arr = np.zeros(len(vec), dtype=np.complex_)
    sum = 0
    for item in vec:
        sum += math.e ** item
    for i in range(len(vec)):
        arr[i] = cmath.sqrt(cmath.e ** vec[i] / sum)
    return arr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    vec = [-3+1j,-3+1j,-3-1j,3+1j]
    ls1 = softmax(vec)
    sum = 0
    print(ls1)
    for item in ls1:
        sum += item
    print(sum)
    test_np = np.zeros(3)
    print(test_np)


    # vgg16_general = plt.imread('MLFinalImage/image/VGG16_general.png')
    # vgg16_mel = plt.imread('MLFinalImage/image/VGG16_MEL.png')
    # vgg19_general = plt.imread('MLFinalImage/image/VGG19_general.png')
    # vgg19_mel = plt.imread('MLFinalImage/image/VGG19_MEL.png')
    # mobilenetv2_general = plt.imread('MLFinalImage/image/MobileNetV2_general.png')
    # mobilenetv2_mel = plt.imread('MLFinalImage/image/MobileNetV2_MEL.png')
    # resnet50_general = plt.imread('MLFinalImage/image/ResNet50_General.png')
    # resnet50_mel = plt.imread('MLFinalImage/image/ResNet50_MEL.png')
    # alexnet_general = plt.imread('MLFinalImage/image/AlexNet_General.png')
    # alexnet_mel = plt.imread('MLFinalImage/image/AlexNet_MEL.png')
    #
    # plt.rcParams.update({
    #     'font.size': 5  # 设置字体大小为14
    # })
    # plt.figure(figsize=(10,6))
    # plt.subplot(3,4,1)
    # plt.imshow(mobilenetv2_general)
    # plt.axis('off')
    # plt.title('MobileNetV2 General')
    #
    # plt.subplot(3,4,2)
    # plt.imshow(mobilenetv2_mel)
    # plt.axis('off')
    # plt.title('MobileNetV2 MEL')
    #
    # plt.subplot(3,4,3)
    # plt.imshow(vgg16_general)
    # plt.axis('off')
    # plt.title('VGG16 General')
    #
    # plt.subplot(3,4,4)
    # plt.imshow(vgg16_mel)
    # plt.axis('off')
    # plt.title('VGG16 MEL')
    #
    # plt.subplot(3,4,5)
    # plt.imshow(vgg19_general)
    # plt.axis('off')
    # plt.title('VGG19 General')
    #
    # plt.subplot(3,4,6)
    # plt.imshow(vgg19_mel)
    # plt.axis('off')
    # plt.title('VGG19 MEL')
    #
    # plt.subplot(3,4,7)
    # plt.imshow(resnet50_general)
    # plt.axis('off')
    # plt.title('ResNet50 General')
    #
    # plt.subplot(3,4,8)
    # plt.imshow(resnet50_mel)
    # plt.axis('off')
    # plt.title('ResNet50 MEL')
    #
    # plt.subplot(3,4,9)
    # plt.imshow(alexnet_general)
    # plt.axis('off')
    # plt.title('AlexNet General')
    #
    # plt.subplot(3,4,10)
    # plt.imshow(alexnet_mel)
    # plt.axis('off')
    # plt.title('AlexNet MEL')
    #
    # plt.show()
    # print_hi('PyCharm')

    # x = np.arange(-10, 10, 0.01)
    # y = 1 / (1 + math.e ** (-x))
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.plot(x,y)
    # plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
