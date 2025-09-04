💊 AI Medical Prescription Extraction

This is a Streamlit web application that extracts structured details from a complete medical prescription text.
It can automatically detect Patient Information, Doctor Information, Medicines, General Instructions, and Date of Prescription.

🚀 Features

📋 Extracts Patient Details (Name, Age, Gender, Contact).

👨‍⚕️ Extracts Doctor Details (Name, Specialization, Hospital/Clinic, Contact).

💊 Parses Medicines (Name, Dosage, Frequency, Duration, Special Instructions).

📌 Extracts General Instructions (Dietary advice, Rest/Lifestyle suggestions, Follow-up date).

📝 Detects Prescription Date.

✅ Displays results neatly in JSON format and a medicines table.

🛠️ Tech Stack

Python 3

Streamlit

Regex
 for text extraction

Pandas
 for medicine table formatting

📂 Project Structure
📦 prescription-extractor
 ┣ 📜 app.py          # Main Streamlit app
 ┣ 📜 README.md       # Project documentation
 ┗ 📜 requirements.txt # Python dependencies

⚙️ Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/your-username/prescription-extractor.git
cd prescription-extractor

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv


Activate it:

Windows (PowerShell)

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


(Or install manually)

pip install streamlit pandas

4️⃣ Run the Application
streamlit run app.py


The app will open in your browser at http://localhost:8501
 🚀

🧪 Example Prescription Input
Patient Name: Naveen
Age: 24
Gender: Male
Patient Contact: +91-9876543210

Doctor Name: Dr. Ramesh
Specialization: General Physician
Hospital: Apollo Clinic
Doctor Contact: +91-9123456789

Prescription Date: 25-08-2025

Paracetamol 500mg – 3 times/day – 5 days – After meals
Ibuprofen 200mg – 2 times/day – 3 days – Before meals

Diet: Avoid oily food
Rest: Take 7-8 hours sleep daily
Follow-up: After 1 week

📊 Sample Output

Patient Info → Name: Naveen, Age: 24, Gender: Male

Doctor Info → Dr. Ramesh, General Physician, Apollo Clinic

Medicines Table:

Medicine Name	Dosage	Frequency	Duration	Instructions
Paracetamol	500mg	3 times/day	5 days	After meals
Ibuprofen	200mg	2 times/day	3 days	Before meals

General Instructions → Avoid oily food, Take rest, Follow-up after 1 week.

Date → 25-08-2025

🔮 Future Improvements

Integrate OCR to read scanned prescriptions.

Use NLP models (Hugging Face / IBM Watson) for more accurate extraction.

Add drug interaction checker.

Export prescriptions in PDF/Excel format.

👨‍💻 Author

Developed by B19 CodeCure ✨
