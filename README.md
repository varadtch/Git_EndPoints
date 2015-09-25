# Git_EndPoints
Delivered for review

Setting up the environment

General Note : Check if virtualenv is installed in the environment. If not install virtualenv. It is always a good practice to isolate the code base to an environment so that the installing/removing modules doesn't impact the python installation of the system..

Install virtualenv
Windows : Assumption Python is installed in C:Python27
C:\Python27\Scripts\pip.exe virtualenv

Linux/Debian : Assumption is pip is already installed on your system.
sudo pip install virtualenv

Setup virtualenv
Windows:
C:\Python27\Scripts\virtualenv.exe CodeBase
cd <path to CodeBase>

Linux/Debian
virtualenv CodeBase
cd <path to CodeBase>

Activate virtualenv
Windows: 
Scripts\activate.bat
Linux/Debian:
 source bin\activate

Clone the git repo
Create a directory where the programs from git will be clonned
mkdir <Programs directory>
clone the git into this directory
pip install -r requirements.txt

All Done .. Environment is all set for running the scripts.

