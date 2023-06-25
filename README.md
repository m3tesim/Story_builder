# To run the project
python3 -m flask --app server.py run 

# STORY BUILDER APP
An Online story builder Game where users can create random stories together 

- What is it about?  
  The story game is a fun group activity which develops each player’s storytelling skills.

- What is the "new feature" which i have    implemented that we haven't seen before? 
  -auto update for the comment section after user write a new line of the story
  -login and logout for users
  -link between stories's data and comments's data 
  -adding authorization in  pages so user can access app only if logged in

  

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? 
List those here (if any).

## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - datetime:
- [x] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name:utilities.py
  - Line number(s):93
  - Name of two properties:name,color
  - Name of two methods: get_date,data
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to a file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name:server.py
  - Line number(s):15
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name:server.py
  - Line number(s):25
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  # Story_builder
