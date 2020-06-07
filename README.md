# AWS-EC2-analyzer
AWS Learning 
Demo project for EC2 managment

#configuration
ec2-analyzer uses AWS cli configred profile to connect to EC2 instances

To run this script aws configurtion is needed :
'aws configure --profile ec2-analyzer'
Script can be run with flags
instances - for acess to EC2 servers
volumes  - for acces to volumes
snapshot - to creat and list snapshots
additional flags are:
 list eg.
	'pipenv run python ec2-analyzer.py volumes list' - to list all EC2 instances
 start eg.
	'pipenv run python ec2-analyzer.py instances start' - to start all EC2 instances
 stop
	'pipenv run python ec2-analyzer.py instances stop' - to stop all EC2 instances
Full info can be found in :
'pipenv run python ec2-analyzer.py --help'

If script have to wokr on only specific EC2 instances with common Tag Project additional flag
--project=projecName can be used eg.
	'pipenv run python ec2-analyzer.py stop --project=SWA' - to stop all EC2 instances in SWA project
