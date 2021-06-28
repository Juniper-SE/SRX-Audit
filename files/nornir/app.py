from nornir_pyez.plugins.tasks import pyez_rpc
from nornir import InitNornir
from rich import print

import os

script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yaml")

firewall = nr.filter(name="juniper-srx-garage0")

extras = {
    "less-than": "1"
}

response = firewall.run(
    task=pyez_rpc, func='get-security-policies-hit-count', extras=extras
)

for dev in response:
    print(response[dev].result)
