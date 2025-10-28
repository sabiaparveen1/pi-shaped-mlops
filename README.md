Project description 
	This project is about building and deploying a Machine Learning model as a REST API using Flask and Docker.
	I used the Iris Flower Dataset, which contains data of different iris flowers with four features: sepal length, sepal width, petal length, and petal width.
	The goal of the project is to predict the type of iris flower — Setosa, Versicolor, or Virginica.
	The model is trained using Scikit-learn and saved with joblib.
	Then, a Flask API is created to serve predictions through HTTP requests.
	Finally, the whole application is containerized using Docker so it can run the same on any system.

	Main API endpoints:
		/ → Shows basic API info
		/health → Health check (to see if the API is running)
		/predict → Takes input features and returns the predicted flower type

Setup and installation instructions 
	installed python3, pip, flask, Scikit-learn

	
How to train the model 
	python3 train_model.py

How to run the API locally
	python3 app.py
	 
How to build and run the Docker container 
	docker build -t iris-ml-assignment .
	docker run -p 5000:5000 iris-ml-assignment

	
Example API requests and responses 

API Endpoints

		curl http://127.0.0.1:5000/health
		response status:{ok}
		
		curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features":[5.1, 3.5, 1.4, 0.2]}'
response {
  "prediction": "setosa",
  "class_index": 0
}

