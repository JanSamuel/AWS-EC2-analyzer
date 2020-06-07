import boto3
import click
session = boto3.Session(profile_name='ec2-analyzer')
ec2 = session.resource('ec2')

@click.group()
def cli():
	"EC2 manager"

@cli.group('volumes')
def volumes():
	"Commands for volumes"

@cli.group('snapshot')
def snapshot():
	"Commands for volumes"

@snapshot.command('list')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def snapshotList(project):
	"list snapshots"
	instances = getInstances(project)
	for i in instances:
		for v in i.volumes.all():
			for snap in v.snapshots.all():
				print(', '.join((
					snap.id, snap.state, snap.progress)))
	return
	
@snapshot.command('create')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def creatSnapshot(project):
	"createing snapshot"
	instances = getInstances(project)
	for i in instances:
		for v in i.volumes.all():
			print("Createing snapshot of {0} ...".format(v.id))
			v.create_snapshot(Description="Created by EC2 analyzer")
	return


@volumes.command('list')
@click.option('--project', default=None, help="only instances for project (tag Project:<name>)")
def volumesList(project):
	"list volumes"
	instances = getInstances(project)
	for i in instances:
		print("EC2 instance {0} has volumes:".format(i.id))
		for v in i.volumes.all():
			tags = {t['Key']: t['Value'] for t in v.tags or []}
			print('  '+', '.join((
				v.id, v.state, str(v.size) + 'GiB', v.encrypted and "Encrypted" or "Not Encrypted")))
	return


@cli.group('instances')
def instances():
	"Commands for instances"

def getInstances(project):
	instances = []
	if project:
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
	else:
		instances = ec2.instances.all()
	return instances

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
		print(', '.join((
			i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name, tags.get('Project','<no project>'))))
	
if __name__=='__main__':
	cli()

	
