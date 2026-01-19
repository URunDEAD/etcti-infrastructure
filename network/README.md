# Network - Netbird Overlay

Netbird dashboard: https://netbird.urundead.win/

## Conventions

### Host naming patterns

{location}-{type}-{function}-{number}

#### Locations:
- upt_b226 (UPT, room b226b)
- upt_roedu (UPT, roedu )
- sptjud_150 (Spitalul Judenetean, room 150)
- usr_{netbird_username} (User mobile device like a phone, laptop)

#### Types:
- srv (Physical/virtual server)
- k8s (Kubernetes node)
- gw (Gateway/router)

If **location** is **usr**:
- lap (Laptop)
- mob (Mobile phone)
- pc (Personal Computer)
- oth (other)

#### Function:
- db (Database)
- web (Serving Web)
- pve (Proxmox Hypervisor)

If **type** is **k8s** or **pve**
- master
- worker

If **location** is **usr**:
- acs (Access)

#### Number:
An number to help differenciate between multiple resources that share the same propreties listed above (HA with more masters for example).

#### Examples:
- upt_b226a-srv-web-1 - UPT B226, Server, Web, #1
- upt_b126-srv-db-1 - UPT B126, Server, Database, #1
- upt_b226b-k8s-master-1 - UPT B226, K8s, Master node, #1
- lon-srv-app-2 - London, Server, Application, #2
- usr_paul_schuldesz-mobile-acs-1

### Groups naming patterns

#### Peers Groups:

Examples:
- nyc-servers - All NYC servers
- lax-servers - All LAX servers
- k8s-cluster - All K8s nodes regardless of location
- web-team - Web team user devices
- db-admins - Database admin devices
- all-servers - All servers across locations

#### Teams groups:

team-{team_name}

Examples
- team-datalab
- team-artificial_vision