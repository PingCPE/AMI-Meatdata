Run the command with python in local
========

prerequisite
1. AWS Credentials with permission to get data from the instance
2. Already install python (recommedned at version 3.13.1 )

=========

How to run (on zsh terminal)
1. Clone to local
2. (Optional) Source env for call python
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
   
4. Set AWS credentail (with enough permission to get data)
5. Run the code with instanceid
   ```bash
   python fetch_metadata.py --instance-id i-007909b1102d53e3b > result.txt
   ```
6. The result will return in json format in file name result.txt
