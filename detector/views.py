import os
from django.shortcuts import render
from .utils import get_prediction

# 📘 Training Info (optional – you can expand later)
component_info = {
    "BATTERY": "Stores electrical energy",
    "RADIATOR": "Cools the engine",
    "ENGINE BLOCK": "Main structure of engine",
    "BRAKE PAD": "Used for braking",
    "SPARK PLUG": "Ignites fuel in engine"
}

def index(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == "POST" and request.FILES.get('image'):

        image = request.FILES['image']
        mode = request.POST.get('mode')

        # ✅ Save image
        upload_dir = os.path.join('detector', 'static', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)

        image_path = os.path.join(upload_dir, image.name)

        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # 🔥 Get prediction from Roboflow
        result = get_prediction(image_path)

        detections = []
        detected_labels = set()

        # ✅ Extract FULL details
        for pred in result.get("predictions", []):
            label = pred.get("class")

            detection_data = {
                "class": label,
                "confidence": round(pred.get("confidence", 0), 3),
                "x": pred.get("x"),
                "y": pred.get("y"),
                "width": pred.get("width"),
                "height": pred.get("height"),
            }

            detections.append(detection_data)
            detected_labels.add(label)

        detected_labels = list(detected_labels)

        # 🏭 INDUSTRY MODE (example logic)
        missing_parts = []
        if mode == "industry":
            required = ["BATTERY", "RADIATOR", "ENGINE BLOCK"]
            missing_parts = [p for p in required if p not in detected_labels]

        # 🏫 TRAINING MODE
        info = {}
        if mode == "training":
            for part in detected_labels:
                info[part] = component_info.get(part, "No info available")

        context = {
            "image_url": "/static/uploads/" + image.name,
            "detections": detections,   # 🔥 full details
            "detected_labels": detected_labels,
            "missing": missing_parts,
            "info": info,
            "mode": mode
        }

        return render(request, 'result.html', context)

    return render(request, 'index.html')