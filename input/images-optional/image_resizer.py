import cv2

input_file = "0.jpg"
output_file = "0.jpg"

def resize_image(image_path, output_path):
    img = cv2.imread(image_path)
    if img is not None:
        img_resized = cv2.resize(img, (416, 416))
        cv2.imwrite(output_path, img_resized)
        print(f"Resized and saved: {output_path}")

print("okay")
resize_image(input_file, output_file)

