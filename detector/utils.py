# from inference_sdk import InferenceHTTPClient

# CLIENT = InferenceHTTPClient(
#     api_url="https://serverless.roboflow.com",
#     api_key="a8WuubAjZJmqiWge2656"
# )

# def get_prediction(image_path):
#     result = CLIENT.infer(image_path, model_id="car-parts-ybiev/1")
#     return result

from inference_sdk import InferenceHTTPClient
import cv2
import os

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="a8WuubAjZJmqiWge2656"   # ⚠️ Replace this (security)
)

def get_prediction(image_path):
    try:
        # 🔥 Step 1: Resize image (VERY IMPORTANT)
        img = cv2.imread(image_path)

        if img is None:
            return {"predictions": []}

        img = cv2.resize(img, (640, 640))  # 🔥 reduce size

        # Save resized temp image
        temp_path = "temp_resized.jpg"
        cv2.imwrite(temp_path, img)

        # 🔍 Step 2: Call API
        result = CLIENT.infer(temp_path, model_id="car-parts-ybiev/1")

        # 🔥 Step 3: Cleanup temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return result

    except Exception as e:
        print("Roboflow API Error:", e)
        return {"predictions": []}   # prevent crash