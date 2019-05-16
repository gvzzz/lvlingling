#自动创建wiki分两步走，首先生成wiki的唯一的编号 需要get接口获取到response中的html爬取唯一标写入wiki

import failCrawling
import utils.httpUtil
def writewiki(spacekey,parentPageName):
    parent_Id = failCrawling.getPageId(parentPageName)
    dict_wiki = failCrawling.getcreate_wikiIDict(spacekey, parent_Id)
    wiki_key = dict_wiki.get('create_wikiId')  #拿到要新增的wiki的key
    wiki_token = dict_wiki.get('create_wikiToken')  #拿到要新增的wiki的token
    print(wiki_key)
    headers = {}
    url = "http://wiki.ymmoa.com/pages/docreatepage.action"
    print(url)
    headers["Cookie"] = 'seraph.confluence=22609947%3A35e0c34e43e1c3a0ce89c545a4e456759f1625e4; mywork.tab.tasks=false; dev_passport=MeryZDWB_K7OEFZpcKxSyk4OLiOV32Bgy4lXMRvu9VzTNX1zoRqQMsXYItDvSvDlBe_S6j4ufz1MMTdS-p2QFw7r67Q-4iyNMjCWJhnAICAXZJw77II_r_uEqQ29v9sVZkzS8Omv_nie3vh4jLbaie3eIXJe1eIE73TewYy9uHQ; __utmc=1; __utmz=1.1556002706.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); confluence-sidebar.width=325; qa_passport=JW165mHVLrM9r6onbocjaaGIMgxpgKXaTjuDiUP0Ys7lr99dxg_OwlLZjmE3xg1IL8AKqWKF8SPZ8Vyoo-dDb-Peq4A0itmJOFTBj7hoBf7qTWhxvEPMdX6Ciz51DsYqTdWOX1B6uhCLyuqAihRS9immRp1sfXR6JjhAMSWvtlY; ymmoa_passport=XzxRDXTq9u-wyjwqyXhqDDLoRdcfi_ETX_grvBfWmR4lFOHSrbagK0Q05JyPbVagvkwjtQtk8z5OkC0QMAYyP-5CI5oF9-37_m0_2701vwtHZGEink3I8D4Q_6mAX5V6zd9SbV6NEAn3tybw-A3K0tBOMNJSSlgucvH4jFdewYo; ymmoa_user={%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E5%9F%BA%E7%A1%80%E5%B9%B3%E5%8F%B0%E6%B5%8B%E8%AF%95%E9%83%A8%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}; JSESSIONID=6BC38FCD33DFD9DB1A61B6A87D533F67; __utma=1.1502096573.1556002706.1556171489.1556257694.4'
    headers["Content-Type"] = 'application/x-www-form-urlencoded; charset=UTF-8'

    dict ={}
    dict['atl_token'] = wiki_token
    dict['queryString'] = 'spaceKey='+ spacekey + '&amp;fromPageId='+parent_Id
    dict['fromPageId'] = parent_Id
    dict['spaceKey'] = spacekey
    dict['titleWritten'] = 'false'
    dict['linkCreation'] = 'false'
    dict['originalReferrer'] = 'http://wiki.ymmoa.com/pages/viewpage.action?pageId='+ parent_Id
    dict['title'] = 88888666666
    dict['confirm'] = 'Save'
    dict['parentPageString'] = parentPageName
    dict['moveHierarchy'] = 'true'
    dict['draftId'] = wiki_key
    dict['entityId'] = wiki_key
    dict['newSpaceKey'] = spacekey
    dict['labelsString'] = None
    dict['position'] = None
    dict['targetId'] = None
    dict['draftShareId'] = None
    print(dict)
    #response = utils.httpUtil.PostForm(url, headers, dict)







if __name__ == '__main__':
    writewiki('rdTeam','201904-201906测试设计')