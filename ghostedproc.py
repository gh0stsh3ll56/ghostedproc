import psutil
import subprocess
import time
import os

# Function to get a list of current running processes with details
def get_processes():
    return {p.pid: p.info for p in psutil.process_iter(['pid', 'name', 'cmdline'])}

# Generate a detailed report of the new processes
def generate_report(started_processes, exe_path):
    report = f"Report for processes started by: {exe_path}\n"
    report += "="*50 + "\n"
    
    if started_processes:
        for pid, info in started_processes.items():
            report += f"PID: {pid}\n"
            report += f"Process Name: {info['name']}\n"
            report += f"Command Line: {' '.join(info['cmdline']) if info['cmdline'] else 'N/A'}\n"
            report += "-"*50 + "\n"
    else:
        report += "No new processes were started.\n"
    
    # Save the report to a file
    with open("process_report.txt", "w") as f:
        f.write(report)
    print("Report saved to 'process_report.txt'.")
    
# Execute the .exe file and monitor for any new processes
def monitor_process(exe_path):
    # Check if the provided path is valid
    if not os.path.exists(exe_path):
        print(f"Error: {exe_path} does not exist.")
        return

    # Get initial processes
    initial_processes = get_processes()

    # Start the .exe program
    print(f"Starting {exe_path}")
    process = subprocess.Popen(exe_path, shell=True)

    started_processes = {}

    # Continuously monitor processes until the main application closes
    try:
        while process.poll() is None:  # poll() returns None while the process is running
            time.sleep(2)  # Adjust the sleep interval as needed
            current_processes = get_processes()

            # Capture newly started processes since the last check
            for pid, info in current_processes.items():
                if pid not in initial_processes and pid not in started_processes:
                    started_processes[pid] = info

            # Keep the initial process list updated as new processes appear
            initial_processes = current_processes

    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user.")

    # Once the .exe process exits, generate the report
    generate_report(started_processes, exe_path)

if __name__ == "__main__":
    exe_path = input("Enter the full path of the .exe file to execute: ").strip()
    monitor_process(exe_path)
