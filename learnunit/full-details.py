"""
Whenever you have multiple API calls to do and parsing the data, writing the unittest
using mock is recommended.

If we write the function outside of class, it is difficult is call it inside mock tests. this is my understanding
"""


from unittest.mock import MagicMock

from actions import patch_nsx_ua_group
from actions.patch_nsx_ua_group import patchNsxUaGroup
from .testlib import generate_simple_response
from aflib.nodes.nsx_manager import NsxManager
from common.saas import vmc

# def test_get_ip_details0():
#     input = {
#         "expression" : [ {
#             "ip_addresses" : [ "10.3.192.4/32", "10.3.192.5/32", "10.3.192.6/32" ],
#             "resource_type" : "IPAddressExpression",
#             "id" : "d1cf92bd-d98a-44f3-9fa8-7a1844029332"
#         } ],
#         "extended_expression" : [ ],
#         "id" : "NSX-UA",
#         "tags" : [ {
#             "scope" : "",
#             "tag" : "SYSTEM_DEFINED_GROUP"
#         } ],
#         "path" : "/infra/domains/mgw/groups/NSX-UA",
#         "relative_path" : "NSX-UA",
#         "parent_path" : "/infra/domains/mgw",
#         "unique_id" : "434e8214-403b-4ce1-9005-25921423e7e6"
#     }
#     expected = {"ip_address": [ "10.3.192.4/32", "10.3.192.5/32", "10.3.192.6/32" ]}
#     rtn = patch_nsx_ua_group.getIpDetails(input)
#     assert rtn == expected
#
#
# def test_get_ip_details1():
#     input = {
#         "expression" : [],
#         "extended_expression" : [ ],
#         "id" : "NSX-UA",
#         "tags" : [ {
#             "scope" : "",
#             "tag" : "SYSTEM_DEFINED_GROUP"
#         } ],
#         "path" : "/infra/domains/mgw/groups/NSX-UA",
#         "relative_path" : "NSX-UA",
#         "parent_path" : "/infra/domains/mgw",
#         "unique_id" : "434e8214-403b-4ce1-9005-25921423e7e6"
#     }
#     expected = {"ip_address": []}
#     rtn = patch_nsx_ua_group.getIpDetails(input)
#     assert rtn == expected

"""In my script i have multiple API calls.
below is the output of one of the API call using vmc call_rest
"""
def mock_sddc_spec():
    return generate_simple_response(status=200, data={
        "nsxtSpecs": [
            {
                "controllerIpSpec": {
                    "managementIps": [
                        "172.30.192.4",
                        "172.30.192.5",
                        "172.30.192.6"
                    ]
                }
            }
        ]
    })

# This is the output of GET call when NSX UA group has all details

def mock_get_nsx_ua_details_correct(*args, **kwargs):
    return generate_simple_response(status=200, data={
        "expression" : [ {
            "ip_addresses" : ["172.30.192.6/32", "172.30.192.4/32", "172.30.192.5/32"],
            "resource_type" : "IPAddressExpression",
            "id" : "d1cf92bd-d98a-44f3-9fa8-7a1844029332",
            "path" : "/infra/domains/mgw/groups/NSX-UA/ip-address-expressions/d1cf92bd-d98a-44f3-9fa8-7a1844029332",
            "relative_path" : "d1cf92bd-d98a-44f3-9fa8-7a1844029332",
            "parent_path" : "/infra/domains/mgw/groups/NSX-UA",
            "marked_for_delete" : False,
            "overridden" : False,
            "_protection" : "NOT_PROTECTED"
        } ],
        "extended_expression" : [ ],
        "reference" : False,
        "resource_type" : "Group",
        "id" : "NSX-UA",
        "display_name" : "NSX-UA",
        "description" : "NSX-UA",
        "tags" : [ {
            "scope" : "",
            "tag" : "SYSTEM_DEFINED_GROUP"
        } ],
        "path" : "/infra/domains/mgw/groups/NSX-UA",
        "relative_path" : "NSX-UA",
        "parent_path" : "/infra/domains/mgw",
        "unique_id" : "434e8214-403b-4ce1-9005-25921423e7e6",
        "marked_for_delete" : False,
        "overridden" : False,
        "_protection" : "NOT_PROTECTED",
        "_create_time" : 1656925411619,
        "_create_user" : "admin",
        "_last_modified_time" : 1663317005375,
        "_last_modified_user" : "admin",
        "_system_owned" : False,
        "_revision" : 7
    })


