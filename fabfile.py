#borrowed from https://github.com/esacteksab/fabric4pelican

import os
import datetime
import slugify
from fabric.api import puts, local
from jinja2 import Environment, FileSystemLoader

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
    
)
        
    if not os.path.exists(out_file):
        with open(out_file, "w") as o:
            if "post" in post_type:
                o.write("Date: %s\nTitle: %s\nTags: %s\n" % (post_date, title, ""))
            else:
                o.write("Title: %s\n\n" % (title))
        print "Wrote %s" % (out_file)
    else:
        print ("{} already exists.".format(out_file))
        
