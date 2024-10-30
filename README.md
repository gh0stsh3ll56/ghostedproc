# ghostedproc
Process Monitor
Overview

This Python script monitors the execution of an .exe file and logs any new processes that are spawned while the .exe is running. It captures the Process ID (PID), process name, and command-line arguments of each new process and saves the details in a report file (process_report.txt).
Features

    Execute an .exe file and monitor processes started during its execution.
    Generate a detailed report of all new processes that are started while the main process runs.
    Capture and log process name, PID, and command line arguments.
    User-friendly console interface to specify the .exe file for monitoring.

Requirements

    Python 3.6 or later
    Cross-platform compatibility (Tested on Windows)

Usage

    Clone or download this repository to your local machine.

    Install the required dependencies using:

    bash

pip install -r requirements.txt

Run the script:

bash

    python monitor_process.py

    When prompted, enter the full path to the .exe file you want to monitor.

    The script will execute the .exe file and monitor for any new processes that are created during its runtime.

    Once the process terminates, a report (process_report.txt) will be generated in the same directory, containing details of the newly spawned processes.

Example

bash

python monitor_process.py
Enter the full path of the .exe file to execute: C:\path\to\application.exe

After running, the report will be saved as process_report.txt in the same directory.
Limitations

    The script will not track processes that start and exit very quickly unless the monitoring interval is adjusted.
    Only new processes that were started after the main .exe was launched will be recorded.

License

This project is licensed under the MIT License.
requirements.txt

psutil

This is a simple project with minimal external dependencies. The script relies on the psutil package for process management and monitoring.
