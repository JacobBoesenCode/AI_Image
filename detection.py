from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()

detections = detector.detectObjectsFromImage(
	input_image=os.path.join(execution_path, "image.jpg"),
	output_image_path=os.path.join(execution_path, "outputimage.jpg"),
)

for eachObject in detections:
	print(
		eachObject["name"],
		" : ",
		eachObject["percentage_probability"],
	)
