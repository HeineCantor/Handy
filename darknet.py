import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

CFG_PATH = 'yolov3.cfg'

def downsampleSequential(batchNorm, inputChannels, outputChannels, size, stride, pad, leakyActivation):
    module_list = []

    if pad:
        pad = size - 1
    else:
        pad = 0

    convLayer = nn.Conv2d(inputChannels, outputChannels, kernel_size=size, stride=stride, padding=pad, bias=(batchNorm==0))
    module_list.append(convLayer)

    if batchNorm:
        batchNormLayer = nn.BatchNorm2d(outputChannels)
        module_list.append(batchNormLayer)

    if leakyActivation:
        activationFunction = nn.LeakyReLU(0.1, inplace=True)
        module_list.append(activationFunction)

    return nn.Sequential(
        *module_list
    )

class ResidualConvolutionalBlock(nn.Module):
    def __init__(self, inputChannels):
        super(ResidualConvolutionalBlock, self).__init__()

        self.inputChannels = inputChannels
        doubledChannels = inputChannels * 2

        self.downSequence = downsampleSequential(1, doubledChannels, inputChannels, 1, 1, 1, True)

        self.upSequence = downsampleSequential(1, inputChannels, doubledChannels, 3, 1, 1, True)
    
    def forward(self, x):
        out = self.downSequence(x)
        out = self.upSequence(out)
        out = x + out

        return out


class YoloBlock(nn.Module):
    def __init__(self, anchors):
        super(YoloBlock, self).__init__()
        self.anchors = anchors

class DarkNet53(nn.Module):
    def __init__(self):
        super(DarkNet53, self).__init__()
        inputChannels = 3

        netModules = []

        netModules.append(downsampleSequential(1, inputChannels, 32, 3, 1, 1, True))

        netModules.append(downsampleSequential(1, 32, 64, 3, 2, 1, True))

        netModules.append(ResidualConvolutionalBlock(64))

        netModules.append(downsampleSequential(1, 64, 128, 3, 2, 1, True))

        for i in range(2):
            netModules.append(ResidualConvolutionalBlock(128))

        netModules.append(downsampleSequential(1, 128, 256, 3, 2, 1, True))

        for i in range(8):
            netModules.append(ResidualConvolutionalBlock(256))

        netModules.append(downsampleSequential(1, 256, 512, 3, 2, 1, True))

        for i in range(8):
            netModules.append(ResidualConvolutionalBlock(512))

        netModules.append(downsampleSequential(1, 512, 1024, 3, 2, 1, True))

        for i in range(4):
            netModules.append(ResidualConvolutionalBlock(1024))


dn = DarkNet53()
