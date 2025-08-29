![](AWS%20Rekognition.png)

1.Upload the image to Amazon S3 bucket.

2.The images stored in the S3 bucket will be used to analyse and generate labels.

3.Amazon Rekognition will be used to analyse the selected image from the S3 bucket and detectecting labels with their confidence levels.

4.IAM will be used to provide user authentication and access to the Amazon CLI on your system.

5.AWS Command Line Interface will be used for interacting with AWS Services.

6.Python file will consist of the programming logic for extracting the image from S3 and running detect_labels operation from Rekognition.

7.The output will consist of number of specified labels according to the input with their confidence levels.

8.A pop-up screen will be generated with the image choosen from S3 bucket with bounding boxes around the detected labels.
