1. Create a Virtual Environment
** In your backend ** -> python -m venv venv 

2. Activate the Virtual Environment -> venv\Scripts\activate

3. Install dependencies -> pip install mysql-connector-python
                                             -> pip install flask
                                             -> pip install flask_sqlalchemy


4. Add '.gitignore' file

5. Add Entries to .gitignore
************************
# Python virtual environment
venv/

# Bytecode files
__pycache__/
*.pyc

# Flask instance folder (optional, if you use instance for configuration)
instance/

# IDE or editor configurations
.vscode/
.idea/

5. To run BACKEND -> python run.py


