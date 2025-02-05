include defs.mk

all:
	true

TESTS0 := $(wildcard tests/test_*.py)
TESTS00 := $(basename $(notdir $(TESTS0)))
TESTS1 ?= $(addsuffix .log,$(TESTS00))
TESTS2 ?= $(addprefix m-,$(TESTS1))

RUNS0 := $(wildcard tests/run_*.py)
RUNS00 := $(basename $(notdir $(RUNS0)))
RUNS1 ?= $(addsuffix .log,$(RUNS00))
RUNS2 ?= $(addprefix m-,$(RUNS1))

XTRA0 := $(wildcard tests/xtra_*.py)
XTRA00 := $(basename $(notdir $(XTRA0)))
XTRA1 ?= $(addsuffix .log,$(XTRA00))
XTRA2 ?= $(addprefix m-,$(XTRA1))

check:
	$(REMAKE) check-local

tests.log: $(TESTS1)
	cat $(TESTS1) > $@

m-tests.log: $(TESTS1)
	cat $(TESTS2) > $@

X_TARGETS ?= tests.log m-tests.log

check-local: $(TESTS1) $(X_TARGETS)

xtra-local: $(XTRA1)

all-local: $(RUNS1)


# you only need RLWRAP set to rlwrap if you want to have a line-editting
# and command history in the pdb debugger.
m-%.log %.log: tests/%.py
	:> $*.log
	:> test.log
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
	@echo XTRA0 $(XTRA0)
	@echo XTRA00 $(XTRA00)
	@echo XTRA1 $(XTRA1)

clean-local:
	-$(RM) $(TESTS1) $(TESTS2) $(RUNS1) $(RUNS2) $(XTRA1) $(XTRA2)
	-$(RM) $(X_TARGETS)

clean: clean-local
	$(RM) $(X_TARGET)
