# -*- coding: utf-8 -*-
# Copyright: (c) 2022, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function
from ..module_utils.utils import MaasValueMapper
from ..module_utils import errors


class NetworkInterface(MaasValueMapper):
    def __init__(
        # Add more values as needed.
        self,
        name=None,  # Interface name.
        id=None,
        subnet_cidr=None,
        machine_id=None,
        mac_address=None,
        vlan=None,
        mtu=None,
        tags=None,
    ):
        self.name = name
        self.id = id
        self.subnet_cidr = subnet_cidr
        self.machine_id = machine_id
        self.mac_address = mac_address
        self.vlan = vlan
        self.mtu = mtu
        self.tags = tags

    @classmethod
    def from_ansible(cls, network_interface_dict):
        obj = NetworkInterface()
        obj.name = network_interface_dict.get("name", None)
        obj.subnet_cidr = network_interface_dict.get("subnet_cidr", None)
        obj.mac_address = network_interface_dict.get("mac_address", None)
        obj.vlan = network_interface_dict.get("vlan", None)
        obj.mtu = network_interface_dict.get("mtu", None)
        obj.tags = network_interface_dict.get("tags", [])
        return obj

    @classmethod
    def from_maas(cls, maas_dict):
        obj = NetworkInterface()
        try:
            obj.name = maas_dict["name"]
            obj.id = maas_dict["id"]
            obj.subnet_cidr = maas_dict["links"][0]["subnet"]["cidr"]
            obj.machine_id = maas_dict["system_id"]
        except KeyError as e:
            raise errors.MissingValueMAAS(e)
        return obj

    def to_maas(self):
        to_maas_dict = {}
        if self.id:
            to_maas_dict["id"] = self.id
        if self.name:
            to_maas_dict["name"] = self.name
        if self.subnet_cidr:
            to_maas_dict["subnet_cidr"] = self.subnet_cidr
        return to_maas_dict

    def to_ansible(self):
        to_ansible_dict = {}
        if self.name:
            to_ansible_dict["name"] = self.name
        if self.subnet_cidr:
            to_ansible_dict["subnet_cidr"] = self.subnet_cidr
        return to_ansible_dict

    def needs_update(self, other_nic):
        return False

    def payload_for_update(self):
        return

    def send_update_request(self, payload):
        return

    def payload_for_create(self):
        return

    def send_create_request(self, payload):
        return
