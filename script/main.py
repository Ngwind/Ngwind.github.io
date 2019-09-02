# coding: utf-8

"""
用来一键创建md文件
"""
import time, shutil


def create_md_file(title):
    nt = time.time()
    format_t = time.strftime("%Y-%m-%d", time.localtime(nt))  # 时间前缀
    format_t_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(nt))
    file_name = format_t + "-" + title + ".md"  # 文件名
    
    f = open("./template.md", "w")
    text = "---\nlayout: post\ntitle: "+  title.encode('utf-8').decode('gbk') + "\ndate: " + format_t_text + "\ntags: \n  - linux  \n---\n\n\n<!-- more -->\n\n## 111\n"
    f.write(text)
    f.close()
    shutil.copy("./template.md", "../_posts/"+file_name)


if __name__ =="__main__":
    title = str(input("输入文章主题："))
    create_md_file(title)
