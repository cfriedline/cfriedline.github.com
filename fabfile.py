import datetime
import slugify
from fabric.api import local, env
import os


#borrowed from https://github.com/esacteksab/fabric4pelican
def new_post(title, slug=None, post_type="post"):
    if slug is None:
        slug = slugify.slugify(u'%s' % title)
        header = len(slug) * '#'
    now = datetime.datetime.now()
    post_date = now.strftime("%Y-%m-%d %H:%M")

    params = dict(
        date=post_date,
        title=title,
        header=header,)
        
    if "post" in post_type:
        out_file = "content/{}.md".format(slug)
    else:
        out_file = "content/pages/{}.md".format(slug)
        
    if not os.path.exists(out_file):
        with open(out_file, "w") as o:
            if "post" in post_type:
                o.write("Date: %s\nTitle: %s\nTags: %s\n" % (post_date, title, ""))
            else:
                o.write("Title: %s\n\n" % (title))
        print "Wrote %s" % (out_file)
    else:
        print ("{} already exists.".format(out_file))


# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def publish():
    local('pelican -s publishconf.py & '
          'ghp-import %s & '
          'git push git@github.com:cfriedline/cfriedline.github.com gh-pages:master & '
          'git push' % env.deploy_path)
