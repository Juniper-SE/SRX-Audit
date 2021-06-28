from nornir_pyez.plugins.tasks import pyez_sec_policy
from nornir import InitNornir

import os

script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yaml")

firewall = nr.filter(name="juniper-srx-garage0")

response = firewall.run(
    task=pyez_sec_policy
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)
