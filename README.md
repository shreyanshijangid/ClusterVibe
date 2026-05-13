# ✨ ClusterVibe: The AI Segmenter

An interactive machine learning web app that performs **K-Means clustering** on a dataset, letting users explore customer segmentation in real time through a sleek, dark-themed dashboard.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.x-orange?style=flat-square&logo=scikit-learn)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=flat-square&logo=plotly)

---

## 🚀 Demo

> Spin it up locally and use the sidebar to choose the number of clusters (K). Watch the scatter plot re-render instantly!

---

## 📌 Features

- 🎲 **Auto-generated dataset** — 300 data points with `Spending_Score` and `Hype_Level` attributes
- 🤖 **Live K-Means clustering** — runs on every slider change (K = 2 to 8)
- 📍 **Centroid overlay** — toggle cluster centers on/off via a checkbox
- 🌑 **Dark-themed Plotly chart** — color-coded clusters with pastel palette
- 📊 **Data breakdown panel** — tail preview table + cluster distribution bar chart

---

## 🛠️ Tech Stack

| Layer | Library |
|---|---|
| UI / App framework | [Streamlit](https://streamlit.io/) |
| ML / Clustering | [scikit-learn](https://scikit-learn.org/) — `KMeans` |
| Data manipulation | [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| Visualization | [Plotly Express](https://plotly.com/python/plotly-express/) |

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/clustervibe.git
cd clustervibe
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 📦 Requirements
