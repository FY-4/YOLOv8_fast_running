import os
import random

trainval_percent = 0.95
train_percent = 0.95
xmlfilepath = 'my_data_1/Annotations'#111111111111111111111111111111111
txtsavepath = 'my_data_1/ImageSets'#111111111111111111111111111111111
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('my_data_1/ImageSets/trainval.txt', 'w')#1111111111111111111111111111
ftest = open('my_data_1/ImageSets/test.txt', 'w')#111111111111111111111111111111111
ftrain = open('my_data_1/ImageSets/train.txt', 'w')#1111111111111111111111111111
fval = open('my_data_1/ImageSets/val.txt', 'w')#1111111111111111111111111111

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()