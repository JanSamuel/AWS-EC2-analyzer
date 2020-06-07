import boto3
import click
session = boto3.Session(profile_name='ec2-analyzer')
ec2 = session.resource('ec2')

def getInstances(project):
	instances = []
	if project:
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
	else:
		instances = ec2.instances.all()
	return instances


@click.group()
def instances():
	"Commands for instances"

@instances.command('start')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def stopEC2Instance(project):
	"Starts EC2"
	instances = getInstances(project)
	print(', '.join(('ID','Availability Zone','State','Public DNS', 'Project')))
	for i in instances:
		print("Starting {0} ...".format(i.id))
		i.start()

@instances.command('stop')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def stopEC2Instance(project):
	"Stops EC2"
	instances = getInstances(project)
	print(', '.join(('ID','Availability Zone','State','Public DNS', 'Project')))
	for i in instances:
		print("Stoping {0} ...".format(i.id))
		i.stop()
	
@instances.command('list')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def listInstances(project):
	"list EC2 instances"
	instances = getInstances(project)
	print(', '.join(('ID','Availability Zone','State','Public DNS', 'Project')))
	for i in instances:
		tags = {t['Key']: t['Value'] for t in i.tags or []}
		print(', '.join((i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name, tags.get('Project','<no project>'))))
	
if __name__=='__main__':
	instances()

	
