# Script: AWS Rekognition Image Label Detector with CloudTrail Verification
# Author: Preshika Basnet
# CIT 438: Cloud Computing
# Instructor: Dr. Victoria Uti
# Final Project: Automating Image Analysis with AWS Rekognition and CloudTrail Integration 

import boto3
import json
from datetime import datetime

# Function to analyze a single image using Rekognition
def analyze_image(bucket_name, image_name):
    # Initialize Rekognition client
    rekognition_client = boto3.client('rekognition')
    # Call the Rekognition DetectLabels API
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_name
            }
        },
        MaxLabels=10
    )

    # Save and print results
    labels_output = ""
    print(f"Detected labels for {image_name}:")
    for label in response['Labels']:
        label_info = f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%"
        print(label_info)
        labels_output += label_info + "\n"
    # Save the labels to a file
    output_filename = f"{image_name}_labels_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_filename, 'w') as f:
        json.dump(response, f, indent=4)
    print(f"\nLabels saved to: {output_filename}\n")
    return output_filename

# Main function for running the script
if __name__ == "__main__":
    # Specify the bucket and image details
    bucket_name = "image-label-bucket"
    image_name = " marek-piwnicki-IOnWkCabL6Q-unsplash.jpg"

    # Analyze the image
    print("Running Rekognition label detection...")
    result_file = analyze_image(bucket_name, image_name)

    # Notify completion
    print("Rekognition analysis complete!")
    print(f"Results saved in: {result_file}")

    # Verify CloudTrail logs
    print("\nYou can now check CloudTrail logs in your S3 bucket (cloudtrail-logs-865) for API activity.")
                                             