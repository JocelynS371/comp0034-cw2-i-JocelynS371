[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10363836&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 2 starter code template

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 


# Fixing error
## Import error in testing
I attempted to create fixtures, which required me to import certain class and functions from the app. I keep getting modul not found error. I have tried using differnt setup.py strctures, but to no avail. I also tried renaming the files. Didn't work.   
I have checked the list of modules installed in my venv, flask_app is one of them. however, the conftest.py cannot seems to find the module. I have also tried importing only the py, but because they are interdependent, it did not work as well. 
I figured it out at the end, I did not install the code in the git workflow. After some attempts, the import is now working.
## Error in hook function pytest_setup_options()   
When running in github action, the following error is returned.
INTERNALERROR>     raise PluginValidationError(
INTERNALERROR> pluggy._manager.PluginValidationError: unknown hook 'pytest_setup_options' in plugin <module 'conftest' from '/home/runner/work/comp0034-cw2-i-JocelynS371/comp0034-cw2-i-JocelynS371/tests/conftest.py'>
After reading online and looking at documentation. THe error is not fixed and the hook function is editted out for a while.
After consulting a friend familar with pytest and selenium, attempted to add a line   
@pytest.hookimpl(optionalhook=True)   

## Error with config
There is a slight error with the config. While it is fine in cintinous intergration, when the command
python -m flask --app 'flask_app:create_app("config.DevelopmentConfig")' --debug run   
is entered into the terminal, the following error is returned
Error: Failed to parse arguments as literal values: 'create_app(config.DevelopmentConfig)'.   
The error cannot seems to be fixed by changing variable names, therefore a workaround is used, where when the app is ran in the terminal, 2 lines of code need to be swapped in __init__. See comment in __init__.






