import os
import PIL as pillow
import rospy
try:
    import cv2
except ImportError:
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    import cv2
    sys.path.append(ros_path)
from os import chdir
import numpy as np
import time
def Yolo_imp(img_data): 
    start_time = time.perf_counter ()
    # print("In Yolo - ",os.getcwd())
    os.chdir(r"/home/avhi/Desktop/ROS_Yolo/Yolo_imp")
    # print("In Yolo - ",os.getcwd())
    
    net = cv2.dnn.readNet('yolov3.cfg','yolov3.weights')
    classes = []

    with open('coco.names', 'r') as f:
        
        classes = f.read().splitlines()

    # img_name = name1 = input("Enter name of the image file: ")
    # img  = cv2.imread('img_name')
    height,width,_ = img_data.shape

    blob = cv2.dnn.blobFromImage(img_data, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)


    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()

    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
    # print(len(boxes))
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # print(indexes.flatten())

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    if len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            print(label, confidence)
            color = colors[i]
            cv2.rectangle(img_data,(x,y), (x+w, y+h), color, 2)
            cv2.putText(img_data, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
        print("------------------------")


    # path = os.getcwd()

    # folder_path = path+'/Yolo_Output_left'
    
    # if os.path.isdir(folder_path) is True:
    #     # print("in if") 
    #     os.chdir(r"Yolo_Output_left")

    # else:
    #     # print("in else")
    #     os.mkdir("Yolo_Output_left")
    #     os.chdir(r"Yolo_Output_left")
            
    # timestamp = str(rospy.Time.now())
    # # image_name = "Yolo_output_left"  + timestamp + ".jpg"

    # image_name =  timestamp + ".jpg"
    # print(image_name)
    # # cv2.imwrite(image_name, img_data)
     
    # # print("Ending YOlo",os.getcwd())
    # cv2.imwrite("waka.jpg", img_data)
    end_time = time.perf_counter ()
    print(end_time - start_time, "seconds")
    print("------------------------")
    return img_data






# cv2.imshow('Image',img_data)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()