## Ansible Collection - kraktorist.figlet

Figlet module. Ansible fodule for famous http://www.figlet.org/ program.

>FIGlet is a program for making large letters out of ordinary text (C).

### Dependencies

```
pip install pyfiglet
```

https://github.com/pwaller/pyfiglet

### Installation

```yaml
# requirements.yaml

collections:
  - name: https://github.com/Kraktorist/ansible-figlet.git
    type: git
    version: master
```

```console
ansible-galaxy install -r requirements.yml
```

### Usage

```yaml
- name: transform the text
  kraktorist.figlet.figlet:
    name: 'Lorem Ipsum'
    font: "lean"
    width: 120
    direction: 1
    justify: left
  register: testout
- name: dump the text
  debug:
    msg: '{{ testout }}'
```

### Output

```
ok: [localhost] => 
  msg:
    changed: true
    failed: false
    message: |2-
  
          _/                                                          _/_/_/
         _/          _/_/    _/  _/_/    _/_/    _/_/_/  _/_/          _/    _/_/_/      _/_/_/  _/    _/  _/_/_/  _/_/
        _/        _/    _/  _/_/      _/_/_/_/  _/    _/    _/        _/    _/    _/  _/_/      _/    _/  _/    _/    _/
       _/        _/    _/  _/        _/        _/    _/    _/        _/    _/    _/      _/_/  _/    _/  _/    _/    _/
      _/_/_/_/    _/_/    _/          _/_/_/  _/    _/    _/      _/_/_/  _/_/_/    _/_/_/      _/_/_/  _/    _/    _/

```