ST Scholarship and Fellowship Management System
A web-based portal designed to help Scheduled Tribe (ST) students discover scholarships and fellowships, check eligibility, submit applications, upload required documents, and track application status in one place.

Overview
This project provides a user-friendly frontend for an AI-enabled scholarship and fellowship management system. It is intended to simplify the application journey for students by offering:

Scholarship and fellowship discovery
Eligibility guidance
Online application form
Document upload section
Application status tracking
Student registration and login flow
Features
Student home page with portal overview
Scholarships and fellowship listings
Eligibility information and requirements
Application form for scholarship/fellowship submission
Document upload panel for required certificates and proofs
Application status tracking workflow
Registration and login pages
Responsive design using HTML, CSS, and JavaScript
Project Structure
Text
ST-Scholarship-and-Fellowship-Management-System/
├── sih project/
│   ├── assets/
│   │   ├── banner1.svg
│   │   ├── banner2.svg
│   │   ├── banner3.svg
│   │   ├── fellowship.svg
│   │   ├── logo.svg
│   │   └── scholarship.svg
│   ├── pages/
│   │   ├── application.html
│   │   ├── dashboard.html
│   │   ├── documents.html
│   │   ├── eligibility.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── scholarships.html
│   │   └── status.html
│   ├── main.css
│   ├── main.html
│   ├── main.js
│   └── scholarship.svg
└── README.md
Tech Stack
HTML5
CSS3
JavaScript
Static frontend assets (SVG and page templates)
Getting Started
Prerequisites
A modern web browser
Python 3 (optional, for local static hosting)
Run locally
Clone the repository:
bash
git clone https://github.com/shailja-bajpaii/ST-Scholarship-and-Fellowship-Management-System.git
cd ST-Scholarship-and-Fellowship-Management-System
Start a local server:
bash
python3 -m http.server 8000
Open the portal in your browser:
Text
http://localhost:8000/sih%20project/pages/home.html
You can also open sih project/pages/home.html directly in a browser if you do not need a local server.

Main Pages
sih project/pages/home.html — landing page and overview
sih project/pages/scholarships.html — scholarship listings
sih project/pages/eligibility.html — eligibility screening
sih project/pages/application.html — student application form
sih project/pages/documents.html — document upload flow
sih project/pages/status.html — application status tracker
sih project/pages/login.html — student login page
sih project/pages/register.html — registration page
Notes
This repository currently contains a frontend prototype/static website. It does not include a backend, database, or live authentication system yet, but it is structured as a foundation for a full scholarship management platform.