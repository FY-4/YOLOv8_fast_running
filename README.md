# YOLOv8_fast_running
## A simple introduction about YOLOv8_fast_running
This project is mainly about getting started with yolov8 code quickly,  <br>
which can help you run yolov8 quickly and implement yolo with only a few steps. <br>
However, for the logic and details of the source code, please check the official code for yourself.
![架构图](images/roboflow_whats_new_in_yolov8.jpg)

## Details
you can git my code in FY-4/YOLOv8_fast_running<br>
I will tell the steps and use gpu to promote the process by the plateform named Autodl

## Structure
>YOLOv8_Finally

>>my_data
>>>images<br>
>>>Annotations<br>
>>>ImageSets<br>
>>>labels<br>

>>1.yaml<br>
>>train.py<br>
>>voc_label.py<br>
>>split_train_val.py<br>

>README.md<br>

## Steps

#### As you open the YOLOv8_fast_running<br>
```Bash
cd YOLOv8_fast_running
```
#### YOLOv8_fast_running/my_data is your datasets
when you finish your dataset<br>
```Bash
python split_train_val.py
python voc_label.py
```
![you will get files after you run the code](images/jiago.jpg)
#### As you finish to reset your 1.yaml file
```Bash
python train.py
```
#### Then if you step into process of trainning model , you can take a relax and wait for a moment which dependent on your trainning times.

## Pay attention some details
>my_data
>>images<br>
>>Annotations<br>
>>ImageSets<br>
>>labels<br>

this is the structure of your datasets<br>*images* contains all of your original photos<br>
<br>
the Annotations contain all the .xml files which is dealt by labellmg<br>so we can put the xml file in this directory<br>
<br>
ImageSets and labels do not request you to do something <br>
just run<br>

```Bash
python split_train_val.py
python voc_label.py
```


