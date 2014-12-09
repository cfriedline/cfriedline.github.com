Date: 2014-09-30 22:02
Title: Software Carpentry at Penn Redux
Tags: swcarpentry, teaching, sql, python

##Intro and shell (day 1)

This post has been a long time coming, since
[R. David Murray](http://www.twitter.com/rdavidmurray) and I taught
the [bootcamp](http://swcarpentry.github.io/2014-08-21-upenn) on
8/21-22/2014. Sadly, I've been struggling with wrangling my own data,
collaborators, going to NSF, planning sampling trips, helping to train
the new undergrads in the lab, and about 1000 other things since
then. Luckily, no one reads my blog.

The planning for this bootcamp came together very quickly, and I think
all parties can agree that some things could have been tightened up a
little bit. With that said, I think it went off really well. It was an
amazing experience both as a scientist to be immersed in that
stimulating of an environment and as an instructor having the good
fortune of a body of students so excited and (dare I say) hungry for
the material. I was extremely proud to be representing Software
Carpentry, and I hope we did the name justice when all was said and
done.

If you've ready my [bio](/pages/about.html), you already know that I lived
around the Philadelphia area for several years before moving to
Richmond, VA. It was great to be back in the city and having dinner at
old ([Monk's Cafe](http://www.monkscafe.com)) and new
([Crow and the Pitcher](http://crowandthepitcher.com)) places. The
folks at Penn were able to secure us great rooms at
[Club Quarters](http://clubquarters.com/philadelphia), too, providing a
great walk over to campus to begin and end the day.

David and I arrived early on the first day in case anyone had issues
with getting the required software up and going before we got
started. No one really needed our help for this part, so we spent the
time getting our laptops connected to the projector, finding the chalk
(I love chalk!) for the boards, and planning the day. We settled on
each teaching for 1/2 of each day with David handling Bash and Python
and me up for git and SQL. I sent out a few tweets about this, but I
feel like we (myself included) were all quite fortunate to have a core
CPython maintainer going over shell and Python lessons. Having not
taught a huge amount (by his own admission), I thought David delivered
all of his lessons with an expected level of mastery. That afternoon,
I taught the git material, but perhaps in a different way than
before.

###Cleaning example files

We needed to distribute the examples to the
course participants, but when I went out to the bootcamp site, they
already had the examples worked through in the lesson notebooks. As a
quick hack, I set these up cleaned versions using another
[IPython notebook](https://github.com/swcarpentry/2014-08-21-upenn/blob/gh-pages/create_clean_dist_files.ipynb)
to run through the examples in the bootcamp course material and strip
out the output cells and zip it all up nice and pretty-like. Seemed to
work pretty well, so if anyone wants it, please feel free to use
it. Moving forward, it would be nice if we had clean versions
committed to the repos from the start, I think.

###Teaching git

Throughout the instructor training (did I mention this was my first
time teaching a bootcamp?) and after, it was never clear to me the
direction with which the lessons were to be delivered. It seemed to
be entirely up to the particular instructor, a situation in which I'm
very comfortable, but I didn't want to step on any toes. Reading
through the git material, I thought it would make much more sense to,
sort-of, pseudo-flip, the lesson material. In this way, I could
introduce some of the material (say 15 minutes a time) and then set
the bootcamp attendees off and running with the lessons as lined out
in the course material. I also paired them up to work on a
collaborative scenario in which the work done in previous lessons was
shared via pull requests to their partner's repository on github
(which also got them all github accounts!).

In terms of my own delivery, I did something perhaps unorthodox. **I
taught git without a GUI and without dropping to the shell**. Instead,
I used an [IPython notebook](http://www.ipython.org). Well, not just a
plain notebook, but one with
[Damian Avila](https://github.com/damianavila/live_reveal)'s live
reveal slideshow extension and the `%rehashx` + `%automagic on`
magics. I did this for a couple of reasons: 1) to introduce the
students to the IPython notebook which they would be seeing when David
taught Python and 2) to have a continuity in my lessons without having
to have presentation slides dropping out to a shell and back again. I
was very pleased with out it all went down on this front - there were
some minor glitches related to the projector and getting confused with
too many Google Chrome windows, but that was all quite
self-inflicted. Having a ready shell integrated with presentation
slides was, from my point of view, a pretty effective way to deliver
the material. I would welcome feed back here, especially from the
bootcamp participants on how it actually went over. The notebook
containing the slides can be downloaded
[here](https://github.com/cfriedline/swc-slides/blob/master/2014-08-21-upenn/git.ipynb).

So, with that out of the way, the git lessons in the course material
were already quite solid, so I didn't really add anything there except
to pair the students up for pushing and pulling in two common
collaborative models: 1) granting access to collaborators to your own
repository and 2) forking a repository and submitting pull
requests. We discussed the safety and pain of both approaches and from
the comments and questions, it was pretty clear to me that we
accomplished several things:

1. That git (or version control, in general) is important.
1. That using git isn't too hard
1. That collaborating using version control is entirely within reach

It was great to hear the immediate feed back from both PIs and their
students that the skills we were presenting to them were going to be
put into practice immediately, a fact that's both stimulating as an
instructor and satisfying as an advocate for best practices in the
real world.

### The room and the Etherpad

As with most Software Carpentry bootcamps, we set up and monitored
an [Etherpad](https://swcarpentry.etherpad.mozilla.org/2014-08-21-upenn?). I thought
this was particularly effective, especially given the room setup.

<img src="/images/swc_upenn.png" width="500px")

Unfortunately, what I alluded to earlier about some of things not
coming together as they normally would have given more time, is that
we were allocated an auditorium setting in which to run the
bootcamp. This meant that it would be difficult for us to get to
students in the middle of the rows to help them, and also that the
highly effective "Post-it barometer system of understanding" could not
be used because we couldn't see people's laptops to which the notes
would be stuck. This is where the Etherpad came in, much more so on
day one than day two (not sure why). I was able to answer many
questions on it while David was teaching. David was able to monitor it
while I was teaching as well. I've heard reports that instructors
often keep their own copy open while they're lecturing, but I think
that, for me at least, it would be really distracting. Having someone
else there to monitor it was really helpful. It's also a great
resource for data mining and adjusting lessons in the future, though I
will admit that I haven't had a chance to go back to my slides and
adjust.  All in all, the room worked out fine, so if there are
reservations about this in the future, it turned out (at least for us)
to be not that big of a deal.

### Live tweeting

I attempted to live tweet while David was teaching as well as
encouraging others to do so, as well. However, it seemed like our
audience wasn't too into it, so I personally devoted most of my time
to the Etherpad. It didn't stop me from sending a few tweets out,
though. I think in the future, I'll make more of an effort to get
participants to do this, as it's a great motivator for instructors to
do well and is great free promotion for the organization.

##Day 2

Day two started off with David teaching Python. We agreed that he'll
likely also take some time after lunch, and took a quick poll to make
sure that everyone was cool with maybe having a little less time with
SQL in the afternoon. We polled also to make sure that SQL was
something that they wanted because David and I kicked around spending
the whole day on Python. We all agreed: rock through all of the Python
and then introduce as much as spastically (because I was teaching?)
possible the SQL portion. Again, David did a great job explaining core
Python concepts to everyone, and I had very little to do expect to
chime in with some cool tidbits about the notebook I've come across
since it's a hugely important part of my daily workflow. I also got to
talk with some of the participants about remote notebooks and
submitting jobs into a cluster batch system, functionality that not
only to people not realize is there, but also how harnessable it all
is once you know a little bit about the IPython ecosystem. I get way
too excited about it, too, which I'm sure is annoying, but I won't
apologize. IPython changed my life. There, I said it.

I wrapped up the day by teaching through the SQL lessons, actually
using the delivered bootcamp material rather than my own slides like
I did with the git lessons.  We went fast, but I tried to be engaging
and informative. I tried to drive home some of the inherent coolness
of databases in general and how they can immediately be applied, as I
have done, in common next-generation sequencing and phylogenetics
workflows. In a room full of material scientists, I was even able to
find a fellow phylogeneticist to talk to about how I handle some of my
data in git, Python, and SQL
([Dogfooding](http://en.wikipedia.org/wiki/Eating_your_own_dog_food),
at it's best).

##Final thoughts

I really enjoyed teaching this bootcamp and getting to geek out with
fellow scientists for a couple of days, especially with scientists who
work in completely different areas than my own. The attendees made
this bootcamp great, too, as would be true with anything like
this. They were excited, engaged, had great questions, and were
totally appreciative of our time. It's not usually the case that one
volunteers (at least for me) with the idea that they should be
showered with praise, but it's really rewarding when you know your
time was well-spent.

It was great to meet and teach with David, and I learned a lot from
watching him teach a subject in which he is an expert. I also enjoyed
our conversations walking back to the hotel from campus. It would be a
pleasure to teach with him again, and I have absolutely no reservations
in recommending him as an instructor for future bootcamps.

In the future, I'll also make sure to do a better job to express the
importance of both the pre- and post-bootcamp surveys.

I especially want to thank Doug J., David S., and Charlotte M. for
taking such great care of us while we were there. From getting us
going in the rooms, to arranging lodging, and providing us with
amazing students, satisfying lunches, and completely essential coffee
breaks, it was a top-notch, class-act all the way. Thank you, thank
you, thank you.

Though my schedule is kind of absurd these days, I'll be sure to carve
out as much time as I can in the future to be able to teach one of
these bootcamps again (and hopefully it won't be too long, hint.). It
was privilege.

--Chris
