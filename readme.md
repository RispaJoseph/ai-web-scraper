# AI Web Scraper

An interactive AI-assisted web scraper built with Python, Selenium, BeautifulSoup, and Streamlit.
This tool allows users to scrape any webpage, clean the content, and extract meaningful information — with optional AI-powered parsing for flexible queries.

---

## 🚀 Features

- Scrape any public webpage using Selenium
- Clean and preprocess HTML content
- Split large DOM content into manageable chunks
- AI-assisted parsing using local LLM (Ollama – optional)
- Ask custom extraction queries from scraped content
- Extract structured data like titles/headings without AI
- Interactive UI built with Streamlit

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** — UI
- **Selenium** — browser automation & scraping
- **BeautifulSoup** — HTML parsing & cleaning
- **LangChain** — prompt pipeline
- **Ollama**  — local LLM inference
- **Chrome WebDriver** — browser driver


## 📂 Project Structure
```
ai-web-scraper/
│
├── main.py          # Streamlit app UI
├── scrape.py        # Scraping + HTML cleaning logic
├── parse.py         # AI parsing logic (Ollama + LangChain)
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### Clone repo

```
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

#### Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Enable AI Parsing
```
curl -fsSL https://ollama.com/install.sh | sh
```

### Pull lightweight model

```
ollama pull tinyllama
```


### Run the App

```
streamlit run main.py
```

