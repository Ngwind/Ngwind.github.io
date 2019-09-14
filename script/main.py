# -*- coding:utf-8 -*-
"""
用来一键创建md文件
"""
import time, shutil, os


def create_md_file(title):
    nt = time.time()
    format_t = time.strftime("%Y-%m-%d", time.localtime(nt))  # 时间前缀
    format_t_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(nt))
    file_name = format_t + "-" + title + ".md"  # 文件名
    
    with open("./template.md", "wb") as f:
        text = "---\nlayout: post\ntitle: "+ title + "\ndate: " + format_t_text + "\ncategories: \n  - pytest  \ntags: \n  - linux  \n---\n\n\n<!-- more -->\n\n## 111\n"
        f.write(text.encode('utf-8'))
    shutil.copy("./template.md", "../_posts/"+file_name)
    cmd = "start ../_posts/"+file_name
    os.system(cmd)


if __name__ =="__main__":
    title = str(input("输入文章主题："))
    create_md_file(title)
