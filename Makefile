PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '   submmodule			   update submodules                  '


html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver: 
	$(BASEDIR)/develop_server.sh restart

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)


github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages:master
	git push

submodule:
	git submodule update --recursive	

travis: publish
	ghp-import $(OUTPUTDIR)
	git remote remove origin
	git remote add origin https://cfriedline:${GH_TOKEN}/cfriedline/cfriedline.github.com
	git push origin gh-pages:master

.PHONY: html help clean regenerate devserver publish github submodule
