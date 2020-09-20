# Convert602 - PDF and DOCX converter itnto T602 document format #

## T602 ##
T602 is a obsolete document editor written for MS-DOS. It was produced by czech company Software-602. Back in the days when PCs started to be popular in the Czech Republic, it was really popular editor with loads of clever features. For some people it was the firs editor they had ever used. But as the time was passing, this software almost completely vanished. But there are still people who use it nowadays. And for these people it is very often critical to get text from "modern" file formats such are PDF and DOCX into T602. This app should help them with that.

## Running T602 ##
Nowadays, T602 can be run only in DOSBox virtualisation software.

## Features ##
- **DOCX document conversion into .602 files for T602 editor**
- **PDF document conversion into .602 files for T602 editor**
- **Segmentation of converted text into multiple T602 documents** - this is critical feature mailnly for long PDF texts (scientific publications etc.) which can be longer than 100 pages. T602, as it was written many years ago is not able to open large .602 files, so this feature had to be introduced.
- **Multi language support** - the app is translated into Czech language and English
- **Direct opening of converted documents** - when the user specifies path to DOSBox and path to directory which is mounted as virtual disk in DOSBox, app is able to open converted documents stored into virtual disk directly in T602 - app opens DOSBox and opens the document in T602 by typing in the command(s)
- **Configuration storage** - app remembers its configuration (it creates *ini* file in AppData, where the configuration is stored)
- **Adjusting parameters of T602 (.602) files** - like tom margin, bottom margin etc.

# Running the app #

## Prerequisities ##
- Python 3.8.3 or newer
- Libraries:
    - python-docx
    
            pip install python-docx


    - pdfminer.six 

            pip install pdfminer.six

    - pyautogui

            pip install pyautogui

    - tkinter - default Python module, no need to install manually

### DOSBox autoexec in dosbox.conf ###
For correct behavior of dosbox-opening part of the app, following things have to be put in autoexec of DOSBox (in autoexec part of dosbox.conf)
- Instruction to mount your prefered directory as a disk (this directory has to be then configured also in this app) For example, i have my DOS directory on disk C:

        MOUNT C C:\DOS

- Add paths to M602 and T602 into PATH variable inside DOSBox. For example T602 and M602 installed in C:\DOS\T602 and C:\DOS\M602:

        PATH=C:\;C:\M602;C:\T602

- Instruction to navigate to C inside DOSBox:

        C:

- Keyboard configuration:

        KEYB us 437

- Instruction to run M602 file explorer

        M602

So for example, autoexec part of dosbox.conf file can look like this:

    [autoexec]
    # Lines in this section will be run at startup.
    # You can put your MOUNT lines here.
    MOUNT C C:\DOS
    PATH=C:\;C:\M602;C:\T602
    C:
    KEYB us 437
    M602

### Running platform ###
The app was developed on Windows and it is optimized for operation under Windows operating system. It is runable on Linux, however, correct behavior of some parts cannot be granted.
Development was done on Windows 10

## Running the app ##
- Clone this repository
- Navigate to folder of the repository
- Run the app.py with python interpretter

        python src/app.py