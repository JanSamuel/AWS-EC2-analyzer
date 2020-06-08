from setuptools import setup

setup(
    name="EC2-analyzer",
    version="0.1",
    author="Jan Owczarek",
    author_email="",
    description="test program for AWS learning",
    license="GPLv3+",
    packages=['ec2_analyzer'],
    url=[''],
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points = '''
        [console_scripts]
        ec2-analyzer=ec2_analyzer.ec2_analyzer:cli
    '''
)
