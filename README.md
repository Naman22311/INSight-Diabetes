                                                                                          INSight Diabetes
This repository contains the code for INSight Diabetes, a web application designed to predict the
potential risk of type 2 diabetes by analyzing SNPs in the input gene sequence.

Project Overview
Guide: Mr. Tavpritesh Sethi
Team Size: 7
Tech Stack: Python, Biopython, Flask, HTML, CSS
Data Sources: NCBI and ClinVar databases

Features
Web interface for inputting gene sequences
Downloads gene sequences from NCBI
Analyzes SNPs to predict type 2 diabetes risk
Utilizes symptoms selected by the user to enhance prediction accuracy

How to Run the Project
Prerequisites
Python 3.x
Flask
Biopython

Installation
Clone the repository: git clone https://github.com/your-username/insight-diabetes.git
cd insight-diabetes

Create a virtual environment: python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages: pip install -r requirements.txt

Project Structure
app.py: Main Flask application file.
templates/: Directory containing HTML templates.
static/: Directory containing static files (CSS, JS, etc.).
requirements.txt: List of required Python packages.

Usage
Home Page:


Enter the INS gene sequence in the provided text area.
Select the symptoms that apply to the user.
Results Page:


Displays whether the user is at risk of type 2 diabetes based on the input gene sequence and selected symptoms.
