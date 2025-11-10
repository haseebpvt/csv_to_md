# Quick Start Guide

## 🚀 Running Locally (5 seconds)

```bash
./run_local.sh
```

Then open: **http://localhost:8501**

## ☁️ Deploy to Cloud (2 minutes)

```bash
./deploy.sh
```

Follow the prompts, and you'll get a live URL like:
`https://csv-to-markdown-xxxxx.run.app`

## 📝 How to Use the App

1. **Upload CSV**: Drag and drop or click to browse
2. **Convert**: Click the "Convert to Markdown" button
3. **Preview**: See the rendered markdown
4. **Download**: Click download to save the `.md` file

## 🎯 Common Tasks

### Test the App Locally
```bash
# Use the example file provided
# 1. Start the app: ./run_local.sh
# 2. Upload example.csv
# 3. See the result!
```

### Update Your Deployed App
```bash
# Make your changes, then:
./deploy.sh
# Use the same service name as before
```

### Stop Local Server
```bash
# Press Ctrl+C in the terminal where Streamlit is running
```

### View Deployment Logs
```bash
gcloud run logs read csv-to-markdown --limit 50
```

### Delete Deployed App
```bash
gcloud run services delete csv-to-markdown --region us-central1
```

## 🐛 Troubleshooting

**App won't start locally?**
```bash
# Make sure you have Python 3.11+ installed
python3 --version

# Recreate virtual environment
rm -rf venv
./run_local.sh
```

**Port already in use?**
```bash
# Find what's using port 8501
lsof -i :8501

# Kill the process or use a different port
streamlit run app.py --server.port=8502
```

**Deployment fails?**
```bash
# Make sure you're logged in
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

## 📚 More Information

- Full documentation: See [README.md](README.md)
- Deployment guide: See [DEPLOYMENT.md](DEPLOYMENT.md)
- Original CLI script: `python csv_to_markdown.py --help`

## 💡 Tips

- The app works offline once deployed (no external dependencies)
- Free tier includes 2M requests/month on Cloud Run
- The app automatically scales from 0 to handle traffic
- CSV files are processed in memory (not stored)

## 🔗 URLs

- **Local**: http://localhost:8501
- **After deployment**: Check terminal output for your live URL
- **Cloud Console**: https://console.cloud.google.com/run

---

Need help? Check the full README.md or DEPLOYMENT.md files!

