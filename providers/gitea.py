# coding:utf8
import requests
import json
from .instance import Instance


class GiteaInstance(Instance):
    prefix = 'api/v1'

    def create(self, gogs_token, clone_addr, repo_name, repo_owner, description):
        data = {
            "auth_token": gogs_token,
            "clone_addr": clone_addr,
            "description": description,
            "private": "on",
            "repo_name": repo_name,
            "repo_owner": repo_owner,
            "service": "5",
        }
        # print(data)
        r = requests.post(
            self.api_url+"/repos/migrate?access_token="+self.token,
            data=data,
            verify=False
        )
        return json.loads(r.text)
