[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10363836&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 2 Instruction

To set up the app:

1. Install all dependancy in requirements.txt , using pip install -r requirement.txt

2. make sure data.db is in the data folder, if not, run flask_app\data\csv_to_sqlite.py to create the database

3. If the app is to be ran using a terminal, open __init__.py and swap 2 lines of code
   following the comments in the code.


# Design and Implementations
Looking back on my design in COMP0035, my app now is very different. THis is because I designed with a REST api in mind, but made an app with ML functionality instead. However, my list of requirement is still mostly applicable
## Requirements
There were 26 must haves in my requirement table. AMong which, 18 were implemented, 4 were not applicable and 4 were not implemented. 
Not all of the requirements were applicable because the requirements were desinged with an Rest api in mind.
The ones not implemented were related to the use of flask-security and flask-email. Although I have tried using them, it created a bug that I couldn't fix and therefore were aborted.
I also attempted to create a page for letting user create a store of datas, that did not go well as that requires the database to interact.
## URL designs
In general, the way I have implemented by routes were very different to the design. In the design, I had 3 main route, /store, /data-entry and /compare. Only data entry were kept. I have also planned to mainly use put method but ended up using post method instead. The orginal consideration is based on the idempotency of the put method. However, in this coursework, I choose to mainly use the post method as not all resource have a pre-defined URL. Most are created by passing a query to an html template. If I were to continue developing a REST api, I would have utilised the put method more.
## Should have
# Fixing errors
## Import Error in Testing
When attempting to create fixtures, I encountered a ModuleNotFoundError despite having installed the necessary modules in my virtual environment. I tried various directory structures and renaming files, but the issue persisted. I eventually discovered that I had not installed the code in the Git workflow, which resolved the import error.
## Error in Hook Function pytest_setup_options()
When running tests in GitHub Actions, the following error was returned:

``` python
INTERNALERROR>     raise PluginValidationError(
INTERNALERROR> pluggy._manager.PluginValidationError: unknown hook 'pytest_setup_options' in plugin <module 'conftest' from '/home/runner/work/comp0034-cw2-i-JocelynS371/comp0034-cw2-i-JocelynS371/tests/conftest.py'>
```

After consulting with a friend familiar with Pytest and Selenium, I attempted to add the line 
`@pytest.hookimpl(optionalhook=True) `
to the hook function, which resolved the error.  
## Error with config
There is a slight error with the config. While it is fine in cintinous intergration, when the command
`python -m flask --app 'flask_app:create_app("config.DevelopmentConfig")' --debug run`    
is entered into the terminal, the following error is returned   
`Error: Failed to parse arguments as literal values: 'create_app(config.DevelopmentConfig)'.   `   
Changing variable names did not resolve the error. As a workaround, two lines of code need to be swapped in __init__.py when running the app in the terminal. See the comments in __init__.py for more details.

# Testing
I have chose to test if the routes are assessable and if they return the correct status code. When I tried to test the route while logged in, it just doesn't work. Here is the screenshot to the tests   
[!test] \screenshots\Screenshot_test.png   
I have also used github for continous intergration, here is the link to the github action
https://github.com/ucl-comp0035/comp0034-cw2-i-JocelynS371/actions
The template of yml is from python application. 
# Tools and technique
link to github repo:
https://github.com/ucl-comp0035/comp0034-cw2-i-JocelynS371
I have also done liniting which could be seen in the workflow.






