# CloudResume_BackEnd
Infrastructure as Code for the backend architecture of a website. It also consist of a serverless function for a site visit counter

The entire architecture for my cloud resume is the following:
![image](https://user-images.githubusercontent.com/66120020/174936435-e38951bf-3713-4035-93b9-625ddd60b8f6.png)

The entire backend infrastructure is deployed via IaC via Sam template. This can be altered by using the following commands:

sam build
sam deploy

CI/CD pipeline is triggred and changes to infratructure is only done if the unit tests pass. 
