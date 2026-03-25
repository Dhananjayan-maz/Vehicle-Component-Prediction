# import os
# import cv2
# import base64
# import numpy as np
# from django.http import JsonResponse
# from django.shortcuts import render
# from .utils import get_prediction


# # 📦 CATEGORY MAPPING (same as yours)
# CATEGORY_MAP = {
#     "ENGINE BAY": [
#         "BATTERY", "AIR COMPRESSOR", "ALTERNATOR", "CAMSHAFT", "CRANKSHAFT",
#         "CYLINDER HEAD", "ENGINE BLOCK", "ENGINE VALVE", "FUEL INJECTOR",
#         "IGNITION COIL", "OIL FILTER", "OIL PAN", "RADIATOR", "RADIATOR FAN",
#         "RADIATOR HOSE", "SPARK PLUG", "THERMOSTAT", "WATER PUMP"
#     ],
#     "BRAKING SYSTEM": [
#         "BRAKE CALIPER", "BRAKE PAD", "BRAKE ROTOR"
#     ],
#     "SUSPENSION SYSTEM": [
#         "COIL SPRING", "LEAF SPRING", "LOWER CONTROL ARM"
#     ],
#     "TRANSMISSION SYSTEM": [
#         "CLUTCH PLATE", "PRESSURE PLATE", "TORQUE CONVERTER", "TRANSMISSION"
#     ],
#     "EXHAUST SYSTEM": [
#         "MUFFLER"
#     ],
#     "ELECTRICAL & SENSORS": [
#         "FUSE BOX", "OXYGEN SENSOR", "OIL PRESSURE SENSOR", "STARTER"
#     ],
#     "EXTERIOR BODY": [
#         "HEADLIGHTS", "TAILLIGHTS", "SIDE MIRROR", "SPOILER", "GAS CAP", "RIM"
#     ],
#     "INTERIOR COMPONENTS": [
#         "INSTRUMENT CLUSTER", "RADIO", "SHIFT KNOB", "WINDOW REGULATOR"
#     ]
# }


# # 📘 Component Info
# COMPONENT_INFO = {
#     "BATTERY": "Provides electrical power to start the vehicle",
#     "OIL PAN": "Stores engine oil",
#     "BRAKE PAD": "Creates friction to stop the vehicle",
#     "RADIATOR": "Helps cool the engine",
#     "SPARK PLUG": "Ignites fuel-air mixture in engine",
#     "MUFFLER": "Reduces exhaust noise",
#     "SIDE MIRROR": "Helps driver see rear sides",
#     "INSTRUMENT CLUSTER": "Displays speed, fuel level, etc."
# }


# def get_category(label):
#     for category, items in CATEGORY_MAP.items():
#         if label in items:
#             return category
#     return "UNKNOWN"


# def index(request):
#     return render(request, 'index.html')


# def predict(request):
#     if request.method == "POST" and request.FILES.get('image'):

#         image = request.FILES['image']

#         # 🔥 Fix filename (remove spaces)
#         filename = image.name.replace(" ", "_")

#         # Save image
#         upload_dir = os.path.join('detector', 'static', 'uploads')
#         os.makedirs(upload_dir, exist_ok=True)

#         image_path = os.path.join(upload_dir, filename)

#         with open(image_path, 'wb+') as f:
#             for chunk in image.chunks():
#                 f.write(chunk)

#         # Get prediction
#         result = get_prediction(image_path)

#         # 🔥 Load image safely
#         img = cv2.imread(image_path)
#         if img is None:
#             return render(request, 'index.html', {"error": "Image not loaded properly"})

#         # Draw bounding boxes
#         for pred in result.get("predictions", []):
#             x = int(pred["x"])
#             y = int(pred["y"])
#             w = int(pred["width"])
#             h = int(pred["height"])
#             label = pred["class"]
#             conf = round(pred["confidence"], 2)

#             x1 = int(x - w / 2)
#             y1 = int(y - h / 2)
#             x2 = int(x + w / 2)
#             y2 = int(y + h / 2)

#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

#             text = f"{label} ({conf})"
#             cv2.putText(img, text, (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         # 🔥 FIX: Ensure valid extension
#         name, ext = os.path.splitext(filename)

#         if ext.lower() not in [".jpg", ".jpeg", ".png"]:
#             ext = ".jpg"

#         output_filename = "output_" + name + ext
#         output_path = os.path.join(upload_dir, output_filename)

#         # Save image
#         cv2.imwrite(output_path, img)

#         # Prepare detections
#         detections = []
#         for pred in result.get("predictions", []):
#             label = pred.get("class")

#             detections.append({
#                 "class": label,
#                 "confidence": round(pred.get("confidence", 0), 3),
#                 "x": pred.get("x"),
#                 "y": pred.get("y"),
#                 "width": pred.get("width"),
#                 "height": pred.get("height"),
#                 "category": get_category(label),
#                 "description": COMPONENT_INFO.get(label, "No description available")
#             })

#         context = {
#             "image_url": "/static/uploads/" + output_filename,
#             "detections": detections
#         }

#         return render(request, 'result.html', context)

#     return render(request, 'index.html')

# def predict_camera(request):
#     if request.method == "POST":
#         import json
#         data = json.loads(request.body)

#         image_data = data['image'].split(',')[1]
#         image_bytes = base64.b64decode(image_data)

