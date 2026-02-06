📊 AI Finance Agent — Stock Analysis & Dashboard

An AI-powered finance assistant that:

✅ Analyzes any stock
✅ Compares two companies
✅ Fetches real market data
✅ Generates price charts
✅ Plots returns & volume
✅ Saves markdown reports
✅ Runs in CLI & Streamlit dashboard

Powered by Agno Agents + Nebius LLM + Yahoo Finance.

🚀 Features

🔍 Stock fundamentals analysis

📈 1-year price history graphs

📊 Normalized performance comparison

📉 Daily returns charts

📦 Volume analysis

📄 Auto-saved reports in Markdown

🖥️ Command-line interface

🌐 Web dashboard (Streamlit)

🤖 Tool-calling AI agent

📂 Project Structure
finance_agent/
│
├── main.py        # CLI runner
├── app.py         # Streamlit dashboard
├── reports/       # Saved charts + reports
├── requirements.txt
├── .env.example
├── README.md
└── venv/

⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/YOUR_USERNAME/finance-agent.git
cd finance-agent

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install streamlit matplotlib yfinance python-dotenv

4️⃣ Setup environment variables

Create .env file:

NEBIUS_API_KEY=your_api_key_here


(Do NOT commit .env to GitHub.)

▶️ Run in Terminal (CLI Mode)
python main.py


Example:

Enter ONE or TWO stocks separated by comma: NVDA,AMD


Outputs:

Analysis table

Saved markdown report

Comparison graph

Returns & volume charts

Saved inside:

reports/

🌐 Run Web Dashboard
streamlit run app.py


Open in browser:

👉 http://localhost:8501

📊 Example Graphs Generated

Normalized performance comparison

Daily returns

Trading volume

All saved automatically.

🧠 Tech Stack

Python 3.10+

Agno Agents

Nebius LLM

Yahoo Finance API

Streamlit

Pandas

Matplotlib

🧪 Sample Prompts

CLI:

AAPL
TSLA,MSFT
NVDA vs AMD


Dashboard:

GOOG,META
RELIANCE.NS,TCS.NS

🛡️ Security

API keys stored in .env

.env added to .gitignore

Never commit secrets

📌 Future Roadmap

📉 Volatility & Sharpe ratio

🔥 Monte-Carlo simulation

📊 Correlation heatmap

💼 Portfolio optimization

☁️ Cloud deployment

⏰ Daily scheduler

📧 Email reports

⭐ Why This Project Matters

This project demonstrates:

✔ AI agents with tool-calling
✔ Real-time financial analysis
✔ Data visualization
✔ CLI + Web UI
✔ Clean architecture
✔ Production-ready patterns

Perfect for:

AI Engineer portfolio

Data science projects

Quant research demos

Full-stack ML apps

🧑‍💻 Author

Built by Sameer 🚀
