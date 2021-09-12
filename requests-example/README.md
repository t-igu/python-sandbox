## requests-example

How to use redmine api with python(do not use python-redmine).

### requirements

```
requests==2.26.0
loguru==0.5.3
```

### install 

```
pip install requests loguru
```

### file structure

```
└── requests-example
    ├── main.py
    └── settings.py
```

### settings.py

```
REDMINE_URL="http://127.0.0.1/redmine"
REDMINE_KEY="<api key>"
REDMINE_USER="remine-user"
REDMINE_PASS="redmine-pass"
```

### Some major features

get issues, users, trackers, statuses, projects, etc

|Resource           |url                                    |method|params(example)                        |
|:------------------|:--------------------------------------|:-----|:--------------------------------------|
|Issue Statuses     |/issue_statuses.json                   |get   ||
|Trackers           |/trackers.json                         |get   ||
|Users              |/users.json                            |get   || 
|User               |/users/[user_id].json                  |get   |include=memberships,groups             | 
|Projects           |/projects.json                         |get   ||
|Project            |/projects/[project_id].json            |get   |include=trackers,issue_categories      |
|Project Memberships|/projects/[project_id]/memberships.json|get   ||
|Issues             |/issues.json                           |get   |limit=0&offset=100&project_id=1&sort=id|
|Issue              |/issues/[issue_id].json                |get   |include=attachments,journals           |

### Referenced site

[Redmine API](https://www.redmine.org/projects/redmine/wiki/Rest_api)