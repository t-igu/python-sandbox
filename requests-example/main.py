import requests
import pprint
import json
import base64

from loguru import logger

from settings import REDMINE_KEY,REDMINE_URL,REDMINE_USER,REDMINE_PASS

def show_data(data):
    logger.info(data)

def get_request_headers(basicAuth=False):
    # Basic認証用の文字列を作成.
    encode_user_and_pasword = base64.b64encode(f'{REDMINE_USER}:{REDMINE_PASS}'.encode('utf-8'))
    decode_user_and_pasword = encode_user_and_pasword.decode('utf-8')
    headers={
        'X-Redmine-API-Key': REDMINE_KEY,
        'content-type': "Application/json",        
    }
    if basicAuth:
        headers.update({'Authorization': f"Basic {decode_user_and_pasword}"})
    return headers

def get_data(url, key):
    headers = get_request_headers()
    response = requests.get(url, headers=headers)
    if (response.status_code==200):
        try:
            data = json.loads(response.text)
            print(type(data[key]), data[key])
            return True, data[key]
        except Exception as e:
            return False, response.text
            
    return None
# issue_statuses

def get_issue_statuses():
    logger.info("--issue_statuses example--")
    url=f'{REDMINE_URL}/issue_statuses.json'
    status, data = get_data(url, 'issue_statuses')
    if (status):
        [show_data(issue) for issue in data if data]
    else:
        logger.info(data)

def get_trackers():
    logger.info("--trackers example--")
    url=f'{REDMINE_URL}/trackers.json'
    _, data = get_data(url, 'trackers')
    [show_data(issue) for issue in data if data]

def get_users():
    logger.info("--users example--")
    url=f'{REDMINE_URL}/users.json'
    _, data = get_data(url, 'users')
    [show_data(issue) for issue in data if data]

def get_projects():
    logger.info("--projects example--")
    url=f'{REDMINE_URL}/projects.json'
    _, data = get_data(url, 'projects')
    [get_project(item['id']) for item in data if data]

def get_project(id):
    logger.info("--project example--")
    url=f'{REDMINE_URL}/projects/{id}.json?include=trackers,issue_categories'
    _, data = get_data(url, 'project')
    show_data(data)
    get_memberships(id)

def get_memberships(id):
    logger.info("--memberships example--")
    url = f'{REDMINE_URL}/projects/{id}/memberships.json'
    _, data = get_data(url, 'memberships')
    [show_data(issue) for issue in data if data]

def get_issues(priject_name, params):
    logger.info("--issues example--")
    offset = 0
    limit = 100
    reccnt = 100
    headers = get_request_headers()
    issues = []

    url = f'{REDMINE_URL}/projects/{priject_name}/issues.json?'
    params_arr = [f"{key}={value}" for key, value in params.items()]
    url = url + '&'.join(params_arr)

    while reccnt >=limit:
        response = requests.get(url + f"&limit={limit}&offset={offset}", headers=headers)
        data = json.loads(response.text)
        wissues = data['issues']
        issues.extend(wissues)
        reccnt = len(wissues)
        offset+=limit

    logger.debug(f"issue count={len(issues)}")
    [get_issue(issue['id'], params={"include":"attachments,journals,children"}) for issue in issues if issues]

def get_issue(id, params={}):
    logger.info("--issues example--")
    url = f'{REDMINE_URL}/issues/{id}.json?'
    params_arr=[f"{key}={value}" for key, value in params.items()]
    url = url + '&'.join(params_arr)
    logger.debug(url)
    _, text = get_data(url, 'issues')
    issue = json.loads(text)
    show_data(issue)
    # delete_issue(issue['issue']['id'])


def create_user(payload):
    url=f'{REDMINE_URL}/users.json'
    headers = get_request_headers(basicAuth=True)
    response=requests.post(url, headers=headers, data=json.dumps(payload))
    jsonresp = json.loads(response.text)
    logger.info(jsonresp)
    return jsonresp

def create_issue(payload):
    url=f'{REDMINE_URL}/issues.json'
    headers = get_request_headers(basicAuth=True)
    response=requests.post(url, headers=headers, data=json.dumps(payload))
    jsonresp = json.loads(response.text)
    issue = jsonresp['issue']
    id = issue['id']
    logger.info(f'Issue(id={id}) was created.')
    return issue

def update_issue(id, payload):
    # for i in range(10):    
        url=f'{REDMINE_URL}/issues/{id}.json'
        headers = get_request_headers(basicAuth=True)
        # logger.info(headers)
        response=requests.put(url, headers=headers, data=json.dumps(payload))
        if (response.status_code==200):
            logger.info(f'Issue(id={id}) was updated.')
            return True
        else:
            return False

def delete_issue(id):
    url=f'{REDMINE_URL}/issues/{id}.json'
    headers = get_request_headers(basicAuth=True)
    response=requests.delete(url, headers=headers)
    if (response.status_code==200):
        logger.info(f'Issue(id={id}) was deleted.')
        return True
    else:
        return False

def setup():
    logger.add("app.log")

def main():
    setup()
    logger.info("--- get projects ---")
    get_projects()
    logger.info("--- get issues ---")
    params = {"project_id": 1,"status_id":"*", "sort":"id:asc"}
    get_issues('project-a', params=params)

    logger.info("--- get users ---")
    get_users()

    logger.info("--- create users ---")

    for i in range(10):
        # user (required): a hash of the user attributes, including:
        # login (required): the user login
        # password: the user password
        # firstname (required)
        # lastname (required)
        # mail (required)
        # auth_source_id: authentication mode id
        # mail_notification: only_my_events, none, etc.
        # must_change_passwd: true or false
        # generate_password: true or false    
        user={
            "user":{
                "login": f"testuser{i+1}",
                "password": "pass_testuser",
                "firstname": f"firstname{i+1}",
                "lastname": f"lastname{i+1}",
                "mail": f"firstname{i+1}@example.com",
            }
        }
        # create_user(user)

    logger.info("--- get trackers ---")
    get_trackers()

    logger.info("--- get statuses ---")
    get_issue_statuses()

    for i in range(110):
        payload = {
            "issue": {
                'project_id':1,
                'tracker_id':1,
                'status_id':1,
                'priority_id':1,
                'subject':f'テスト{i}',
                'description':f'テスト作成{i}',
            }
        }
        # issue=create_issue(payload)
        # payload = {
        #     "issue": {
        #         "subject": f"テスト{issue['id']}",
        #         "notes": f"The subject was changed({issue['id']})",
        #     }
        # }
        # update_issue(issue['id'], payload)
        # delete_issue(issue['id'])
if __name__=="__main__":
    main()