from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load mô hình
model = load_model('model.h5')

# Tên các lớp bệnh
class_names = [
    'Benign keratosis-like lesions',
    'Melanocytic nevi',
    'Dermatofibroma',
    'Melanoma',
    'Vascular lesions', 
    'Basal cell carcinoma',
    'Actinic keratoses'
]

# Mô tả ngắn gọn cho từng bệnh
disease_info = {
    'Benign keratosis-like lesions': 'Tổn thương lành tính thường do lão hóa da.',
    'Melanocytic nevi': 'Nốt ruồi, thường là lành tính nhưng cần theo dõi nếu thay đổi.',
    'Dermatofibroma': 'U xơ da lành tính thường xuất hiện ở chân.',
    'Melanoma': 'Ung thư da ác tính, cần được chẩn đoán và điều trị sớm.',
    'Vascular lesions': 'Tổn thương mạch máu như u máu hoặc giãn mạch.',
    'Basal cell carcinoma': 'Loại ung thư da phổ biến nhất, tiến triển chậm.',
    'Actinic keratoses': 'Tổn thương tiền ung thư do phơi nắng lâu dài.'
}

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(100, 75))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    predicted_index = np.argmax(prediction)
    predicted_label = class_names[predicted_index]
    confidence = float(prediction[predicted_index])

    # Danh sách (bệnh, xác suất) sắp xếp giảm dần
    all_probs = sorted(
        [(class_names[i], float(prediction[i])) for i in range(len(class_names))],
        key=lambda x: x[1], reverse=True
    )

    return predicted_label, confidence, all_probs

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No image part'
        file = request.files['image']
        if file.filename == '':
            return 'No selected file'

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        label, confidence, all_probs = predict_image(file_path)
        description = disease_info.get(label, "Không có thông tin mô tả.")

        return render_template(
            'predict.html',
            filename=filename,
            label=label,
            confidence=round(confidence * 100, 2),
            description=description,
            all_probs=[(name, round(prob * 100, 2)) for name, prob in all_probs]
        )

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
