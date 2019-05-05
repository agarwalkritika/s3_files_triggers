## Overview

Introduction of server less programming opens a wide range of possibilities for multiple functionalities. One such functionality is analysis and processing of files uploaded to S3 bucket, as soon as they are uploaded, and that too without maintaining any servers.

## Usage
### Installing dependencies
#### Python dependencies
This plugin uses the boto3 python package. You can install that using
```sh
pip install boto3
``` 
#### Permissions
The plugin assumes that the machine you are running it on, either has roles for required permissions or has credentials with required permission (discussed separately).

Credentials can be configured using command line
```sh
aws configure
``` 

(Or you can run this on an EC2 instance with required role)
### Execution
 1. Clone the repository or download the zip.
 2. cd to the unzipped folder.
 3. Run the command line ```python main.py```
 
 The program shall prompt for the bucket name on which you want to install the plugin.
 
 Provide the correct bucket name.