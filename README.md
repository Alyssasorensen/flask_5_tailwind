## flask_5_tailwind
# HHA 504 Homework Assignment 5

This task offers you the opportunity to gain practical experience in video hosting, designing a Flask application with Tailwind CSS, and launching it on a cloud platform. You will make use of CDN services provided by Google Cloud or Azure to enhance video delivery, guaranteeing a smooth viewing experience for global audiences.

## Design Rationale and Principles Followed

I decided to use an online healthcare informatics program informational video to show on the CDN and flask app. The viewer will see an informational video as well as the word "section" and "description." "Section" displays the time when the director starts talking about the program in the video and the decription explains this. 

## Steps for Setting Up and Using the CDN with the Flask App

Setting up and using Azure's Content Delivery Network (CDN) to host your video involves several steps. Below are the general directions for hosting your video on Azure CDN. Keep in mind that specific steps may vary depending on your Azure setup and the video file you want to host.

**Steps to Host Your Video on Azure CDN:** 

1. Upload Video to Azure Storage:

If you haven't already, upload your video file to an Azure Storage Account. You can use the Azure Portal, Azure Storage Explorer, or Azure CLI to do this.

2. Create an Azure CDN Profile:

In the Azure Portal, go to the Azure CDN service and create a new CDN profile. Choose the Standard Verizon or Standard Akamai option, depending on your needs.

3. Create an Azure CDN Endpoint:

Within your CDN profile, create a CDN endpoint. Configure the endpoint to use your Azure Storage Account as the origin, and specify the path to your video file.

4. Configure Caching and Content Rules:

Configure caching rules for your CDN endpoint. You can specify cache duration, query string handling, and other caching options.

Set up content rules if you need to customize how the CDN serves your video files.

5. Verify and Test the CDN Endpoint:

Once the CDN endpoint is set up, verify that it's working correctly. You should be able to access your video through the CDN URL.

6. Integrate CDN URL with Your Application:

Update your Flask app or web application to use the CDN URL for embedding the video. Replace the local video file URL with the CDN URL in your HTML or application code.

7. Performance and Security (Optional):

Explore additional options for optimizing CDN performance, such as enabling HTTP/2 or setting up a custom domain.

Consider implementing security features like access controls and HTTPS if needed.

8. Test CDN Performance:

Test the performance of your CDN-hosted video to ensure that it loads efficiently and is accessible from different regions.

9. Monitoring and Scaling (Optional):

Set up monitoring and alerts to keep an eye on CDN performance.

If your app experiences increased traffic, consider scaling your CDN resources to handle the load.

10. Documentation and Troubleshooting:

Refer to Azure's official documentation for Azure CDN for any specific configurations or troubleshooting steps.


## Steps for Deploying the Flask App to the Chosen Cloud Platform

**To deploy your Flask app to Microsoft Azure using Azure App Service with Git, you can follow these instructions:**

**Step 1:** Prepare Your Flask App for Deployment

1a. Make sure your Flask app is fully functional and follows best practices for production-ready applications. This includes configuring your database, setting environment variables, and securing your application.

1b. Create a requirements.txt file for your Flask app to specify its dependencies. 

**Step 2:** Create an Azure App Service

2a. Open a terminal or command prompt and log in to your Azure account using the Azure CLI:

```
az login
```

2b. Create a resource group for your app (replace <resource-group-name> with a unique name for your resource group):

```
az group create --name <resource-group-name> --location <azure-region>
```

2c. Create an Azure App Service plan:

```
az appservice plan create --name <app-service-plan-name> --resource-group <resource-group-name> --sku FREE
```

2d. Create the Azure App Service:

```
az webapp create --name <app-name> --resource-group <resource-group-name> --plan <app-service-plan-name>
```

Replace <app-name> with a unique name for your app.

**Step 3:** Deploy Your Flask App to Azure Using Git

3a. Navigate to your Flask app's root directory and initialize a Git repository (if not already done):

```
git init
```

3b. Add your code and commit it to the Git repository:

```
git add .
git commit -m "Initial commit"
```

3c. Configure your Azure App Service as a Git remote. Replace <app-name> with the name of your Azure App Service:

```
az webapp deployment source config-local-git --name <app-name> --resource-group <resource-group-name>
```

3d. Follow the instructions provided in the command output to add the Git remote to your local Git repository.

3e. Push your code to Azure App Service:

```
git push azure master
```

3f. The deployment process will begin, and your Flask app will be deployed to Azure App Service.

**Step 4:** Verify Your Azure App

4a. Once the deployment is complete, you'll receive a URL for your deployed Flask app (e.g., https://<app-name>.azurewebsites.net).

4b. Open a web browser and visit the URL of your deployed Flask app to verify that it's running correctly.

**Step 5:** Manage Your Azure App

You can manage your Azure App Service, monitor its performance, and configure custom domains through the Azure Portal or by using the Azure CLI.

## Observations and Benefits of Using a CDN and Cloud Deployment

## Challenges Encountered and How I Addressed Them