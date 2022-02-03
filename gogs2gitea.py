#coding: utf8
import urllib3
urllib3.disable_warnings()
from providers.gitea import GiteaInstance
from providers.gogs import GogsInstance

gogs_token = 'xxxxxxxx'
gogs_addr = 'http://gogs.server:3000/'
gitea_token = 'xxxxxxxx'
gitea_addr = 'https://gitea.server:3000/'
gogs = GogsInstance(gogs_addr, gogs_token)
gitea = GiteaInstance(gitea_addr, gitea_token)


def migrate_repos(gogs, gitea):
    gogs_repo_list = gogs.list_repos()

    for item in gogs_repo_list:
        clone_addr = gogs_addr+item["full_name"]
        repo_name = item["name"]
        repo_owner = item['full_name'].split('/')[0]
        description = item["description"]
        try:
            resp = gitea.create(gogs_token,clone_addr,repo_name,repo_owner,description)
            if "The repository with the same name already exists." not in resp["message"]:
                print(clone_addr)
        except Exception as e:
            print(e)
            print("[ERROR]: "+clone_addr)


migrate_repos(gogs, gitea)