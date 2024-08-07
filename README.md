# INSight Diabetes

Project Overview:    July 7, 2024

- Guide: Mr. Tavpritesh Sethi
- Tech Stack: Python, Biopython, Flask, HTML, CSS
- Project Duration: April 24 - May 24

INSight Diabetes is a web application designed to predict the potential risk of type 2 diabetes by analyzing Single Nucleotide Polymorphisms (SNPs) in the input gene sequence. The application collects and utilizes gene sequence data from NCBI and ClinVar databases.

Features

- Implemented a web interface to input and analyze gene sequences.
- Integrated SNP detection in gene sequences.
- Utilized NCBI and ClinVar databases to collect gene sequence data.
- Provided feedback based on detected SNPs and user-reported symptoms.

How to Run the Project

1. Clone the repository from GitHub:

        git clone https :// github .com/your − repo/INSight − Diabetes . git
   
2. Navigate to the project directory:

        cd INSight−Diabetes

3. Install the required dependencies:

       pip install − r requirements . txt

4. Set your email for Entrez:

        Entrez . email = "youremail@example.com"

6. Run the Flask application:

        python app.py
   
8. Open a web browser and navigate to:
   
        http ://127.0.0.1:5000/

Project Structure

- app.py : Main Flask application file.
- templates/ : Directory containing HTML templates.
- static/ : Directory containing static files (CSS, JS, etc.).
- requirements.txt : List of required Python packages.

Usage

Home Page:

1. Enter the INS gene sequence in the provided text area.
1. Select the symptoms that apply to the user.

Results Page:

Displays whether the user is at risk of type 2 diabetes based on the input gene sequence and selected symptoms.
