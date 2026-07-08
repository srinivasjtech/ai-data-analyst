<div align="center">

# 📊 AI Data Analyst

### Upload a CSV. Get instant charts, stats, and AI-powered insights — no code required.

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciLz4=&logoColor=white" />
<img src="https://img.shields.io/badge/Firebase-Firestore-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" />
<img src="https://img.shields.io/badge/Plotly-Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
<img src="https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge" />

</div>

---

## ✨ What is this?

**AI Data Analyst** is a single-file [Streamlit](https://streamlit.io) app that turns any CSV upload into:

- 📈 Instant summary stats and interactive charts
- 🤖 One-click AI-generated insights (trends, outliers, recommendations) via **Groq's Llama 3.3 70B**
- 💬 A free-form "ask anything about this data" chat box
- ☁️ Optional dataset metadata logging to **Firebase Firestore**

No notebooks, no boilerplate — just drag, drop, and explore.

---

## 🗂️ Table of Contents

- [Features](#-features)
- [Demo Flow](#-demo-flow)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Output Samples](#-output-samples)
- [License](#-license)

---

## 🚀 Features

| | Feature | Description |
|---|---|---|
| 📁 | **CSV Upload** | Drag-and-drop any `.csv` file |
| 🔢 | **Instant Metrics** | Row count, column count, and missing values at a glance |
| 👀 | **Data Preview** | Scrollable preview of the first 10 rows |
| 📊 | **6 Chart Types** | Histogram, Box Plot, Heatmap, Scatter, Bar, and Line charts |
| 🧠 | **AI Auto-Analysis** | One click summarizes patterns, anomalies, and business recommendations |
| ❓ | **Ask AI Anything** | Natural-language Q&A grounded in your actual data |
| ☁️ | **Firestore Logging** | Optional — automatically saves dataset metadata for tracking uploads over time |

---

## 🎬 Demo Flow

```mermaid
flowchart LR
    A[📁 Upload CSV] --> B[📊 Auto Summary + Metrics]
    B --> C{Pick Chart Type}
    C --> D[Histogram / Box / Heatmap / Scatter / Bar / Line]
    B --> E[🤖 Generate AI Insights]
    B --> F[💬 Ask Custom Question]
    E --> G[Groq LLM Response]
    F --> G
    B -.optional.-> H[☁️ Save Metadata to Firestore]
```

---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/ai-data-analyst.git
cd ai-data-analyst
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your secrets

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Then open `.streamlit/secrets.toml` and add your **Groq API key** (required) and **Firebase credentials** (optional — see [Configuration](#-configuration)).

### 5. Run the app

```bash
streamlit run app.py
```

Your browser will open at **`http://localhost:8501`** 🎉

> 💡 Want to try it immediately? Upload the included `assets/sample_employees.csv` — it's the same dataset used to generate the [output samples](#-output-samples) above.

---

## 🔧 Configuration

### Required — Groq API Key
Get a free key at [console.groq.com](https://console.groq.com), then add it to `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

### Optional — Firebase Firestore
Enable this to automatically log metadata (row/column counts, missing values, upload time) for every uploaded dataset.

**Option A — path to service account JSON:**
```toml
FIREBASE_SERVICE_ACCOUNT_PATH = "path/to/serviceAccountKey.json"
```

**Option B — inline credentials (great for Streamlit Cloud):**
```toml
[firebase]
type = "service_account"
project_id = "your-project-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "..."
# ...remaining service account fields
```

> 💡 If Firebase isn't configured, the app runs perfectly fine — it just skips metadata logging and shows an info banner.

> 🔒 **Never commit `secrets.toml`.** It's already excluded via `.gitignore`.

---

## 📁 Project Structure

```
ai-data-analyst/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── secrets.toml.example        # Template for API keys & Firebase config
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io)** — UI framework
- **[Pandas](https://pandas.pydata.org/) / [NumPy](https://numpy.org/)** — data wrangling
- **[Plotly Express](https://plotly.com/python/plotly-express/)** — interactive charts
- **[Groq](https://groq.com/)** (Llama 3.3 70B) — AI insights & Q&A
- **[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) / Firestore** — optional metadata storage

---

## 🗺️ Roadmap

- [ ] Support multi-file uploads and dataset comparisons
- [ ] Export AI insights as a PDF/Markdown report
- [ ] Add authentication for multi-user Firestore history
- [ ] Support Excel (`.xlsx`) uploads
- [ ] Chart export (PNG/SVG)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-idea`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push and open a Pull Request

---
## 🖨️Output Samples

1. When giving the input csv file.

![alt text](<Screenshot 2026-07-07 115222.png>)

2. Shows the necessary plots or graphs for the given input csv file.

![alt text](<Screenshot 2026-07-07 115621.png>)

3.AI output for the question given regarding the input csv file data.

![alt text](<Screenshot 2026-07-07 115700.png>)

---

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

Made with ❤️ and ☕ using Streamlit

</div>
