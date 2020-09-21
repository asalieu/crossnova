### IMPORTANT NOTE
In this excerciseI used vscode as my development environment and docker for Windows64 bit on machine. I also using other python frameworks for 
testing such as jupyter notebook and Spyder.

However because I am currently really busy preparing for my final thesis presentation in october schedule for october, i am not able to look at 
the rest of the exercises hence i have tried to cover as much as possible all the parts in this excersise as accordingly as possible and putting 
into consideration all the good standards such as security, readibility, architecture, scalability etc


###PROJECT NAME
crossnova: This is a python dash application that simulate a visualization of a auto data on scatter plot given x,y (numeric columns) selection.

###PROJECT REQUIREMENT
For this project to run, the below technical requirements should be fullfiled 
1) Python 3.7 version must be present on the system 
2) Ensure that the postgrsql connection string configurations are created in .env file in accordance with the parameter names used in app.py file
3) The .env file must be present in the same directory with the app.py file
4) Ensure the requirements.txt file properties are all installed 


###INSTALLATION
This Program can be run both on a docker conatainer and locally using the python web engine.

To run locally utilizing python web engine:

---On VsCode: 
Firstly, ensure you are have VS Code Python extension
1) Then navigate to the project directory
2) Open the app.py file in the editor window
3) Then click the Run Python File in Terminal play button in the top-right side of the editor
Then you can now goto http://localhost:9000/

-- To run as a docker container
In terminal, cd into the project directory
1) Run the command docker build -t crossnova .
2) Run docker run -d -p 9000:8050 
Then you can now goto http://localhost:9000/
