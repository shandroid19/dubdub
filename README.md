# dubdub.ai assignment
### This is a Todo list backend developed using flask.
## steps to run the application:
- Clone the repo by running "git clone https://github.com/shandroid19/dubdub.git" command in the terminal.
- Open the terminal in the directory of the cloned repository.
- Run the command: " docker build --tag dubdub-image . " to create a docker image for the application (Will be executed only if docker daemon process is running).
- Run the command: " docker run -p 5000:5000 dubdub-image " to create a container instance of the application running on port 5000. 
- The http requests can be made to http://127.0.0.1:5000 
