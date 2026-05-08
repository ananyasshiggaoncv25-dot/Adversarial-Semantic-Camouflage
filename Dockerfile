# Use Python 3.12 slim for smaller image size
FROM python:3.12-slim

# Install system libraries required by Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    librandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r ghost_persona/requirements.txt

# Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps chromium

EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "ghost_persona/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
