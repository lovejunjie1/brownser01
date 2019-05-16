# -*- coding: utf-8 -*-
#shotgun.guild.py
import os

if True:
    #api的安装命令
    installCmd = 'pip install git+git://github.com/shotgunsoftware/python-api.git@v3.0.26'
    #os.system(installCmd)

    # 最高版本的多多少少还是有些问题，用固定版本的就可以了

    #登录:
    import shotgun_api3
    #这是用户登录方式
    sg = shotgun_api3.Shotgun("https://rinfigo.shotgunstudio.com",login="lovejunjie1",password="WFshotgun!23")
    #最好还是使用脚本登录方式，为每个脚本分配不同的钥匙，方便排错
    #http://developer.shotgunsoftware.com/python-api/authentication.html

    #验证用户真实性：
    sg.authenticate_human_user("lovejunjie1", "WFshotgun!23", None)
    #{'login': 'lovejunjie1', 'type': 'HumanUser', 'id': 88}  返回值


    data = {
    "project": {"type": "Project", "id": 89},
    "sg_sequence": {"type": "Sequence", "id": 41},
    "code": "001_200",
    'sg_status_list': "ip"
    }

    #sg.create('Shot', data)
    # 添加镜头信息，shot，需要已知project的ID和sequence的ID，code指的是名字，sg_status是状态，进行中什么的



fields = ['id', 'code']
sequence_id = 41
project_id = 89
filters = [
['project', 'is', {'type': 'Project', 'id': project_id}],
['id','is',1173]

]
assets= sg.find("Shot",filters,fields)
print assets
'''
,
['shot', 'is', {'type': 'Shot', 'id': 1173}],
['sequences', 'is', {'type': 'Sequence', 'id': sequence_id}]
'''


