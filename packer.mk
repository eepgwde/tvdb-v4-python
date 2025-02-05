## weaves
# Test make file for weaves module testing.

# Now to be used with conda

include defs.mk 

all::
	true

ifneq ($(UUT),)

check::
	:> $(X_LOG)
	$(PYTHON) -m unittest -v tests.$(UUT)

else

check::
	:> $(X_LOG)
	$(PYTHON) -m unittest discover -v -s tests

endif 

install-local:
	$(PIP) install --break-system-packages --user -e .

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
	$(RM) -f $(wildcard dist/*.tar.gz)
	-$(SHELL) -c "cd $(HOME)/.local; pip3 uninstall --yes $(PKG)"

# A fast build
dist-local: uninstall
	$(PYTHON) -m build --sdist --no-isolation --skip-dependency-check

# Not so fast
dist: uninstall
	$(PYTHON) -m build --sdist

install: dist-local
	$(PIP) install --user $(wildcard dist/*.tar.gz)

clean::
	-$(SHELL) -c "find . -type d -name __pycache__ -exec rm -rf {} \;"
	-$(SHELL) -c "find . -type f -name '*.log' -delete "
	-$(SHELL) -c "find . -type f -name '*~' -delete "
	-$(SHELL) -c "find . -type d -name '*egg*' -exec rm -rf {} \; "
	rm -f $(wildcard dist/*)
	rm -f ChangeLog AUTHORS
