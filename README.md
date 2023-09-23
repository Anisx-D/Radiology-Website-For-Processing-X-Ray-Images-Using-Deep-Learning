# Radiology-Website-For-Processing-X-Ray-Images-Using-Deep-Learning  
  
Realised as the Design and Development Project for ENSI
  
## Installation:  
    
### Activate Virtual Environment:  

If you're using a virtual environment (which is recommended for isolating project dependencies), activate it. Navigate to your project directory and run the appropriate command for your operating system.
  
On Windows:  
  
`myenv\Scripts\activate`  
  
On macOS and Linux:  
  
`source myenv/bin/activate`  
  
### Navigate to Project Directory:  

Open a terminal or command prompt and navigate to the root directory of the cloned repository.  
  
### Install Dependencies:  

If you haven't already installed the project's dependencies, use pip to install them. You can do this by running:
  
`pip install -r requirements.txt`  
  
Ensure that you have a requirements.txt file in your project directory with all the necessary package dependencies listed.  
  
### Apply Database Migrations:  
  
Django projects often use databases to store data. To apply the database migrations and create the database schema, run the following commands:  
  
`python manage.py makemigrations`  
`python manage.py migrate`  

  
### Create a Superuser (Optional):  
  
Create a superuser with the following command:
  
`python manage.py createsuperuser`  
  
Follow the prompts to set a username, email, and password for the superuser.  
  
### Run the Development Server:  
  
Start the Django development server with the following command:  
  
`python manage.py runserver`  
  
By default, the server will run on http://127.0.0.1:8000/. You can access this project by opening a web browser and navigating to this address.  
  
### Access the Admin Interface (Optional):  
  
You can access the admin interface by going to http://127.0.0.1:8000/admin/ and logging in with the superuser credentials.  
