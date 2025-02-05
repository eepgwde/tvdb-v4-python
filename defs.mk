## weaves
# Common defines for the Makefile .mk files we have

# Fix this with := 
PKG := tvdb_v5_unofficial

PYTHON ?= python3
PIP ?= pip3

# RLWRAP ?= rlwrap
RLWRAP ?=

# For testing and documents
PYTEST ?= unittest
UUT ?= 
X_LOG ?= test.log
X_TARGET ?= $(X_LOG) make.log

DOCSDIR ?= docs/

## Some features for make(1)
# record the top-level directory
TOP ?= $(shell pwd)

# all often used targets
# check, check-local and xtra-local run tests
# view-local is used to display MAKE variables, usually file lists
.PHONY: all all-local check check-local view-local clean-local clean xtra-local dist dist-local

REMAKE := $(MAKE) MAKEFLAGS=$(MAKEFLAGS) MAKEFILES="$(MAKEFILE_LIST)"

# for running tests and scripts
PYTHONIOENCODING=utf-8
PYTHONPATH ?= .:$(TOP)/$(PKG)
export PYTHONPATH
