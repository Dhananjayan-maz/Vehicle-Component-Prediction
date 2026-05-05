# Nexus AI – Vehicle Component Detection (YOLOv8 + Django)
## Overview

Nexus AI is a web-based intelligent vehicle component detection system built using YOLOv8 and Django.
It allows users to upload images or capture live camera input to detect vehicle components such as ENGINE BAY, BRAKING SYSTEM, SUSPENSION SYSTEM, INTERIOR COMPONENTS and more.

<img width="1912" height="782" alt="ai vec 1" src="https://github.com/user-attachments/assets/d8844d80-f96c-4db2-904a-972237d3d882" />
<img width="1918" height="903" alt="ai vec 2" src="https://github.com/user-attachments/assets/e79f72fb-3a84-49d6-89e3-aa269c85a407" />

This project combines Computer Vision + Web Development to create an interactive AI-powered detection dashboard.

🎯 Key Features

📂 Image Upload Detection

📷 Live Camera Capture

🤖 YOLOv8 Object Detection Model

📊 Detection Results with Confidence Scores

🎨 Modern Glassmorphism UI (Responsive Design)

⚡ Real-Time Preview Before Detection

🔄 Drag & Drop Upload Support

🧠 AI Model  
Model: YOLOv8   
Framework: Ultralytics / Roboflow  
Task: Object Detection  
Output:  
* Component Name  
* Category  
* Confidence Score  
* Description  

🛠️ Tech Stack  
* Frontend  
* HTML5  
* CSS3 (Glassmorphism UI)  
* JavaScript (Camera + Preview Handling)

⚙️ Backend  
* Django (Python)  
* Django Templates  
* REST Handling (Form Submission)  

🤖 AI / ML
* YOLOv8  
* Roboflow (for dataset / inference)  
* OpenCV (optional if used)  

📸 Application Workflow
User uploads image or starts camera  
Preview is shown in UI  
User clicks "Run AI Detection"  
Image is sent to Django backend  
YOLOv8 processes the image  
Results are displayed with:
Bounding boxes  
Component details 
Confidence %  

## Installation & Setup

1️⃣ Clone Repository  
git clone https://github.com/your-username/nexus-ai-vehicle-detection.git  
cd nexus-ai-vehicle-detection  
2️⃣ Create Virtual Environment  
python -m venv venv  
source venv/bin/activate   # Linux / Mac  
venv\Scripts\activate      # Windows  
3️⃣ Install Dependencies  
pip install -r requirements.txt  
4️⃣ Run Django Server  
python manage.py runserver  
5️⃣ Open in Browser  
http://127.0.0.1:8000/

## Thank You...
