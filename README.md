# 🧠 Intellern – AI-Powered Learning Assistant

**Intellern** is an open-source, AI-powered learning assistant designed to help users actively learn through personalized document uploads, contextual chat, quiz generation, and multilingual tutoring. It combines modern technologies like LLMs, Retrieval-Augmented Generation (RAG), and speech interfaces to enhance daily learning.

---

## 📆 Monorepo Structure

```
intellern/
├── intellern-backend/      # FastAPI + LangChain/LlamaIndex + PostgreSQL + Auth0
└── intellern-frontend/     # Angular + Signals + Auth0 + TailwindCSS
```

---

## ✨ Features

### Learning Engine

* Upload and process documents (PDF, DOCX, TXT)
* Chunk, embed, and index documents using LangChain or LlamaIndex
* Contextual chat with OpenAI or local LLMs
* Track session history and generate daily summaries

### Assessment and Review

* Generate quizzes and tests based on content
* Track scores and learning progress

### Multilingual Tutor

* Language learning modules for English and German
* Speech-to-text (STT) and text-to-speech (TTS) for interaction
* Vocabulary builder and grammar practice

### Intelligent Augmentation

* Optional internet search to supplement document context
* Results integrated into learning flow

### Secure Auth

* Auth0 for authentication and role-based access
* User profiles, session history, and document ownership

---

## 🔧 Tech Stack

### Backend

* FastAPI, PostgreSQL, SQLAlchemy
* LangChain or LlamaIndex for RAG
* OpenAI, Whisper, ElevenLabs
* Auth0, PyJWT
* Docker, Alembic

### Frontend

* Angular v20, Signals, RxJS
* TailwindCSS
* Auth0 Angular SDK
* ngx-translate (i18n)

---

## ⚙️ Setup Instructions

### Prerequisites

* Docker + Docker Compose
* Node.js (v20+), npm
* Python 3.13+
* Auth0 tenant and OpenAI API key (optional)

### Quick Start

```bash
# Clone repo
git clone https://github.com/yourusername/intellern.git
cd intellern

# Start backend
cd intellern-backend
cp .env.example .env
docker-compose up --build

# Start frontend
cd ../intellern-frontend
npm install
ng serve
```

Backend: [http://localhost:8000](http://localhost:8000)
Frontend: [http://localhost:4200](http://localhost:4200)

---

## 🔹 Backend Structure (intellern-backend)

* `app/api/v1/`: Endpoints for auth, uploads, quizzes, learning, tutor
* `app/services/`: Business logic (RAG, quiz generation, STT/TTS)
* `app/utils/`: Helper functions (embedding, vector store, web search)
* `app/db/models/`: ORM models for User, Document, Session, Quiz
* `docker/`: Dockerfile and Compose config
* `scripts/`: Dev scripts (migrate, seed, start)

---

## 🔹 Frontend Structure (intellern-frontend)

* `features/`: Modular Angular feature folders (auth, uploads, learning, etc.)
* `core/`: Singleton services and global providers (API, auth, interceptors)
* `shared/`: Reusable UI components, pipes, directives
* `layouts/`: App layout components (public, dashboard)
* `assets/i18n/`: Translation files for English and German

---

## 🔐 Auth0 Setup

1. Create Auth0 app (SPA + API)
2. Configure environment files:

Backend `.env`:

```
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_API_AUDIENCE=https://intellern.api
```

Frontend `environment.ts`:

```ts
auth: {
  domain: 'your-tenant.auth0.com',
  clientId: 'your-client-id',
  audience: 'https://intellern.api'
}
```

---

## 🔮 Testing

Backend:

```bash
cd intellern-backend
pytest
```

Frontend:

```bash
cd intellern-frontend
ng test
```

---

## 🚜 Deployment Options

* Docker Compose (for dev or staging)
* Render / Railway / Fly.io
* Kubernetes (manifests coming soon)
* GitHub Actions for CI/CD

---

## 🙌 Contributing

We welcome contributions! To get started:

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes
4. Push and open a Pull Request

Please follow:

* Conventional commits
* Black + isort + flake8 for backend
* ESLint + Prettier for frontend

---

## 📖 License

MIT License © 2025 Theophilus Kofi Gordon

---

## 🌟 Vision

Intellern is built to support lifelong learners, educators, and developers by combining intelligent systems with structured knowledge delivery. From learning a new language to preparing for exams, Intellern is your personalized AI study partner.
