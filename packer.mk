## weaves
# Test make file for weaves module testing.

# Now to be used with conda

PYTHON ?= python3
PIP ?= pip3
UUT ?= 
FILE ?= test.log
PYTHONIOENCODING=utf-8
DOCSDIR ?= docs/
PKG := tvdb_v5

export SDIR

all::
	true

ifneq ($(UUT),)

check::
	:> $(FILE)
	$(PYTHON) -m unittest -v tests.$(UUT)

else

check::
	:> $(FILE)
	$(PYTHON) -m unittest discover -v -s tests

endif 

install-local:
	$(PIP) install --break-system-packages --user .

clean::
	$(RM) $(wildcard *.pyc *.log *~ nohup.out)

distclean::
	$(RM) -rf html
	$(RM) $(wildcard *.json)

## Install

.PHONY: uninstall dist-local docs dist install-local distclean

# --no-private 

docs: 
	rm -rf ${DOCSDIR}
	epydoc -v \
					--no-frames --no-sourcecode --name="weaves-poset" \
					--url="https://github.com/eepgwde/weaves-poset" \
					--inheritance listed --html \
					--graph classtree --show-private --show-imports \
					--css etc/epydoc.css -o ${DOCSDIR} weaves/*.py

uninstall::
	rm -f $(wildcard dist/*.tar.gz)
	-$(SHELL) -c "cd $(HOME)/.local; pip3 uninstall --yes $(PKG)"

dist-local: uninstall
	$(PYTHON) setup.py sdist

install: dist-local
	$(PIP) install --user $(wildcard dist/*.tar.gz)

dist:
	scp $(wildcard dist/*.tar.gz) root@glenda:/var/www/html/weaves-dev.tar.gz

clean::
	-$(SHELL) -c "find . -type d -name __pycache__ -exec rm -rf {} \;"
	-$(SHELL) -c "find . -type f -name '*.log' -delete "
	-$(SHELL) -c "find . -type f -name '*~' -delete "
	-$(SHELL) -c "find . -type d -name '*egg*' -exec rm -rf {} \; "
	rm -f $(wildcard dist/*)
	rm -f ChangeLog AUTHORS
