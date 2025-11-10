# CSV to Markdown Converter

A simple web application built with Streamlit that converts CSV files into structured Markdown format.

## Features

- 📤 Drag-and-drop CSV file upload
- 🔄 Convert CSV rows into key-value pair format
- 👁️ Live markdown preview
- ⬇️ Download converted markdown file
- 📝 View raw markdown output
- 🎨 Clean and modern UI

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

### Web Interface (Recommended)

**Easy way** - Use the run script:

```bash
./run_local.sh
```

**Manual way** - Run the commands:

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Command Line

You can still use the original command-line script:

```bash
python csv_to_markdown.py input_file.csv -o ./output/directory
```

## CSV Format

Your CSV should have a header row with column names:

```csv
Name,Email,Age,City
John Doe,john@example.com,30,New York
Jane Smith,jane@example.com,25,Los Angeles
```

This will be converted to:

```markdown
### filename

Name: John Doe
Email: john@example.com
Age: 30
City: New York

---

Name: Jane Smith
Email: jane@example.com
Age: 25
City: Los Angeles
```

## Deployment to Firebase/Google Cloud

### Quick Deploy

**Easy way** - Use the deploy script:

```bash
./deploy.sh
```

The script will guide you through the deployment process.

**Manual way** - Deploy directly:

```bash
gcloud run deploy csv-to-markdown \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

### Detailed Instructions

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment guide including:
- Google Cloud Run deployment
- Firebase Hosting integration
- Custom domain setup
- Environment variables
- Monitoring and logging
- Troubleshooting

## Project Structure

```
csv_to_markdown/
├── app.py                    # Streamlit web application
├── csv_to_markdown.py        # Original CLI script
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container configuration
├── example.csv              # Sample CSV file
├── run_local.sh             # Quick start script
├── deploy.sh                # Deployment script
├── README.md                # This file
├── DEPLOYMENT.md            # Detailed deployment guide
└── .streamlit/
    └── config.toml          # Streamlit configuration
```

## License

MIT

