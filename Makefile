PY=python
PELICAN=pelican
PELICANOPTS=

GHP-IMPORT=ghp-import

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
GIT_MESSAGE="Manual deploy to GitHub pages"

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


github: clean html
	git branch -D gh-pages
	$(GHP-IMPORT) -m $(GIT_MESSAGE) $(OUTPUTDIR)
	git push -f origin gh-pages:master
	git push

submodule:
	git submodule update --init --recursive

travis: html
	git config --global user.name "Chris Friedline"
	git config --global user.email cfriedline@vcu.edu
	$(GHP-IMPORT) -m "Travis build ${TRAVIS_BUILD_NUMBER}" $(OUTPUTDIR)
	git remote remove origin
	@git remote add origin https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git
	@git push -f origin gh-pages:master &> /dev/null

.PHONY: html help clean regenerate devserver publish github submodule travis
