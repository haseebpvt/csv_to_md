#!/bin/bash

# Script to deploy to Google Cloud Run

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Deploying CSV to Markdown Converter to Google Cloud Run${NC}"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ gcloud CLI is not installed${NC}"
    echo "Install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Get project ID
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)

if [ -z "$PROJECT_ID" ]; then
    echo -e "${RED}❌ No GCP project is set${NC}"
    echo "Set it with: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

echo -e "${GREEN}✓ Using project: ${PROJECT_ID}${NC}"
echo ""

# Ask for service name
read -p "Enter service name (default: csv-to-markdown): " SERVICE_NAME
SERVICE_NAME=${SERVICE_NAME:-csv-to-markdown}

# Ask for region
read -p "Enter region (default: us-central1): " REGION
REGION=${REGION:-us-central1}

# Ask if authentication is required
read -p "Allow unauthenticated access? (Y/n): " ALLOW_UNAUTH
ALLOW_UNAUTH=${ALLOW_UNAUTH:-Y}

if [[ $ALLOW_UNAUTH =~ ^[Yy]$ ]]; then
    AUTH_FLAG="--allow-unauthenticated"
else
    AUTH_FLAG="--no-allow-unauthenticated"
fi

echo ""
echo -e "${BLUE}📦 Deploying...${NC}"
echo ""

# Deploy to Cloud Run
gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --region "$REGION" \
  --platform managed \
  $AUTH_FLAG \
  --memory 512Mi \
  --cpu 1 \
  --max-instances 10

# Check if deployment was successful
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Deployment successful!${NC}"
    echo ""
    echo "Your app is now live at the URL shown above."
    echo ""
    echo "To view logs:"
    echo "  gcloud run logs read $SERVICE_NAME --limit 50"
    echo ""
    echo "To delete the service:"
    echo "  gcloud run services delete $SERVICE_NAME --region $REGION"
else
    echo ""
    echo -e "${RED}❌ Deployment failed${NC}"
    exit 1
fi

