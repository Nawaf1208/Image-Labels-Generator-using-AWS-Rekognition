import sys, json, boto3, botocore

REGION = "YOUR_REGION"
PROFILE = "rekog-demo"   # the profile you configured
BUCKET = "YOUR_BUCKET_NAME"
KEY = "dog.jpg"          # change if needed

def main():
    # If you want to pass bucket/key from CLI: python detect_labels.py BUCKET KEY
    bucket = sys.argv[1] if len(sys.argv) > 1 else BUCKET
    key    = sys.argv[2] if len(sys.argv) > 2 else KEY

    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    rekog = session.client("rekognition")

    try:
        resp = rekog.detect_labels(
            Image={"S3Object": {"Bucket": bucket, "Name": key}},
            MaxLabels=10,
            MinConfidence=70.0
        )
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}))
        sys.exit(1)

    labels = resp.get("Labels", [])
    print("\nDetected labels:")
    for l in labels:
        print(f"- {l['Name']} ({l['Confidence']:.1f}%)")

    # Save raw JSON (handy for your portfolio)
    with open("labels_output.json", "w", encoding="utf-8") as f:
        json.dump(resp, f, indent=2)
    print("\nSaved full response to labels_output.json")

if __name__ == "__main__":
    main()
