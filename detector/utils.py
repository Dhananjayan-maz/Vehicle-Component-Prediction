# import requests

# API_KEY = "YOUR_API_KEY"
# MODEL_URL = "https://detect.roboflow.com/YOUR-MODEL/1"

# def get_prediction(image_path):
#     with open(image_path, "rb") as img:
#         response = requests.post(
#             MODEL_URL,
#             params={"api_key": API_KEY},
#             files={"file": img}
#         )
#     return response.json()

from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="a8WuubAjZJmqiWge2656"
)

def get_prediction(image_path):
    result = CLIENT.infer(image_path, model_id="car-parts-ybiev/1")
    return result