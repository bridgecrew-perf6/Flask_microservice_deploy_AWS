# Flask_microservice_deloy_AWS
[![Python application test with Github Actions](https://github.com/kaifeng-yu16/Flask_microservice_deloy_AWS/actions/workflows/main.yml/badge.svg)](https://github.com/kaifeng-yu16/Flask_microservice_deloy_AWS/actions/workflows/main.yml)

This is duke ids721 project1. This project builds a translation microservice using Flask and deploys it on AWS using AWS App Runner. It is implemented using a pre-trained model from hugging face. You can use it to translate Chinese texts into English.

## How to use
To use this app, go to website https://cm2uvp39yf.us-east-1.awsapprunner.com/, enter the chinese text you want to translate, and hit "translate" button.


![image](https://user-images.githubusercontent.com/90477174/151687738-a2016c36-7f58-4e21-988a-61483affe767.png)


### Some sample chinese text
"一个人" means alone in English.

"我喜欢数据科学“ means "I love data science"

"明天我要带我的猫去洗澡“ means "I am taking my cat to shower tomorrow"

## How to deploy
To deploy this app on AWS using AWS App Runner, follow the step:

- Login into AWS Management Console (https://console.aws.amazon.com/console/).
- Selete AWS service: AWS App Runner.
- Click "Create service".
- In the following page, in "Source" section, select "Source code repository" and add your github repo which contains source code of this app.
- In "Deployment settings" section, select "Automatic" to automaticlly deploy your code.
- Click "next" and go to step2.
- Select "Configure all settings here", "Python 3" and enter "pip install -r requirements.txt", "python main.py", "8080" as shown.

![image](https://user-images.githubusercontent.com/90477174/151688085-cfc04aca-1f12-412f-8a4a-93ce676b5a24.png)

- Keep clicking "next" until click "Create & deploy"
- After a few minutes, your app will be deployed and good to go.
