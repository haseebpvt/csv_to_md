# Deployment Guide

## Deploy to Google Cloud Run (Firebase Infrastructure)

Google Cloud Run is the recommended way to deploy Streamlit apps on Firebase infrastructure.

### Prerequisites

1. Install Google Cloud SDK:
```bash
# macOS
brew install google-cloud-sdk

# Or download from: https://cloud.google.com/sdk/docs/install
```

2. Login to Google Cloud:
```bash
gcloud auth login
```

3. Set your project (or create one at https://console.cloud.google.com):
```bash
gcloud config set project YOUR_PROJECT_ID
```

### Method 1: Deploy with Cloud Build

1. Make sure Docker is installed and running

2. Deploy directly from source:
```bash
gcloud run deploy csv-to-markdown \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1
```

This will:
- Build the Docker image from your Dockerfile
- Deploy it to Cloud Run
- Give you a public URL (e.g., `https://csv-to-markdown-xxxxx-uc.a.run.app`)

### Method 2: Deploy using pre-built Docker image

1. Build the Docker image:
```bash
docker build -t gcr.io/YOUR_PROJECT_ID/csv-to-markdown .
```

2. Push to Google Container Registry:
```bash
docker push gcr.io/YOUR_PROJECT_ID/csv-to-markdown
```

3. Deploy to Cloud Run:
```bash
gcloud run deploy csv-to-markdown \
  --image gcr.io/YOUR_PROJECT_ID/csv-to-markdown \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated
```

### Connect to Firebase Hosting (Optional)

If you want to use your Firebase domain:

1. Initialize Firebase in your project:
```bash
firebase init hosting
```

2. When prompted, select "Set up an existing Cloud Run service"

3. Follow the prompts to connect your Cloud Run service

4. Deploy:
```bash
firebase deploy --only hosting
```

Now your app will be accessible at `https://your-project.web.app`

## Environment Variables (if needed)

If you need to add environment variables:

```bash
gcloud run deploy csv-to-markdown \
  --set-env-vars "KEY1=VALUE1,KEY2=VALUE2"
```

## Update the Deployment

To update your app after making changes:

```bash
# Using source deploy
gcloud run deploy csv-to-markdown --source .

# Or rebuild and deploy Docker image
docker build -t gcr.io/YOUR_PROJECT_ID/csv-to-markdown .
docker push gcr.io/YOUR_PROJECT_ID/csv-to-markdown
gcloud run deploy csv-to-markdown \
  --image gcr.io/YOUR_PROJECT_ID/csv-to-markdown
```

## Local Docker Testing

Before deploying, test the Docker container locally:

```bash
# Build the image
docker build -t csv-to-markdown .

# Run locally on port 8080
docker run -p 8080:8080 csv-to-markdown

# Access at http://localhost:8080
```

## Cost Considerations

Cloud Run pricing:
- Free tier: 2 million requests per month
- Pay only when your app is processing requests
- Very cost-effective for low to medium traffic

## Monitoring

View logs and metrics:
```bash
# View logs
gcloud run logs read csv-to-markdown --limit 50

# Or use the Cloud Console:
# https://console.cloud.google.com/run
```

## Custom Domain

To use a custom domain:

1. Go to Cloud Run console
2. Select your service
3. Click "Manage Custom Domains"
4. Follow the instructions to verify and map your domain

## Troubleshooting

### Port Issues
Make sure your app listens on the port specified by the `PORT` environment variable (default: 8080 in Cloud Run)

### Memory Issues
If your app needs more memory:
```bash
gcloud run deploy csv-to-markdown --memory 1Gi
```

### Build Failures
Check the build logs:
```bash
gcloud builds list
gcloud builds log BUILD_ID
```

## Security

To require authentication:
```bash
gcloud run deploy csv-to-markdown --no-allow-unauthenticated
```

Then use Firebase Authentication or Cloud IAM for access control.

