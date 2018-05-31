# aws-boto3-scripts
Python scripts for AWS using boto3 SDK

| Script        			 | Description  									   |
| ---------------------------| ----------------------------------------------------|
| [ec2_start.py](scripts/ec2_start.py)	             | Start all instances with a specific tag             |
| [ec2_stop.py](scripts/ec2_stop.py)	             | Stop all instances with a specific tag              |
| [ec2_ip_route53.py](scripts/ec2_ip_route53.py)     | Find EC2 public IP and change Route53 'A' record    |

## Installation

Requires Python and [boto3](https://github.com/boto/boto3).

```
git clone https://github.com/dmitrijsf/aws-boto3-scripts
cd aws-boto3-scripts
pip install -r requirements.txt
```
## Usage

**Set desired AWS credentials**

In this example I am using [**aws-vault**](https://github.com/99designs/aws-vault) to work with desired profile.

```
❯ aws-vault add home
Enter Access Key ID: your-aws-access-key-id
Enter Secret Access Key: your-aws-access-key
Added credentials to profile "home" in vault

# launches subshell with desired AWS environment variables
❯ aws-vault exec -- home
```
**Launching Scripts**

```
❯ cd scripts
# modify the script according to your needs
# ec2_ip_route53.py

# set instance ID
instance_id = 'i-0111112233' # Instance ID, e.g. 'i-0111112233'
# set Hosted Zone ID
zone_id = 'ZBDAAABBBCCC' # Hosted Zone ID, e.g. 'ZBDAAABBBCCC'
# domain
domain = 'technoff.eu' # Domain, e.g. technoff.eu

❯ python ec2_ip_route53.py
technoff.eu record was changed to: 52.51.120.202
```