# ⚡ SkillBridge — Full-Stack Freelance Service Marketplace

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11" />
  <img src="https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask 3.0" />
  <img src="https://img.shields.io/badge/PostgreSQL-Neon_DB-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Render-Hosted-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render" />
  <img src="https://img.shields.io/badge/Socket.IO-Realtime_Chat-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="Socket.IO" />
  <img src="https://img.shields.io/badge/OAuth-Google_2.0-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google OAuth" />
</p>

---

## 🌐 Live Demo & Deployment

🚀 **Production App URL:** [https://skillbridgefinal.onrender.com](https://skillbridgefinal.onrender.com)  
🗄️ **Database Infrastructure:** Neon Serverless PostgreSQL  
☁️ **Hosting Platform:** Render Web Services (Production Gunicorn WSGI)

---

## 📌 About SkillBridge

**SkillBridge** is a modern, enterprise-grade freelance marketplace platform connecting clients with skilled service providers. Built with a scalable Python Flask monolithic architecture, SkillBridge provides an end-to-end service lifecycle experience — from intelligent service discovery and real-time WebSocket messaging to cryptographic digitally-signed legal contracts and provider portfolio showcases.

---

## ✨ Key Platform Features

### 👤 Multi-Role Authentication & User Profiles
* **Role Management:** Full multi-role system supporting **Clients**, **Service Providers**, and **Administrators**.
* **Google OAuth 2.0 Integration:** 1-click seamless registration and login with Google.
* **Provider Auto-Upgrade:** Clients can seamlessly upgrade to Service Providers upon listing their first service.

### 🏪 Service Marketplace & Algorithmic Search
* **Category Exploration:** Filter services across Web Development, Graphic Design, Content Writing, Video Editing, Music & Audio, Photography, and Digital Marketing.
* **Smart Search Engine:** Built-in keyword auto-detection and category matching.
* **Priority Heap Recommendation:** Top featured services calculated dynamically using Min/Max Priority Heaps (`heapq`).

### 📝 Legal-Grade Digital Contracts
* **Cryptographic Signatures:** Digital agreements generating SHA-256 hashes upon client and provider sign-off.
* **Audit Compliance:** Timestamp and IP address tracking during signature verification.
* **Comprehensive Terms:** Built-in IP rights allocation, payment terms, and cancellation policies.

### 💬 Real-Time Communication & Notifications
* **Order Chat System:** Real-time WebSocket messaging via Flask-SocketIO tied directly to specific order IDs.
* **Notification Center:** Dynamic alerts for order status changes, contract events, and platform updates.

### 🤝 Communities & Portfolios
* **Skill Communities:** Join domain-specific groups (Web Devs, UI/UX Guild, Copywriters Alliance, etc.).
* **Provider Portfolios:** Showcases for freelancers to display completed projects, images, and external work links.

### 🛡️ Admin Management Dashboard
* **Content Moderation:** Comprehensive dashboard to oversee users, moderate services, manage categories, and handle site feedback.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3.11, Flask 3.0 (Application Factory & Blueprints) |
| **Database & ORM** | SQLAlchemy 2.0, Flask-SQLAlchemy, Neon Serverless PostgreSQL |
| **Production WSGI** | Gunicorn (Multi-threaded worker) |
| **Real-time Server** | Flask-SocketIO |
| **Authentication** | Flask-Login, Werkzeug Security, Authlib (Google OAuth 2.0) |
| **Frontend** | HTML5, Vanilla CSS3 (Custom Tokens & Dark/Light Themes), JavaScript (ES6+), Jinja2 |

---

## 🏗️ Architecture & CS Concepts

SkillBridge adheres strictly to core Object-Oriented Programming (OOP) and Software Architecture principles:

* **Application Factory Pattern:** `create_app()` modular initialization allowing dynamic environment switching (`Development`, `Production`, `Testing`).
* **MVC Pattern:** Strict separation of Database Models ([models.py](file:///d:/SkillBridge/SkillBridge%20V2.5/SkillBridge%20V2.5/models.py)), Controllers/Blueprints ([routes.py](file:///d:/SkillBridge/SkillBridge%20V2.5/SkillBridge%20V2.5/routes.py)), and Business Managers ([managers.py](file:///d:/SkillBridge/SkillBridge%20V2.5/SkillBridge%20V2.5/managers.py)).
* **Data Structures:**
  * **Heaps (`heapq`):** Top-N service selection in $O(N \log K)$ time.
  * **Trie / HashMap:** Fast string search and autocomplete query matching.
  * **Queues (`collections.deque`):** Order status transition pipelines.
* **Database Optimization:** Strategic index creation, foreign key constraints, connection pooling with `pool_pre_ping=True`, and automatic SSL reconnects.

---

## ⚡ Getting Started (Local Development)

### 1. Clone Repository
```bash
git clone https://github.com/Manin1311/SkillBridge.git
cd SkillBridge
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your credentials:
```env
SECRET_KEY=your-super-secret-key
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 4. Initialize & Seed Database
```bash
python init_db.py
```

### 5. Run Application
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## ☁️ Deployment Guide (Render)

1. Connect repository `Manin1311/SkillBridge` on **[Render Dashboard](https://dashboard.render.com)**.
2. Set Environment Variables:
   * `PYTHON_VERSION` = `3.11.8`
   * `FLASK_ENV` = `production`
   * `DATABASE_URL` = `<Neon-PostgreSQL-Connection-String>`
   * `SECRET_KEY` = `<Random-Secret-Key>`
   * `GOOGLE_CLIENT_ID` = `<Google-OAuth-Client-ID>`
   * `GOOGLE_CLIENT_SECRET` = `<Google-OAuth-Client-Secret>`
3. Set Build & Start Commands:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn -w 1 --threads 4 wsgi:app`

---

## 📄 License

This project is open source and available under the **MIT License**.
