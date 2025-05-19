# 🧬 INSight Diabetes

**INSight Diabetes** is a **Flask-based web application** designed to predict the potential risk of **type 2 diabetes** by analyzing **Single Nucleotide Polymorphisms (SNPs)** in user-provided gene sequences. Leveraging data from **NCBI** and **ClinVar** databases, it offers a user-friendly interface for gene sequence analysis and risk assessment.

📅 **Project Overview**  
- **Guide**: Mr. Tavpritesh Sethi  
- **Duration**: April 24, 2024 - May 24, 2024  
- **Last Updated**: July 7, 2024  

---

## 🚀 Features

- **Gene Sequence Input** 🧪: User-friendly interface to input and analyze INS gene sequences.  
- **SNP Detection** 🔍: Identifies Single Nucleotide Polymorphisms in gene sequences.  
- **Database Integration** 🌐: Fetches gene sequence data from NCBI and ClinVar.  
- **Risk Assessment** 📊: Provides feedback on type 2 diabetes risk based on SNPs and user-reported symptoms.  

---

## 🧠 Tech Stack

| **Layer**            | **Technology**           |  
|-----------------------|--------------------------|  
| **Backend**           | Flask, Python, Biopython |  
| **Frontend**          | HTML, CSS                |  
| **Database**          | NCBI, ClinVar (external) |  

---

## 📁 Project Structure

```
INSight-Diabetes
├── templates/                 # HTML templates for frontend
│   ├── index.html            # Home page for gene sequence input
│   ├── results.html          # Results page for risk assessment
├── static/                   # Static assets
│   ├── css/                  # CSS styles
│   ├── js/                   # JavaScript files
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ✅ Prerequisites

Ensure the following are installed on your system:  
- 🐍 Python 3.8+  
- 📦 Flask  
- 🧬 Biopython  
- 📜 Other dependencies listed in `requirements.txt`  

---

## 📦 Installation & Running Locally

Follow these steps to set up and run the project on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Naman22311/INSight-Diabetes
cd INSight-Diabetes
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Entrez Email
Set your email for NCBI's Entrez API in `app.py`:  
```python
Entrez.email = "youremail@example.com"
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Application
Open a web browser and navigate to:  
🌐 `http://127.0.0.1:5000/`

---

## 🖥 Usage

### Home Page
1. **Input Gene Sequence** 🧬: Enter the INS gene sequence in the provided text area.  
2. **Select Symptoms** ✅: Choose applicable symptoms from the provided options.  

### Results Page
- **Risk Assessment** 📈: Displays the risk of type 2 diabetes based on detected SNPs and selected symptoms.  

---
