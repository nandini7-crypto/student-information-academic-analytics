# Student Information Management & Academic Analytics System

## 📌 Project Overview

The **Student Information Management & Academic Analytics System** is a web-based academic data management and analytics project developed using Python, Pandas, SQL, SQLite, and Django.

The project combines **data analysis, database management, and a Django web interface** to manage student academic records and generate useful performance insights.

The system analyzes student attendance and subject scores to identify performance patterns, compare subject averages, and examine the relationship between attendance and final marks.

This project was developed as a portfolio project to demonstrate practical skills in **Information Management, Data Analysis, Database Management, Data Visualization, and Web Application Development**.

---

## 🎯 Objectives

* Manage student academic records
* Analyze student academic performance
* Calculate average scores for different subjects
* Identify highest and lowest performing students
* Analyze overall attendance
* Study the relationship between attendance and final marks
* Visualize academic performance using charts
* Provide a searchable student records interface
* Display individual student performance details
* Practice data handling and analysis using Python and Pandas
* Practice database management using SQLite and SQL
* Develop a web-based academic analytics dashboard using Django

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Matplotlib**
* **Django**
* **SQLite**
* **SQL**
* **HTML & CSS**
* **JavaScript**
* **CSV**
* **Git & GitHub**

---

## 📂 Project Structure

```text
Student_Analytics_Project/
│
├── data/
│   └── students.csv
│
├── dashboard/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── dashboard.html
│   │       └── student_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── analysis.py
├── create_database.py
├── queries.py
├── import_students.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Data Analysis

The project performs the following analyses:

* Dataset overview and structure
* Missing value analysis
* Average scores for Python, SQL, and Machine Learning
* Highest and lowest performing students
* Average student attendance
* Attendance vs Final Mark correlation
* Subject performance comparison
* Identification of top-performing students
* Data visualization using charts

### Key Findings

* **Machine Learning** had the highest average score among the three subjects.
* **SQL** had the lowest average score among the three subjects.
* The average attendance was **82.8%**.
* **Emily** had the highest final mark of **95**.
* **Daniel** had the lowest final mark of **59**.
* The sample showed a strong positive correlation between attendance and final marks.

> **Note:** The dataset contains fictional student records created for educational and portfolio purposes. The findings are based on a small sample and should not be considered general conclusions about student performance.

---

## 🗄️ SQL Database and Analytics

The project uses **SQLite** to store and analyze student records.

SQL queries were implemented to:

* Retrieve student records
* Filter students based on final marks
* Find top-performing students
* Calculate average subject scores
* Calculate average attendance
* Find highest and lowest final marks
* Count students meeting performance criteria
* Analyze students by department
* Identify students with high attendance and performance

The SQL implementation is available in `queries.py`, while `create_database.py` creates the SQLite database from the CSV dataset.

---

## 🌐 Django Web Application

The project was extended into a Django-based web application that provides an interactive interface for viewing and analyzing student information.

### Dashboard Features

* Student performance summary
* Total student count
* Average final mark
* Average attendance
* Highest final mark
* Top-performing student
* Average subject scores
* Subject performance chart
* Attendance vs Final Mark scatter plot
* Attendance-performance correlation
* Student records table
* Student search functionality
* Individual student detail pages
* Performance status classification

### Performance Status

Students are categorized based on their final marks:

* **Excellent** — 90 and above
* **Good** — 75–89
* **Needs Improvement** — below 75

The Django application also includes an **admin interface** for managing student records.

---

## 📈 Analytics Dashboard

The dashboard provides visual representations of academic data, including:

* Subject average comparison
* Attendance vs final mark relationship
* Student performance records
* Individual student academic profiles

The dashboard is designed to provide a simple interface for understanding student performance data without directly working with the underlying database.

---

## 🔐 Data & Database

The project uses SQLite for the Django application's local database.

The generated database file is excluded from version control using `.gitignore` to avoid uploading local database data to GitHub.

The original student dataset is stored as a CSV file and is used as the source for analysis and database population.

---

## 🚀 Future Improvements

Possible future enhancements include:

* Student authentication and role-based access
* Student and staff management modules
* PostgreSQL database integration
* More advanced academic reports
* Additional interactive visualizations
* Exporting reports to CSV or PDF
* Predictive analysis for student performance
* Deployment of the Django application online
* Improved responsive design for mobile devices

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/nandini7-crypto/student-information-academic-analytics.git
```

### 2. Navigate to the project directory

```bash
cd student-information-academic-analytics
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run Django migrations

```bash
python manage.py migrate
```

### 5. Import the student dataset

```bash
python import_students.py
```

> Run `import_students.py` only once to avoid creating duplicate student records.

### 6. Start the Django development server

```bash
python manage.py runserver
```

### 7. Open the application

Visit:

```text
http://127.0.0.1:8000/
```

---

## 👩‍💻 Author

**Nandini Asok**

BCA Graduate | Python, SQL, Data Analysis & Web Development

This project was developed as part of a personal portfolio to demonstrate practical experience in Python, SQL, data analysis, database management, and Django web development.