# This is the output of GET call when NSX UA group don't have all MGR ip details


def mock_get_nsx_ua_details_incorrect():
    return generate_simple_response(status=200, data={
        "expression": [],
        "extended_expression": [],
        "reference": False,
        "resource_type": "Group",
        "id": "NSX-UA",
        "display_name": "NSX-UA",
        "description": "NSX-UA",
        "tags": [
            {
                "scope": "",
                "tag": "SYSTEM_DEFINED_GROUP"
            }
        ],
        "path": "/infra/domains/mgw/groups/NSX-UA",
        "relative_path": "NSX-UA",
        "parent_path": "/infra/domains/mgw",
        "unique_id": "e9a18602-9d67-43f0-88b0-fd1553ea4f52",
        "realization_id": "e9a18602-9d67-43f0-88b0-fd1553ea4f52",
        "owner_id": "694548ab-74cf-43b0-91d9-eb0fb462defd",
        "origin_site_id": "694548ab-74cf-43b0-91d9-eb0fb462defd",
        "marked_for_delete": False,
        "overridden": False,
        "_system_owned": False,
        "_create_time": 1662546656332,
        "_create_user": "admin",
        "_last_modified_time": 1662546656332,
        "_last_modified_user": "admin",
        "_protection": "NOT_PROTECTED",
        "_revision": 0
    })


def mock_manager_details():
    return generate_simple_response(status=200, data=["172.30.192.6/32", "172.30.192.4/32", "172.30.192.5/32"])

# Output after passing the mock_get_nsx_ua_details_correct data to getIpDetails function

def mock_getipaddress_output(*args, **kwargs):
    return generate_simple_response(status=200, data={
        "ip_address": ["172.30.192.6/32", "172.30.192.4/32", "172.30.192.5/32"]
    })

# Final output when the configuration is correct and remediation is not done.

def mock_correct_nsx_ua_group_output():
    return generate_simple_response(status=200, data={
        "ua_group_addresses": [
            "172.30.192.6/32",
            "172.30.192.4/32",
            "172.30.192.5/32"
        ],
        "remediation_required": "No patching required. All 3 NSX UA ip address are part of UA group."})

# Final output when the configuration is incorrect and remediation is done.

def mock_incorrect_nsx_ua_group_output():
    return generate_simple_response(status=200, data={
        "ua_group_addresses": [],
        "remediation_required": "Patching is required. Proceeding with PUT API call",
        "put_status": "PUT is completed",
        "verify_ua_group_ip": "After patching NSX UA address and Group Ip addresses are same",
        "after_patch_ua_ips": [
            "172.30.192.6/32",
            "172.30.192.4/32",
            "172.30.192.5/32"
        ]
    })


def test_correct_ua_group(monkeypatch):
    """
    Note: When there is no extra function inside the run apart from run function
    We can directly pass all the required inputs using mock and execute the unit test.

    When extra function is there we have to call that (line:213) also as part of the unit test
    When different API calls like one from NSX and other from VMC we have to mock both in the unittest
    lines 209, 211
    :param monkeypatch:
    :return:
    """
    # Below line, we are passing the correct UA group data and final output
    side_effects = [mock_get_nsx_ua_details_correct(), mock_correct_nsx_ua_group_output()]
    # Mock data for NSX API call
    mock_nsx_api = MagicMock(side_effects=side_effects)
    # assigning MOCK data for VMC API call
    mock_vmc_api = MagicMock(side_effects=[mock_sddc_spec()])
    # Executing the NSX API calls with all the mock details
    monkeypatch.setattr(NsxManager, 'call_rest', mock_nsx_api, raising=False)
    # Executing the VMC API calls with all the mock details
    monkeypatch.setattr(vmc, 'call_rest', mock_vmc_api, raising=False)
    # Because, there is a function inside the class, we have to run it with input and output data as side_effects
    monkeypatch.setattr(patchNsxUaGroup, "getIpDetails", MagicMock(side_effects=[mock_get_nsx_ua_details_correct(), mock_getipaddress_output()]))
    # This will execute the whole script with all the mock details
    action = patch_nsx_ua_group.patchNsxUaGroup()
    status, result = action.run(platform="local", sddc_id="mock")
    assert status is True
    print(result)