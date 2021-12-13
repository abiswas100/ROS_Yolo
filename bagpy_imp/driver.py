import bagtoimage_copy as bi
from Yolo_imp import Yolo_new as Yolo

# img_data = []

img_data = bi.bag_to_image()

Yolo.Yolo_imp(img_data)


