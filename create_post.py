import argparse
import slugify
import datetime
import os


def new_post(title, slug=None, post_type="post"):
    if slug is None:
        slug = slugify.slugify(u'%s' % title, to_lower=True)
    now = datetime.datetime.now()
    post_date = now.strftime("%Y-%m-%d %H:%M")

    if "post" in post_type:
        out_file = "content/{}.md".format(slug)
    else:
        out_file = "content/pages/{}.md".format(slug)

    if not os.path.exists(out_file):
        with open(out_file, "w") as o:
            if "post" in post_type:
                o.write("Date: %s\nTitle: %s\nTags: %s\n" % (post_date,
                                                             title, ""))
            else:
                o.write("Title: %s\n\n" % (title))
        print("Wrote %s" % (out_file))
    else:
        print("{} already exists.".format(out_file))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title",
                        type=str,
                        help="post title",
                        required=True)
    args = parser.parse_args()
    if args.title:
        new_post(args.title)

if __name__ == '__main__':
    main()
