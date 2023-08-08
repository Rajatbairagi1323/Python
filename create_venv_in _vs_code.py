# Create virtual environment in vs code.

# PRESTEPS --> check the python is install or not.
python3/python --version   # Not install first install it / already install please take the step 2

pip install package_name

# STEP 1) First you make a folder in for ex: Desktop/Download/documents/etc....

# STEP 2) locate your folder in vs code by click on file option --> new folder --> locate it.

# STEP 3)  write a command in terminal open terminal  press the key (ctrl+shift+p) to open the terminal.
python3 -m venv venv    # To paste this commands in vs code or any terminal (ctrl+shift+v) for paste  
                        # Shift is necessary to copy/paste/cut in terminal.  (ctrl+shift+c/p/x)
#STEP 4)
.\.venv\Scripts\activate

#STEP 5)
# your virtual environment is created.

# STEP 5) deactivate the virtual environment use command:
deactivate

