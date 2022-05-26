#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: figlet

short_description: Transform a string to ASCII image

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is a clone of the famous program for Ansible.

options:
    name:
        description: This is the string for transforming.
        required: true
        type: str
    font:
        description:
            - Figlet ASCII Font to transform
        required: false
        type: str
    width:
        description:
            - max width of page to display
        required: false
        type: int
    direction:
        description:
            - Text direction ('auto', 0 or 1)
            - 0 for left-to-right
            - 1 for right-to-left
        required: false
        type: str
    justify:
        description:
            - Text alignment ('auto', 'center', 'left', 'right')
        required: false
        type: str

author:
    - Kraktorist (@kraktorist)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  kraktorist.figlet.figlet:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  kraktorist.figlet.figlet:
    name: hello world
    font: standard

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: The output message that the module generates.
    type: str
    returned: always
    sample: |
    
      (Lorem Ipsum with hashtags)

      
      ###                               ###
       #                                 #
       #                                 #
       #      ##  ## #  ##  # ## ##      #  # ##   ### #  #  # ## ##
       #     #  #  ##  #  #  #  #  #     #   #  # #    #  #   #  #  #
       #   # #  #  #   ####  #  #  #     #   #  #  ##  #  #   #  #  #
       #   # #  #  #   #     #  #  #     #   #  #    # #  #   #  #  #
      ######  ##  ###   ### ### ## ##   ###  ###  ###   ## # ### ## ##
                                             #
                                            ###
'''

from ansible.module_utils.basic import AnsibleModule

import traceback

try:
    from pyfiglet import Figlet
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        font=dict(type='str', required=False, default='standard'),
        width=dict(type='int', required=False, default=80),
        direction=dict(type='raw', required=False, default='auto'),
        justify=dict(type='str', required=False, default='auto'),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if not HAS_ANOTHER_LIBRARY:
        # Needs: from ansible.module_utils.basic import missing_required_lib
        module.fail_json(
            msg=missing_required_lib('another_library'),
            exception=ANOTHER_LIBRARY_IMPORT_ERROR)

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    f = Figlet(
        font=module.params['font'],
        width=module.params['width'],
        direction=module.params['direction'],
        justify=module.params['justify']
    )
    result['message'] = f.renderText(module.params['name'])
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()