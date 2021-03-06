# Core Library modules
import datetime
import os
import re

# Third party modules
import pymysql


def generate_file(d):
    new_filename = d["filename"].split(".")[0] + ".md"
    filename = os.path.abspath(new_filename)
    # if os.path.isfile(filename):
    #     return
    date = datetime.datetime.utcfromtimestamp(d["last_edited"])

    pattern = re.compile("<h1>.*?</h1>\n")

    content = d["content"]
    content = re.sub(pattern, "", content)

    with open(filename, "w") as f:
        f.write(
            f"""---
layout: post
title: {d['title']}
summary: {d['description']}
slug: {d['filename'].split('.')[0]}
author: Martin Thoma
date: {date:%Y-%m-%dT%H:%M:%S}
category:
featured_image:
---
{content}
"""
        )


if __name__ == "__main__":
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd=os.environ["MYSQL_PW"],
        database="martin-thoma-de",
    )

    cursor = mydb.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM artikel")

    myresult = cursor.fetchall()

    # ['id', 'filename', 'title', 'content', 'description', 'priority', 'last_edited', 'last_editor_id']
    for x in myresult:
        generate_file(x)
