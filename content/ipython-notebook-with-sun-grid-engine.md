Date: 2013-07-09 15:55
Title: IPython notebook with Sun Grid Engine
Tags: ipython, sge

Here at VCU, we have what some might call a high performance computing center. While 
this is largely true, there are many limitations to how the current system is 
deployed and managed.  My IT background has made working 
around these limitations somewhat easier, though no less of a PITA.  Hopefully, 
some of these tips can help others, as well.

For the purposes of this tutorial, I will assume that you have Python 2.7.x 
installed with IPython.  I've been using the fabulous Enthought Python 
Distribution (a.k.a. EPD) for quite some time, which gets me most of the 
way there.  As I like living on the edge, I run IPython from the git repo. However, 
the setup described here should largely be the same regardless of the version 
of IPython you choose to run.

A current limitation of IPython notebooks is that they must be served 
from a single directory, which presents an interesting paradigm with 
respect to version control.  This can be managed in multiple ways:

1. Have all notebooks installed in a single folder and version 
control at the top level of the folder, including all *.ipynb files
1. Create a folder for each notebook and tie it to an individual running 
notebook process.

Both of these are possible, and working with either scenario should hopefully 
be clear by the end of this document.  If not, definitely check out the 
[IPython documentation](http://ipython.org/ipython-doc/dev/config/index.html).  

#Create an IPython profile
    ipython profile create --parallel --profile=sge
	
This will create a profile as IPYTHONDIR/profile_sge

#Edit the cluster profile file

Open `ipcluster_config.py` and make the following edits:

    c.IPClusterEngines.engine_launcher_class = "SGEEngineSetLauncher"
    c.IPClusterStart.controller_launcher_class = "SGEControllerLauncher"
	
This setting enables submitting the controller and engines as SGE qsub jobs.

#Edit the notebook profile file

Open `ipython_notebook_config.py` and make the following edits:

    c.NotebookApp.password = ...
	c.NotebookManager.save_script=True
	
The first line sets a password to use for the notebook.  How to do this is 
in the [documentation](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html#security).
The second line saves the notebook out as a Python file for use later.  None of these are 
necessarily important for running with SGE, but I'm noting them here anyway.

#Hack the IPython frontend

Our cluster setup has compute nodes which all have access to any one of several 
NFS mounts.  While this is somewhat of a generic setup, a _feature_ which can 
result is a write delay of the controller and engine scripts that get dropped 
when starting a cluster from the notebook. To get around this, I made an edit to 
`lib/python2.7/site-packages/IPython/html/services/clusters/clustermanager.py` which 
changes `delay = CFloat(1., config=True,...)` to delay = CFloat(30., config=True,...).
This effectively will, when a cluster is initiated from the notebook, start a controller 
process via qsub, wait 30 seconds, then start the array job for the engines. This is a 
definite hack, and I'd like to see it implemented as a feature sometime in the future. I 
should probably file a bug...

#Create scripts to start the job

I created two scripts to start the notebook process on the cluster.

`notebook_qsub.sh`

    #!/bin/bash
    qsub -cwd -V -N inotebook start_notebook.sh
	
`start_notebook.sh`

	#!/bin/bash
	ipython notebook --pylab inline --no-browser --profile=sge
	
I put both of these scripts in the folder which will house my notebooks (see options 
above), make them both executable (`chmod +x`).  Because I'm passing `-cwd`, these scripts 
will operate from the current working directory (i.e., where the ipynb files are).  

#Start the notebook

Starting the notebook is simple now.  I just cd to the directory where the notebooks are 
and run `./notebook_qub.sh`.  Assuming all goes well, I should now have my notebook process, 
named "inotebook", showing up when running `qstat`.

#Connect to the notebook
Unfortunately, the notebook process will now be running on a compute node, which is not accessible 
from the outside network.  To enable access from my machine, I do a little SSH tunneling magic.  It 
goes like this:

Open up your .ssh/config and make the following edits

    Host <submitnode>
    User <username>
    HostName <fully.qualified.domain.name.of.submitnode>
    
	Host <computenode>
	User <username>
	ProxyCommand ssh <submitnode> -W %h:22
	LocalForward localhost:8888	localhost:8888
	
This will enable you to `ssh <computenode>` and tunnel the connection through the `<submitnode>` to which 
you already have access.  The port will be forwarded, through, as well, so all you need to do is now is fire-up 
your favorite, websocket-enabled browser, and hit `http://localhost:8888`. You should now also be able to go the Clusters tab and fire up a cluster.  If you `watch qstat`, you should see 
the controller job start, wait, and then the engines will start.  	

I'm definitely making some assumptions here about architecture and that SSH forwarding is enabled in your 
environment. Your mileage may vary, but I hope this gives a good overview of what my process looks like. 
More about this problem can be found on my 
[StackExchange post](http://stackoverflow.com/questions/15376992/starting-an-ipython-cluster-from-the-notebook-with-a-delay).

 
