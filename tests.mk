.PHONY: all all-local check check-local view-local clean-local clean

RLWRAP ?= 
# RLWRAP ?= rlwrap
PYTEST ?= unittest

REMAKE := $(MAKE) MAKEFLAGS=$(MAKEFLAGS) MAKEFILES="$(MAKEFILE_LIST)"

all:
	true

TESTS0 := $(wildcard tests/test_*.py)
TESTS00 := $(basename $(notdir $(TESTS0)))
TESTS1 ?= $(addsuffix .log,$(TESTS00))
TESTS2 ?= $(addprefix m-,$(TESTS1))
TESTS2 ?= $(addprefix m-,$(TESTS1))

RUNS0 := $(wildcard tests/run_*.py)
RUNS00 := $(basename $(notdir $(RUNS0)))
RUNS1 ?= $(addsuffix .log,$(RUNS00))
RUNS2 ?= $(addprefix m-,$(RUNS1))

check:
	$(REMAKE) check-local

tests.log: $(TESTS1)
	cat $(TESTS1) > $@

m-tests.log: $(TESTS1)
	cat $(TESTS2) > $@

X_TARGETS ?= tests.log m-tests.log

check-local: $(TESTS1) $(X_TARGETS)

all-local: $(RUNS1)


m-%.log %.log: tests/%.py
	:> $*.log
	( $(RLWRAP) python -m $(PYTEST) -v $< ) 2>&1 | tee m-$*.log
	cat test.log > $*.log

view-local:
	@echo TESTS0 $(TESTS0)
	@echo TESTS00 $(TESTS00)
	@echo TESTS1 $(TESTS1)
	@echo TESTS2 $(TESTS2)
	@echo RUNS0 $(RUNS0)
	@echo RUNS00 $(RUNS00)
	@echo RUNS1 $(RUNS1)

clean-local:
	-$(RM) $(TESTS1) $(TESTS2) $(RUNS1) $(RUNS2)
	-$(RM) $(X_TARGETS)
