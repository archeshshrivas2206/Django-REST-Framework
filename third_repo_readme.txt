🚀 Tribal S.E.T.U. - Smart Education & Tribal Upliftment
SIH'26 INTERNAL ROUND QUALIFIED AT PICT Out of 221 competing teams, we proudly emerged as one of the Top 45 teams to qualify!

Tribal S.E.T.U. is an AI-enabled Scholarship and Fellowship Management System explicitly designed for the Ministry of Tribal Affairs (MoTA) and Scheduled Tribe (ST) students. It serves as a unified digital ecosystem to streamline end-to-end administration of schemes like the National Fellowship for Scheduled Tribe (NFST) and National Overseas Scholarship (NOS)[cite: 1]. By prioritizing low-bandwidth accessibility, regional language support, and intelligent document scrutiny, Tribal S.E.T.U. overcomes the digital divide to ensure rapid, transparent financial disbursal[cite: 1].

🌟 Project Overview
Currently, ST students in remote areas face significant hurdles due to complex English forms, poor internet connectivity, and delayed manual processing[cite: 1]. Tribal S.E.T.U. shifts this paradigm from manual verification to "Intelligent Automated Scrutiny"[cite: 1]. It combines a bilingual, voice-assisted Progressive Web App (PWA) for applicants with an AI-ML Processing Hub for administrators, capable of auto-verifying documents, flagging forgeries, and automatically generating merit lists based on dynamic scheme criteria[cite: 1].

🎯 Key Features
🎓 For Applicants (ST Students)
🗣️ Bhashini Voice-Assisted Input: Enables students to fill out application fields (Name, Community, Institute) by speaking in Hindi, Marathi, or English[cite: 1]. The AI populates the corresponding English fields, completely bypassing technical and language barriers[cite: 1]. 📶 Offline-First PWA (Low Data Mode): An offline-capable portal that caches the app shell and honors browser "Save-Data" settings[cite: 1]. Students can complete forms and attach documents offline; the system silently auto-syncs when an internet connection is established[cite: 1]. 📱 WhatsApp Deficiency Resolution: Automatically notifies students via WhatsApp if documents (like blurred income certificates) are rejected, allowing them to upload corrections directly within the chat[cite: 1]. 🔍 Searchable Bilingual Directory: Features short eligibility summaries for official scheme listings across MahaDBT and the Ministry of Tribal Affairs[cite: 1].

👨‍💼 For Administrators (MoTA Desk Officers)
🧠 Smart Scrutiny & Forgery Detection: An AI engine utilizes OCR (Tesseract/EasyOCR) and OpenCV to extract text, match it against Identity APIs (like Aadhaar/DigiLocker), and assign a 0-100% Confidence Score[cite: 1]. High-confidence applications are auto-verified, while CV models flag manipulated pixels or forged stamps[cite: 1]. 📊 Split-Screen Triage Dashboard: Desk officers view applications sorted by AI confidence[cite: 1]. Flagged documents open in a split-screen view showing the original certificate next to AI-extracted fields for quick, one-click deficiency notification[cite: 1]. ⚙️ Zero-Code Dynamic Scheme Builder: A drag-and-drop rule engine allowing administrators to launch new scholarships, set parameters (e.g., income limits, required documents), and deploy them without writing any code[cite: 1]. 📈 Executive MoTA Dashboard: Features interactive maps, gender ratio quotas, PVTG inclusion tracking, and automated merit list calculation for direct PFMS disbursal[cite: 1].

💻 Tech Stack
🌐 Frontend Integration: React/Vite built as a Progressive Web App (PWA) with Tailwind CSS (compiled directly into the app bundle for low-data mode)[cite: 1]. ⚙️ Backend Framework: Python (FastAPI/Django) for AI-driven assessment endpoints and a Node.js API server to bridge Bhashini transcription services[cite: 1]. 🛡️ AI Validation Models: Tesseract OCR / EasyOCR for text extraction, paired with OpenCV for image manipulation analysis[cite: 1]. 🗄️ Database & Storage: PostgreSQL for relational applicant data and AWS S3 / Firebase Cloud Storage for secure document retention[cite: 1].

⚙️ Installation & Setup
1. 🖥️ Launch the Frontend (React/Vite)
To run the applicant and dashboard UI locally:

Open the project folder and install dependencies: npm ci
Start the development server: npm run dev
Open the Local URL printed by Vite (usually http://localhost:5173/).
(For a static live preview, run npm run build:live and open live-preview/index.html with VS Code Live Server).

2. 🎙️ Configure the Voice Server (Bhashini API)
For voice transcription, you must request credentials from Bhashini. Set these strictly on the server environment:

export BHASHINI_USER_ID='your-user-id'
export BHASHINI_API_KEY='your-api-key'
export BHASHINI_PIPELINE_ID='your-asr-pipeline-id'
npm run voice-server

### 2. 🎙️ Configure the Voice Server (Bhashini API)
For voice transcription, you must request credentials from Bhashini. Set these strictly on the server environment:
```bash
pip install -r requirements.txt
uvicorn main:app --reload

```text
##👥 Meet the Team

**This project was developed as a Skill Bridge initiative by the following team:**
**Pune Institute of Computer Technology SY STUDENTS**


__________________________________
| Ayman Kazi     | Team Leader   |
__________________________________
| Anushka Dhane  | Team Member   |
| Rudra Kharche  | Team Member   |
| Darshan Rajale | Team Member   |
| Aditya Pandya  | Team Member   |
| Aryan Jaiswal  | Team Member   |
__________________________________