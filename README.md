## PDFParser
A pdf table parse which uses tabula-py.

## Requirements
 - Python 3
 - tabula-py (and its requirements)
 - Java 7+ (for tabula-py)
 
### OS
Created and works under Windows 10.

## Setup Instructions
 - Windows commands assume the latest version of Windows 10 is used.

#### 1. Download and install Python 3 version 3.6.5 or higher.
 - The latest python version can be downloaded at: https://www.python.org/downloads/
 - In Ubuntu version 18.04, Python 3.6.5 is installed by default and uses *python3* instead of *python*.
   - On Linux, this can be installed with the command:
   
            $ sudo apt install python3

#### 2. Install the pip module.
 - This is installed with the latest python version by default. If it is not installed, follow the installation instructions at: https://pip.pypa.io/en/stable/installing/
   - On Linux, this can be installed with the command:
   
            $ sudo apt install python3-pip

#### 3. Install requirements:
 - In the directory containing *app.py*, run one of the following commands based on which operating system is being used.
   - Windows Command Prompt:
 
            $ py -m pip install -r requirements.txt
   - Linux:
 
            $ pip3 install -r requirements.txt

## Usage
#### 1. Place the pdfparse.py file in a directory containing pdf files to process.
#### 2. Open a powershell as administrator in that directory.
#### 3. Run the command:
 
            $ py pdfparse.py

#### 4. The result is placed in the output.csv file in the same directory.


