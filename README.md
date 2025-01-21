Run the command with python in local
========

prerequisite
1. AWS Credentials with permission to get data from the instance
2. already install python (recommedned at version 3.13.1 )

=========

How to run
1. clone to local
2. install boto3 library
3. Set AWS credentail (with enough permission to get data)
4. run the code with instanceid
   ```python fetch_metadata.py --instance-id i-007909b1102d53e3b > result.txt```
5. The result will return in json format in file name result.txt
