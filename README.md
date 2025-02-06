# This is my image recognition python script.
The purpose of this script is to be able to take an image input and then be able to output recognizable elements within the image to a new .jpg file.

## Environment Setup
### Pyenv
Install and Update Dependencies\n
`sudo apt update -y`

Run the following command to install all of pyenv's dependencies
`sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git`


Run the following command to install the script of pyenv
`curl https://pyenv.run | bash`

Run the following commands to set environment variables for pyenv
`echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc`
`echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc`
`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc`

Restart the shell to begin using pyenv
`exec "$SHELL"`

Ensure that pyenv was successfully installed by running the following command
`pyenv`


Once pyenv has been successfully installed there are two versions of python that will need to be utilized for this project. 3.7.6 and 3.9.13. To install these versions type the following commands.
`pyenv install 3.7.6`
`pyenv install 3.9.13`

Ensure that each version has been installed successfully by typing the following command and then you are able to star the next phase.
`pyenv versions`


### Python Virtual Environment
These steps are going to result in you completely setting up your python virtual environment and from there you will be ready to code!
First we will create a directory for our project.
`mkdir MyProject; cd MyProject`

Now that we are inside of our project environment, we will start by setting which version of python we will be using for the installation of ImageAI dependencies. This is completed by executing the following command.
`pyenv local 3.9.13`

Once this command has executed enter the following command to enter python and ensure the proper version is selected. This will be visible in the python MOTD.
`python`

To exit type:
`exit()`

Now we have confirmed the proper version of python is running in our directory, we will create the virtual environment and enter it by typing the following commands.
`python -m venv .venv`
`source .venv/bin/activate`

We will know this was successful if the terminal prompt is led by a (.venv) tag. From here you are able to start installing the depencies for ImageAI.
`pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3`

Once this command has finished there may be a warning to update your pip version. Ignore this warning as long as there wasn't an error everything should work. Now we are going to switch our version of python again. First complete this by deactivating the virtual environment by typing the following command.
`deactivate`

We will change the version of python now using the same method as before.
`pyenv local 3.7.6`

Once this command has finished enter the virtual environment again.
`source .venv/bin/activate`

When you are inside the virtual environment you can install the last library needed.
`pip install imageai --upgrade`


## Running the script
Once you have installed the detector.py into your work directory you will need to install any .jpg image for the script to detect objects in. The name of this image must be `image.jpg`. You can run the script by typing the following command while inside the virtual environment.
`python detector.py`

After the script has finished running, you will see the new file in your directory along with everything the script was able to identify.

## Credits
Image AI Documentation
https://imageai.readthedocs.io/en/latest/

PyEnv Installation
https://www.dedicatedcore.com/blog/install-pyenv-ubuntu/

## Author
This documentation was written by Jacob Boesen on 02/06/2025
Contact: jacob.boesen(at)cdw(dot)com
