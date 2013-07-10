Date: 2013-07-10 10:47
Title: Managing IPython notebooks with GitHub
Tags: ipython, git

In the process of moving all of my new code to GitHub, I started thinking about how I 
wanted to manage things like my IPython notebooks. Previoulsy, with my code 
on [Bitbucket](http://bitbucket.org/cfriedline), I created a single hg [repo](https://bitbucket.org/cfriedline/cluster_ipynb) 
for all of my notebooks on our cluster. Given that the notebooks have to live in a single 
directory for every instance of the notebook, I did that to avoid having to run multiple notebook 
processes for each of the notebooks I was working on.

It occured to me today that there is another possible solution to this, and one I'll be using 
for all of my new code (which will be on [GitHub](http://github.com/cfriedline)). The process looks 
like this, and seems much less messy from a VCS standpoint.

1. Launch a notebook process on the cluster (or use an existing one)
1. Create a new notebook file
1. Create a new directory on the cluster to house the 
notebook file (with `touch`'ed `.gitignore` and `README.md` files)
1. Move the notebook to this directory
1. Create a new repo on GitHub
1. `git add .`, `git commit`, `git remote add origin`, `git push origin master`, etc.
1. Symlink the `.ipynb` file back into the directory from where the notebook is running.

Seems to work great. Note that deleting the notebook from the Dashboard will only 
delete the symlink, not the notebook itself. Maybe a safety feature, maybe an annoyance, but 
only time will tell. Simple enough.


