1. What is the difference between model training and model deployment?
	Model training means teaching the model using data so it can make predictions.
	Model deployment means making the trained model available for others to use — like through an API or web app.
	
2. Why do we save trained models using joblib or pickle?
	We save trained models using joblib or pickle so we don’t have to train them again every time. We can simply load the saved model and use it for predictions.

3. What are the advantages of serving ML models through REST APIs?
	Anyone can access the model from any device using HTTP requests. It allows easy integration with websites, apps, or other systems. It makes sharing and using the model faster and simpler.

4. Explain the purpose of each HTTP method (GET, POST) used in your API.
	GET: Used to get information, like checking if the API is running (/health).
	POST: Used to send data to the server, like sending flower features to get a prediction (/predict).

5. What is Docker, and why is containerization important for ML deployment?
	Docker is a tool that runs applications inside containers. Containerization keeps everything (code, libraries, model) together, so the app runs the same on every system without setup problems.

6. How does Docker ensure consistency across different environments (dev, staging, production)?
	Docker uses containers that include the same setup, dependencies, and versions.
	This makes sure the app behaves the same in development, testing, and production.

7. What is the role of requirements.txt in Python projects and Docker containers?
	requirements.txt lists all the Python libraries needed for the project.
	Docker uses this file to install everything automatically when building the container.

8. Why do we expose ports in Docker containers?
	We expose ports so that the app running inside the container can be accessed from outside. For example, we expose port 5000 so we can open the API in a browser or send requests to it.

9. How would you scale your API to handle 1000 requests per second?
	We can scale by:
	Running multiple containers of the same app.
	Using a load balancer to share traffic between containers.
	Using cloud services like Kubernetes or AWS ECS for auto-scaling.

10. What are some security considerations when deploying ML models as APIs?
	Validate all input data before processing.
	Use HTTPS to protect data transfer.
	Add authentication or API keys.
	Don’t expose sensitive data or model details.
	Monitor and limit the number of requests to prevent abuse.
