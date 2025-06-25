import time
def callback(commit):
    commit.author_name = b"Prachidubeyyy"
    commit.author_email = b"prachidubey3030@gmail.com"
    commit.committer_name = b"Prachidubeyyy"
    commit.committer_email = b"prachidubey3030@gmail.com"
    commit.author_date = commit.committer_date = b"%d +0530" % int(time.time())
