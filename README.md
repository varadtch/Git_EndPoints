{\rtf1\ansi\ansicpg1252\deff0\deflang16393{\fonttbl{\f0\fnil\fcharset0 Calibri;}{\f1\fnil\fcharset2 Symbol;}}
{\*\generator Msftedit 5.41.21.2510;}\viewkind4\uc1\pard\sa200\sl276\slmult1\lang9\f0\fs22\par
\fs48 Setting up the environment\fs22\par
General Note : Check if virtualenv is installed in the environment. If not install virtualenv. It is always a good practice to isolate the code base to an environment so that the installing/removing modules doesn't impact the python installation of the system..\par
\fs36 Install virtualenv\fs22\par
\pard{\pntext\f1\'B7\tab}{\*\pn\pnlvlblt\pnf1\pnindent0{\pntxtb\'B7}}\fi-360\li720\sa200\sl276\slmult1\ul\b Windows :\ulnone\b0  Assumption Python is installed in C:Python27\par
{\pntext\f1\'B7\tab}C:\\Python27\\Scripts\\pip.exe virtualenv\par
\ul\b{\pntext\f1\'B7\tab}Linux/Debian :\ulnone\b0  Assumption is pip is already installed on your system.\par
{\pntext\f1\'B7\tab}sudo pip install virtualenv\par
\pard\sa200\sl276\slmult1\par
\pard\sa200\sl276\slmult1\fs36 Setup virtualenv\ul\i\fs22\par
\pard\sa200\sl276\slmult1\b\i0 Windows:\ulnone\i\par
\b0\i0 C:\\Python27\\Scripts\\virtualenv.exe CodeBase\par
cd <path to CodeBase>\par
\ul\b Linux/Debian\ulnone\b0\par
virtualenv CodeBase\par
cd <path to CodeBase>\par
\par
\fs36 Activate virtualenv\fs22\par
\ul\b Windows:\ulnone\b0  \par
Scripts\\activate.bat\par
\ul\b Linux/Debian:\ulnone\b0\par
 source bin\\activate\par
\par
\fs36 Clone the git repo\fs22\par
Create a directory where the programs from git will be clonned\par
mkdir <Programs directory>\par
clone the git into this directory\par
pip install -r requirements.txt\par
\par
All Done .. Environment is all set for running the scripts.\par
\par
}
 