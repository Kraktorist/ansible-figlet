## Ansible Collection - kraktorist.figlet

Figlet module. Ansible fodule for famous http://www.figlet.org/ program.

```
         ______ _____ _____ _      _     _
        |  ____|_   _/ ____| |    | |   (_)
        | |__    | || |  __| | ___| |_   _ ___    __ _
        |  __|   | || | |_ | |/ _ \ __| | / __|  / _` |
        | |     _| || |__| | |  __/ |_  | \__ \ | (_| |
        |_|    |_____\_____|_|\___|\__| |_|___/  \__,_|
                                                __
                                               / _|
   _ __  _ __ ___   __ _ _ __ __ _ _ __ ___   | |_ ___  _ __
  | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \  |  _/ _ \| '__|
  | |_) | | | (_) | (_| | | | (_| | | | | | | | || (_) | |
  | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_| |_| \___/|_|
  | |               __/ |
  |_|              |___/
                  _    _               _
                 | |  (_)             | |
  _ __ ___   __ _| | ___ _ __   __ _  | | __ _ _ __ __ _  ___
 | '_ ` _ \ / _` | |/ / | '_ \ / _` | | |/ _` | '__/ _` |/ _ \
 | | | | | | (_| |   <| | | | | (_| | | | (_| | | | (_| |  __/
 |_| |_| |_|\__,_|_|\_\_|_| |_|\__, | |_|\__,_|_|  \__, |\___|
                                __/ |               __/ |
                               |___/               |___/
   _      _   _                              _            __
  | |    | | | |                            | |          / _|
  | | ___| |_| |_ ___ _ __ ___    ___  _   _| |_    ___ | |_
  | |/ _ \ __| __/ _ \ '__/ __|  / _ \| | | | __|  / _ \|  _|
  | |  __/ |_| ||  __/ |  \__ \ | (_) | |_| | |_  | (_) | |
  |_|\___|\__|\__\___|_|  |___/  \___/ \__,_|\__|  \___/|_|
               _ _                          _            _
              | (_)                        | |          | |
  ___  _ __ __| |_ _ __   __ _ _ __ _   _  | |_ _____  _| |_
 / _ \| '__/ _` | | '_ \ / _` | '__| | | | | __/ _ \ \/ / __|
| (_) | | | (_| | | | | | (_| | |  | |_| | | ||  __/>  <| |_ _
 \___/|_|  \__,_|_|_| |_|\__,_|_|   \__, |  \__\___/_/\_\\__(_)
                                     __/ |
                                    |___/


```

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

### Examples

See [examples/testmod.yml](examples/testmod.yml) for another example