Date: 2014-10-14 14:20
Title: How we should (and should not) collaborate
Tags: collaborate, git, latex, openscience

For those of you how know me (all 10 of you), you are well aware of
where I stand on open science and, more recently, on
reproducibility. For everyone else, I believe strongly in open
science, open writing, open collaboration, accountability, and
documentation. I have nothing to hide when it comes to how I do
science, and I expect the same from my collaborators. With regard to
reproducibility, I promise to make every effort to write methods with
enough detail that will enable you, albeit with some skill required,
to reproduce my results. I will not, most likely, provide anyone with
fully turn-key solutions (e.g, [Docker](http://www.docker.com),
[Vagrant](http://www.vagrantup.com)). I don't believe that's my job as
a scientist, and until someone convinces me otherwise, that's where I
stand.  All that being said, **I welcome collaboration, and would love
to work with you**. Yes, even you. And you.

A recent collaboration of mine has reminded me how much there is for
some of us to learn when it comes to working in, for lack of a better
term, an open science framework. First thing's first: I don't expect
anyone to become a LaTeX expert overnight or understand how to cherry
pick changes across git branches, but here is a list of a few things
that I would prefer not to (read: likely won't) do.

1. Use Microsoft Word
2. Email infinite copies of documents around
3. Provide a sharing solution (e.g, Google Drive, Dropbox) to you,
only to turn around and then email you documents.
4. Engage in endless email threads about changes to documents, tables,
figures, etc.

To address these, here's my preferred working environment and how it
might benefit us to be the most productive when working on a paper together.

###Use LaTeX:

I could go on and on, but my main reasons for writing this way are:

1. Citation management (BibTeX, AucTex, RefTeX, etc.)
2. Plain-text documents lend themselves to version control
3. Version control provides a natural way to collaborate (i.e., via
[Github](http://www.github.com))
4. It's available everywhere, even on the web via
       [Authorea](http://www.authorea.com),
       [WriteLaTeX](http://www.writelatex.com),
       [ShareLaTeX](http://www.sharelatex.com), etc.
5. It makes journal submission much easier!


### Use git

Of course, there are many ways to version control, but this is what I
prefer. It makes working collaboratively possible while keeping
changes safe and contributions accounted-for. It's also what we teach
at [Software Carpentry](http://www.software-carpentry.com) so what
kind of instructor would I be if I didn't use it? It also gets us away
from the (just plain) nasty paradigm of emailing documents around like
`results_1_cf_1_2_modified_cf2_modified_5.csv`.

### Use email for its purpose...

1. To tell me what I a good job I'm doing
2. To set up a time so we can have a conference call to tell me what a
   good job I'm doing
3. To allow me a place to tell you what a good job you're doing
4. You get the idea.

### Use collaboration tools for collaboration

This could mean many things to many people.  To me, it means something like this:

1. If we have documents on Google Drive and you want to chat about it or make changes,
do those things using the tools in Google Drive. This way, we can keep track of
work and requests for work without going completely nuts.
1. If you want to make a significant change to a document we're writing together on
Github, submit an issue or pull request for the same reasons as above
1. Please don't make me log into the same Google Drive that I've
shared to you, click the same `Download` button you could click,
download the files to my computer, and then email them to you.

### For Pete's sake

Please, please, please, take the time to consider what I'm saying and
how you're currently doing things. Might there be some upfront,
getting-used-to-it-ivness? Sure.  I promise, though, it will be worth
it. We have so much technology to help us be the most productive
scientists we can be, and from my own experiences, we are all much
happier when things go smoothly and don't have to spend time on
thoughts like "in what folder did I put that most recent version of
that file."

This concludes rant #546.

--Chris
