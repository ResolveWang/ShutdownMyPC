import json
import re
from bs4 import BeautifulSoup
from datetime import datetime


def get_newest(session, uid):
    url = 'http://weibo.com/' + uid + '/profile?profile_ftype=1&is_ori=1#_0'
    page = session.get(url).text

    soup = BeautifulSoup(page, 'html.parser')
    scripts = soup.find_all('script')
    status = ''
    for s in scripts:
        if 'pl.content.homeFeed.index' in s.string:
            status = s.string

    pattern = re.compile(r'FM.view\((.*)\)')
    rs = pattern.search(status)

    if rs:
        cur_status = rs.group(1)
        html = json.loads(cur_status).get('html')
        soup = BeautifulSoup(html, 'html.parser')
        newest = soup.find(attrs={'action-type': 'feed_list_item'})
        post_cont = newest.find(attrs={'node-type': 'feed_list_content'}).text.strip()
        post_stamp = int(newest.find(attrs={'node-type': 'feed_list_item_date'}).get('date')[:-3])
        post_time = datetime.fromtimestamp(post_stamp)
        now = datetime.now()
        t = (now - post_time).total_seconds()
        return post_cont, t
    else:
        return None    