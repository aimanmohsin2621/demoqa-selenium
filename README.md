# 🧪 DemoQA Selenium Automation Project

This is a professional Selenium automation testing project built for practice and demonstration purposes.  
It automates UI testing on the **[DemoQA website](https://demoqa.com)** using **Python + Selenium + Pytest**.

---

## 🚀 Project Overview

This framework follows a **Page Object Model (POM)** structure —  
meaning, all page-related actions and elements are stored in separate files for better organization and scalability.

### 📁 Folder Structure

demoqa-selenium/
├─ artifacts/ # Screenshots and visual test results
├─ tests/
│ ├─ conftest.py # Global test setup (browser fixture)
│ ├─ requirements.txt # Required Python packages
│ ├─ pages/ # Page classes (page objects)
│ │ └─ practice_form_page.py
│ ├─ utils/ # Helper tools
│ │ └─ visual_diff.py
│ └─ tests/ # Test cases
│ ├─ test_open_demoqa.py
│ ├─ test_practice_form.py
│ ├─ test_bookstore_e2e.py
│ └─ test_visual_regression.py
└─ README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

Run this command inside your main folder:

```bash
pip install -r tests/requirements.txt

Make sure you update your ChromeDriver path inside your test files if needed:
service = Service(r"C:\Users\<your-name>\Downloads\chromedriver-win64\chromedriver.exe")

Run the Tests
To execute all tests:

pytest -v


Or to run a specific test file:

pytest tests/tests/test_practice_form.py -v

🧠 Tests Included
Test File	Description
test_open_demoqa.py	Verifies DemoQA website opens correctly
test_practice_form.py	Tests filling and submitting the practice form
test_bookstore_e2e.py	Performs an API + UI test on BookStore module
test_visual_regression.py	Compares screenshots for visual differences
🖼️ Visual Regression Testing

When test_visual_regression.py runs:

1.Takes a screenshot (current_home.png)

2.Compares with a base image (base_home.png)

3.Reports if any visual changes are found.

👩‍💻 Author

Aiman Mohsin
Python Selenium Automation | Student Project Submission