from cerberus import Validator
"""
        action_block :: sample ::
        - name: manipulate_inventory
          type: shell
          path: /tmp/shellscripts
          actions:
            - thisisshell.sh
"""
schema= { 
        'name': {'type': 'string', 'required': True },
        'type': { 'type': 'string', 'allowed': ['shell', 'subprocess']},
        'path': {'type': 'string', 'required': False},
        'actions': { 'type': 'list', 'schema': {'type': 'string'}, 'required': True}
        
        }
v = Validator(schema)
doc1 = {
        'name': 'manuplate_inven',
        'type': 'shell',
        'path': '/tmp/sompath',
        'actions': [
            'thisisshell.sh',
            'echo "helloworld" "hello too"',
            ]
        
        }
doc2 = {
        'name': 'manuplate_inven',
        'type': 'shellidd',
        'path': '/tmp/sompath',
        'actions': [
            'thisisshell.sh',
            {}
            ]
        }
print(v.validate(doc1))
print(v.errors)
print(v.validate(doc2))
print(v.errors)

"""
ansible schema hook schema: 

- name: build_openshift_cluster
  type: ansible
  actions:
    - playbook: test_playbook.yaml
      vars: test_var.yaml
      extra_vars: { "testvar": "world"}
"""
print("### Ansible schema ###")
schema= {
        'name': {'type': 'string', 'required': True },
        'type': { 'type': 'string', 'allowed': ['ansible']},
        'path': {'type': 'string', 'required': False},
        'actions': { 'type': 'list', 
                     'schema': {
                         'type': 'dict',
                         'schema': {
                             'playbook': {'type': 'string', 'required': True},
                             'vars': {'type': 'string', 'required': False},
                             'extra_vars': {'type': 'dict', 'required': False}
                         }
                     },
                     'required': True
                   }
        }
doc1 = {
        'name': 'build_openshift_cluster',
        'type': 'ansible',
        'actions': [
              { 
                'playbook': 'test',
        #        'vars': 'test',
        #        'extra_vars': {}
              },
              {
                'playbook': 'test',
        #        'vars': 'test',
                'extra_vars': {
                    '1': '2',
                    '2': '3'
                     }
              }
            ]
        
        }
v = Validator(schema)
print(v.validate(doc1))
print(v.errors)
