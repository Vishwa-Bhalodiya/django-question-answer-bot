# Question Answer Bot

A **Question Answering Bot** project that lets users interact with an intelligent QA system using a REST API and web interface. This bot processes user questions and returns answers - either from predefined logic or AI models - powered by Django.

## Features

- Django backend with modular apps (`api`, `qa_bot`)
- Exposes REST API endpoints for asking questions
- Could be integrated with AI or custom logic for answering
- Easy to run locally or deploy
- Clear project structure

## Project Structure

```bash
django-question-answer-bot/
├── api/ # API app (views, serializers, routes)
├── qa_bot/ # Core bot logic (models, services, utils)
├── manage.py # Django project runner
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation
```

## Getting Started

Follow these steps to run this project locally:

### 1) Clone the Repository

```bash
git clone https://github.com/Vishwa-Bhalodiya/django-question-answer-bot.git
cd django-question-answer-bot
```

### 2) Create & Activate a Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

## 4) Environment Variables

If your bot integrates with external AI or services, add a .env file with keys like:

```bash
AZURE_OPENAI_API_KEY=your_openai_key_here
AZURE_OPENAI_API_ENDPOINT=your_endpoint_here
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

### 5) Start the Development Server

```bash
python manage.py runserver
```

Now open your browser and visit: http://127.0.0.1:8000/

## Usage

## API Endpoints

Add actual endpoints once you define them in api/urls.py, for example:

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/upload/ | POST | To upload the documents. |
| /api/ask/ | POST | To send a question and receive an answer. |

#### Request example (JSON):
```bash
{
  "question": "What is the main topic of this document?"
}
```

#### Response example:
```bash
{
  "answer": "The main topic of this document is xyz."
}
```






