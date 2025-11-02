# 😊 Emotion Detector

A simple and elegant web app that detects facial emotions from uploaded images using a **pre-trained deep learning model** from Hugging Face.  
Built with **Streamlit** and **Python**, it lets users upload an image, get instant predictions, and view emotion confidence in real time.

---

## 🚀 Features

- 📸 Upload any image (JPG, JPEG, PNG) directly from your device  
- 🤖 Detects facial emotions using a pre-trained transformer model  
- 📊 Displays prediction confidence as a percentage and progress bar  
- ⚡ Fast, lightweight, and easy to run locally  
- 🎨 Clean white-themed interface for a modern, readable look  

---

## 🧠 Tech Stack

| Tool / Library | Purpose |
|----------------|----------|
| **Python 3** | Core programming language |
| **Streamlit** | Frontend web framework |
| **Transformers (Hugging Face)** | For loading the emotion detection model |
| **Torch** | Deep learning backend |
| **Pillow (PIL)** | Image loading and processing |

---

## 🗂️ Project Structure

📁 image_emotion_detector/
│
├── app.py # Streamlit app (UI + main logic)
├── model.py # Pre-trained model loading and prediction
├── requirements.txt # List of dependencies
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/image_emotion_detector.git
cd image_emotion_detector
```

2. (Optional) Create a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

4. Install dependencies
bash
Copy code
pip install -r requirements.txt

6. Run the app
bash
Copy code
streamlit run app.py
Then open your browser and visit:

arduino
Copy code
http://localhost:8501
🧩 Example Usage
Choose an image from your computer.

The app processes it and detects an emotion (e.g. happy, sad, angry).

See the predicted emotion and confidence percentage displayed instantly.

🛠️ Future Improvements
Add database support for storing predictions

Include multiple face detection in one image

Add history or download feature

Deploy the app online (Render, Vercel, etc.)

👨‍💻 Author
Ulonnam Ugochukwu Martins
📧 ogochukwuulonnam986@gmail.com

🌐 Live Demo (Optional)
You can deploy this project on Render, Streamlit Cloud, or Vercel.
Example:
https://marcomynous-emotion-detector-app-ccg4bf.streamlit.app/

