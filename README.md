# 🚗 Nexus AI – Vehicle Component Detection System

An AI-powered vehicle component detection system developed using YOLOv8 and Django that enables users to upload vehicle images or use live camera input to identify and classify vehicle components in real time.

---

## 📌 Project Overview

Nexus AI is a computer vision-based web application designed to detect and classify vehicle components such as engine systems, braking systems, suspension systems, and interior components using deep learning object detection models.

The system combines Artificial Intelligence and Web Development to provide an interactive dashboard capable of performing real-time vehicle component analysis with confidence-based predictions.

---

## ✨ Key Features

### 🔹 AI-Powered Detection
- Vehicle component detection using YOLOv8
- Bounding box visualization
- Confidence score generation
- Component classification and labeling

### 🔹 Image & Camera Support
- Upload vehicle images for detection
- Live camera capture functionality
- Real-time image preview before inference
- Drag-and-drop image upload support

### 🔹 Detection Results
- Display detected component names
- Confidence percentage output
- Component category visualization
- Structured prediction results dashboard

### 🔹 UI & User Experience
- Modern Glassmorphism-based responsive UI
- Interactive dashboard layout
- Smooth animations and preview handling
- Responsive design for multiple devices

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Django
- Python

### AI / Computer Vision
- YOLOv8
- Roboflow
- OpenCV

### Development Tools
- VS Code
- GitHub

---

## ⚙️ System Workflow

```text
User Uploads Image / Uses Camera
                ↓
      Image Preview Generation
                ↓
      Send Image to Backend
                ↓
      YOLOv8 Model Inference
                ↓
     Detect Vehicle Components
                ↓
 Generate Bounding Boxes & Scores
                ↓
     Display Detection Results
```

---

## 🧠 Project Architecture

```text
                ┌─────────────────┐
                │ User Interface  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Django Backend  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ YOLOv8 Model    │
                │ Inference Engine│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Detection Output│
                │ Bounding Boxes  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Result Dashboard│
                └─────────────────┘
```

---

## 📸 Project Screenshots

### 🏠 Detection Dashboard
<img width="1912" height="782" alt="ai vec 1" src="https://github.com/user-attachments/assets/d8844d80-f96c-4db2-904a-972237d3d882" />

### 🤖 Vehicle Component Detection
<img width="1918" height="903" alt="ai vec 2" src="https://github.com/user-attachments/assets/e79f72fb-3a84-49d6-89e3-aa269c85a407" />

---

## 📂 Project Structure

```text
vehicle-component-detection/

├── manage.py
├── nexus_ai/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/                     # Main application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── detect.html
│   │   └── results.html
│   │
│   └── static/
│
├── media/                     # Uploaded images
├── yolov8_model/              # Trained model files
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dhananjayan-maz/Vehicle-Component-Prediction.git
cd Vehicle-Component-Prediction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Django Server

```bash
python manage.py runserver
```

### 5️⃣ Open in Browser

```text
http://127.0.0.1:8000/
```

---

## 🎯 Detection Categories

The system supports detection of vehicle components such as:

- Engine Bay
- Braking System
- Suspension System
- Interior Components
- Mechanical Parts

---

## 🔮 Future Enhancements

- Real-time video stream detection
- Multi-object tracking
- AI-based damage detection
- Model performance analytics
- Cloud deployment support
- Mobile-friendly optimization
