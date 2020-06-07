# AWS-EC2-analyzer
AWS Learning 
Demo project for EC2 managment

#configuration
ec2-analyzer uses AWS cli configred profile to connect to EC2 instances

To run this script aws configurtion is needed :
'aws configure --profile ec2-analyzer'
Script can be run with flags
 list
	'pipenv run python ec2-analyzer.py list' - to list all EC2 instances
 start
	'pipenv run python ec2-analyzer.py start' - to start all EC2 instances
 stop
	'pipenv run python ec2-analyzer.py stop' - to stop all EC2 instances
If script have to wokr on only specific EC2 instances with common Tag Project additional flag
--project=projecName can be used eg.
	'pipenv run python ec2-analyzer.py stop --project=SWA' - to stop all EC2 instances in SWA project
