# myapp1
# Text Analysis Web Application

## Setup Instructions

1. SSH into your EC2 instance.
2. Install necessary packages:
    ```bash
    sudo yum update -y
    sudo yum install python3 python3-pip -y
	pip install transformers torch boto3
	pip install transformers torch
	sudo yum install httpd
	sudo yum install git -y
	
    ```
3. Unzip the code file or Unzip the zip file or Clone the git repo using this command:
	```bash
	git clone https://github.com/linhntk123/myapp1.git
    ```
4. Navigate to the project folder:
	```bash
	    cd myapp1
    ```
5. Start httpd:
    ```bash
    sudo systemctl start httpd
    ```
6. Run the Flask application:
    ```bash
    sudo python3 main.py runserver 0.0.0.0:80

Note: If port 80 has been used, kill all processes using it:
	```
	sudo fuser -k 80/tcp

## Usage

1. Open a web browser and navigate to the public IP of your EC2 instance.
2. Enter text into the textarea and press the "Analyze" button.
3. View the results, which include detected entities and syntax tokens.