#         # Convert to OpenCV image
#         nparr = np.frombuffer(image_bytes, np.uint8)
#         img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#         # Save temporary image
#         temp_path = "temp.jpg"
#         cv2.imwrite(temp_path, img)

#         # Run prediction
#         result = get_prediction(temp_path)

#         detected = []
#         for pred in result.get("predictions", []):
#             detected.append(pred["class"])

#         return JsonResponse({"detected": detected})

import os
import cv2
import base64
from django.shortcuts import render
from .utils import get_prediction


# 📦 CATEGORY MAP
CATEGORY_MAP = {
    "ENGINE BAY": [
        "BATTERY", "AIR COMPRESSOR", "ALTERNATOR", "CAMSHAFT", "CRANKSHAFT",
        "CYLINDER HEAD", "ENGINE BLOCK", "ENGINE VALVE", "FUEL INJECTOR",
        "IGNITION COIL", "OIL FILTER", "OIL PAN", "RADIATOR", "RADIATOR FAN",
        "RADIATOR HOSE", "SPARK PLUG", "THERMOSTAT", "WATER PUMP"
    ],
    "BRAKING SYSTEM": ["BRAKE CALIPER", "BRAKE PAD", "BRAKE ROTOR"],
    "SUSPENSION SYSTEM": ["COIL SPRING", "LEAF SPRING", "LOWER CONTROL ARM"],
    "TRANSMISSION SYSTEM": ["CLUTCH PLATE", "PRESSURE PLATE", "TORQUE CONVERTER", "TRANSMISSION"],
    "EXHAUST SYSTEM": ["MUFFLER"],
    "ELECTRICAL & SENSORS": ["FUSE BOX", "OXYGEN SENSOR", "OIL PRESSURE SENSOR", "STARTER"],
    "EXTERIOR BODY": ["HEADLIGHTS", "TAILLIGHTS", "SIDE MIRROR", "SPOILER", "GAS CAP", "RIM"],
    "INTERIOR COMPONENTS": ["INSTRUMENT CLUSTER", "RADIO", "SHIFT KNOB", "WINDOW REGULATOR"]
}


COMPONENT_INFO = {
    "BATTERY": "Provides electrical power",
    "OIL PAN": "Stores engine oil",
    "BRAKE PAD": "Used for braking",
    "RADIATOR": "Cools engine",
    "SPARK PLUG": "Ignites fuel",
    "MUFFLER": "Reduces noise",
    "SIDE MIRROR": "Rear view",
    "INSTRUMENT CLUSTER": "Displays vehicle info"
}


def get_category(label):
    for category, items in CATEGORY_MAP.items():
        if label in items:
            return category
    return "UNKNOWN"


def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == "POST":

        upload_dir = os.path.join('detector', 'static', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)

        image = request.FILES.get('image')
        camera_image = request.POST.get('camera_image')

        # ==============================
        # 📂 HANDLE IMAGE INPUT
        # ==============================
        if image:
            filename = image.name.replace(" ", "_")

            # Ensure extension
            name, ext = os.path.splitext(filename)
            if ext.lower() not in [".jpg", ".jpeg", ".png"]:
                ext = ".jpg"
            filename = name + ext

            image_path = os.path.join(upload_dir, filename)

            with open(image_path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)

        elif camera_image:
            format, imgstr = camera_image.split(';base64,')
            filename = "camera_capture.jpg"
            image_path = os.path.join(upload_dir, filename)

            with open(image_path, "wb") as f:
                f.write(base64.b64decode(imgstr))

        else:
            return render(request, 'index.html', {"error": "No image provided"})

        # ==============================
        # 🔍 CALL ROBOFLOW API
        # ==============================
        try:
            result = get_prediction(image_path)
        except Exception as e:
            print("API ERROR:", e)
            return render(request, 'index.html', {
                "error": "API connection failed"
            })

        # ==============================
        # 🖼 LOAD IMAGE
        # ==============================
        img = cv2.imread(image_path)

        if img is None:
            return render(request, 'index.html', {"error": "Image load failed"})

        detections = []

        # ==============================
        # 📦 PROCESS PREDICTIONS
        # ==============================
        for pred in result.get("predictions", []):
            x = int(pred["x"])
            y = int(pred["y"])
            w = int(pred["width"])
            h = int(pred["height"])
            label = pred["class"]
            conf = round(pred["confidence"], 2)

            x1 = int(x - w / 2)
            y1 = int(y - h / 2)
            x2 = int(x + w / 2)
            y2 = int(y + h / 2)

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Label
            text = f"{label} ({conf})"
            cv2.putText(img, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            detections.append({
                "class": label,
                "confidence": conf,
                "category": get_category(label),
                "description": COMPONENT_INFO.get(label, "No description available")
            })

        # ==============================
        # 💾 SAVE OUTPUT IMAGE (FIXED)
        # ==============================
        name, ext = os.path.splitext(filename)
        if ext.lower() not in [".jpg", ".jpeg", ".png"]:
            ext = ".jpg"

        output_filename = "output_" + name + ext
        output_path = os.path.join(upload_dir, output_filename)

        success = cv2.imwrite(output_path, img)

        if not success:
            return render(request, 'index.html', {"error": "Failed to save output image"})

        # ==============================
        # 📤 SEND TO TEMPLATE
        # ==============================
        context = {
            "image_url": "/static/uploads/" + output_filename,
            "detections": detections
        }

        return render(request, 'result.html', context)

    return render(request, 'index.html')