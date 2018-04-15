#爬虫
import re
#1.get html Text

#2 <span class="top_score">7315</span>
html='''<span class="top_score">7315</span>
        <span class="top_score">7316</span>
        <span class="top_score">73</span>
        <span class="top_score">715</span>
        <span class="top_score">15</span>"""
res=re.findall('<span class="top_score">(.+?)</span',html)
print(res)
