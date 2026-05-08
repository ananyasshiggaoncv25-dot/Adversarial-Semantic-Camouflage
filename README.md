````markdown
# 👻 Ghost Persona: Adversarial Semantic Camouflage

> **Reclaim your digital privacy** through intelligent intent masking and search trail obfuscation.

![Production Ready](https://img.shields.io/badge/status-production%20ready-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.12%2B-blueviolet?style=flat-square)

---

## 🎯 Overview

**Ghost Persona** is a privacy-hardened system that generates adversarial search personas to obscure your real search intent from tracking algorithms, data brokers, and surveillance systems.

### Key Features

✅ **Intent Inversion Engine** - AI-powered contrast persona generation via Google Gemini  
✅ **Mimetic Automation** - Playwright-based browser automation with stealth detection bypass  
✅ **Real-time Dashboard** - Streamlit UI with entropy visualization  
✅ **Production Deployment** - Docker containerization + Railway/Render ready  
✅ **No Local Keys** - Environment-based secret management  
✅ **Zero Tracking** - Randomized scrolling, variable timing, stealth signatures  

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│          GHOST PERSONA SYSTEM (3-TIER)              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  🧠 AI LAYER (engine.py)                            │
│  ├─ Intent Inverter                                │
│  ├─ Gemini Model Integration                       │
│  └─ Contrast Persona Generation                    │
│       └─ persona_type, queries[], entropy_score    │
│                                                     │
│  🤖 AUTOMATION LAYER (automation.py)                │
│  ├─ Mimetic Controller                             │
│  ├─ Playwright Browser                             │
│  └─ Stealth Detection Bypass                       │
│       └─ Randomized Scrolling & Timing             │
│                                                     │
│  🎨 FRONTEND LAYER (app.py)                         │
│  ├─ Streamlit UI                                   │
│  ├─ Real-time Logs                                 │
│  └─ Entropy Visualization                          │
│       └─ Gauge Chart (Tracker Confusion %)         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Local Development

**1. Clone Repository**
```bash
git clone https://github.com/ananyasshiggaoncv25-dot/Adversarial-Semantic-Camouflage
cd Adversarial-Semantic-Camouflage
```

**2. Install Dependencies**
```bash
pip install -r ghost_persona/requirements.txt
```

**3. Set Environment Variable**
```bash
export GEMINI_API_KEY="your-google-gemini-api-key"
```

**4. Run Streamlit App**
```bash
streamlit run ghost_persona/app.py
```

**5. Access**
```
http://localhost:8501
```

---

## 🐳 Docker Deployment

### Build & Run Locally

```bash
# Build image
docker build -t ghost-persona .

# Run container
docker run -p 8501:8501 \
  -e GEMINI_API_KEY="your-key-here" \
  ghost-persona
```

### Deploy to Railway

```bash
# 1. Push to GitHub
git push origin main

# 2. Connect to Railway.app
# 3. Set GEMINI_API_KEY in Railway dashboard
# 4. Auto-deploys from Dockerfile ✅
```

### Deploy to Render

```bash
# 1. Push to GitHub
git push origin main

# 2. Connect to render.com
# 3. Set GEMINI_API_KEY in Render dashboard
# 4. Auto-deploys from Dockerfile ✅
```

---

## 📋 How It Works

### Workflow Example

```
User Input
  ↓
"I'm searching for Rolex Daytona watches"
  ↓
[IntentInverter.generate_ghost_persona()]
  ↓
Generated Contrast Persona:
  - persona_type: "Vintage Fashion Historian"
  - entropy_score: 0.92 (92% confusion)
  - queries: [
      "1950s fashion trends",
      "vintage timepiece history",
      "Swiss watchmaking heritage",
      ...
    ]
  ↓
[MimeticController.interaction_loop()]
  ↓
🛡️ Camouflaging with: 1950s fashion trends
🛡️ Camouflaging with: vintage timepiece history
...
  ↓
Search Trail Obfuscated ✅
```

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| **AI Engine** | Google Gemini 1.5 Flash |
| **Browser Automation** | Playwright + Stealth Plugin |
| **Frontend** | Streamlit |
| **Data Validation** | Pydantic |
| **Visualization** | Plotly |
| **Container** | Docker |
| **Language** | Python 3.12 |

---

## 📁 Project Structure

```
Adversarial-Semantic-Camouflage/
├── ghost_persona/
│   ├── requirements.txt      # Python dependencies
│   ├── engine.py             # AI Layer - Intent Inverter
│   ├── automation.py         # Automation Layer - Mimetic Controller
│   └── app.py                # Frontend Layer - Streamlit UI
├── Dockerfile                # Production container
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

---

## 🔐 Privacy & Security

✅ **No API keys in repository** - Environment variables only  
✅ **No local data persistence** - Ephemeral execution  
✅ **Stealth signatures** - Bypass detection systems  
✅ **Randomized behavior** - Prevent pattern matching  
✅ **HTTPS only** - Encrypted transit  

---

## ⚙️ Configuration

### Environment Variables

```bash
# Required
GEMINI_API_KEY=your-google-gemini-api-key

# Optional
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## 🐛 Troubleshooting

### "GEMINI_API_KEY not found"
```bash
export GEMINI_API_KEY="your-key-here"
streamlit run ghost_persona/app.py
```

### Playwright timeout
```bash
# Increase timeout in automation.py
page.goto(url, wait_until="domcontentloaded", timeout=60000)  # 60 seconds
```

### Docker build fails
```bash
docker build --no-cache -t ghost-persona .
```

### Streamlit won't start
```bash
pip install --upgrade streamlit
streamlit run ghost_persona/app.py --logger.level=debug
```

---

## 📊 Entropy Scoring

The system calculates **entropy_score** (0.0 - 1.0):

- **0.0 - 0.3** → Low obfuscation (weak masking)
- **0.3 - 0.7** → Medium obfuscation (reasonable privacy)
- **0.7 - 1.0** → High obfuscation (strong masking) ✅

The contrast persona is generated to maximize entropy difference from your real intent.

---

## 🚧 Future Enhancements

- [ ] Multi-engine support (DuckDuckGo, Bing, Ecosia)
- [ ] Browser fingerprint randomization
- [ ] VPN/Proxy rotation integration
- [ ] Search history export (anonymized)
- [ ] User preference presets
- [ ] A/B testing interface for persona effectiveness

---

## 📝 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

**ANANYA S SHIGGAON**  
RVCE, Bangalore  
[GitHub Profile](https://github.com/ananyasshiggaoncv25-dot)

---

## 🙏 Acknowledgments

- Google Gemini API for intent inversion
- Playwright for browser automation
- Streamlit for rapid UI development
- Open-source security community

---

## ⚠️ Disclaimer

This tool is for **educational and privacy research purposes**. Users are responsible for compliance with local laws and terms of service of websites accessed. The authors assume no liability for misuse.

---

**Built with ❤️ for digital privacy advocates.**
````
