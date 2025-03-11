##  AWS Rekognition & CloudTrail-based image analysis system 🔍

# Overview 🚀
This project automates image analysis using AWS Rekognition to detect objects and labels in images stored in AWS S3, while ensuring security and compliance tracking via AWS CloudTrail.
# Problems
Problem1: Manual Image Tagging is Slow & Error-Prone
  - Businesses and researchers manually tag images for catagorization for machine learning and AI models
  - This is time-consuming inconsistent and inefficient
Solution: AWS Rekognition automates label detection, providing high-accuracy classifications instantly.
Impact: E-commerce platforms, media companies, and researchers save time & improve accuracy.

Problem2: No Security or Tracking for Image Processing
  - How do we know who is analyzing which images?
  - Companies using AWS Rekognition lack API-level tracking, making it harder to ensure data security & compliance.
Solution: AWS CloudTrail logs every Rekognition API request, ensuring full transparency and auditability.
Impact: Improves data security, regulatory compliance (GDPR, HIPAA), and security tracking.

Problem3: Unstructured Image Analysis Data is Hard to Use
  - Raw AI responses from image detection aren't formatted for easy integration into databases or applications.
  - Extracting meaningful insights from AWS Rekognition’s output requires additional processing.
Solution: The Python script formats and saves structured JSON outputs, making it easy to search, filter, and integrate.
Impact: Data is ready for AI models, dashboards, and automation workflows.

## System Architecture 🏗️
Components & Workflow:
  ~ S3 Bucket (image-label-bucket) – Stores input images.
  ~ AWS Rekognition – Detects image labels (e.g., "Cat", "Mountain").
  ~ CloudTrail (cloudtrail-logs-865) – Logs all DetectLabels API requests.
  ~ Python Script (image_label.py) – Automates the process:
    - Retrieves images from S3
    - Sends them to AWS Rekognition
    - Saves detected labels in JSON format
  ~ CloudTrail Logs – Used for auditing API activity.

There is a word document for step-by-step instructions with commands and expected output for how to Set Up & Run the Project 📌

## Sample Output & Results
Example: Detected Labels for an Image
Running the script for an image like mycat-unsplash.jpg might return:
{
   "Labels": [
        {
            "Name": "Cat",
            "Confidence": 99.9
        },
        {
            "Name": "Pet",
            "Confidence": 98.5
        }
    ]
}

JSON files are saved locally as:
mycat-unsplash.jpg_labels_YYYYMMDD_HHMMSS.json

CloudTrail Logs for API Calls
List CloudTrail logs in S3: aws s3 ls s3://cloudtrail-logs-865/AWSLogs/<account-id>/CloudTrail/ --recursive
Download and inspect logs:
    aws s3 cp s3://cloudtrail-logs-865/AWSLogs/<account-id>/CloudTrail/<log-file-name> ./
    gunzip <log-file-name>.json.gz
    cat <log-file-name>.json | jq '.Records[] | select(.eventName=="DetectLabels")'
Sample log output for an API call:
json
{
    "eventTime": "2024-12-10T19:00:00Z",
    "eventName": "DetectLabels",
    "awsRegion": "us-east-1",
    "requestParameters": {
        "image": {
            "s3Object": {
                "bucket": "image-label-bucket",
                "name": "mycat-unsplash.jpg"
            }
        }
    }
}

Who Can Benefit From This? 🎯 
   ~ E-Commerce & Digital Media → Automate product image categorization.
   ~ Security & Compliance Teams → Track Rekognition API activity for audits.
   ~ AI & Data Scientists → Process structured image datasets easily.
   ~ Researchers & Wildlife Conservationists → Monitor and analyze environmental images.

License
This project is licensed under the MIT License.

References
[AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
[Boto3 Python SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 
