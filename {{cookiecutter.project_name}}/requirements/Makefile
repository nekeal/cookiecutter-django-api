.PHONY: all check clean

objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs)

%.txt: %.in
	uv pip compile -v --output-file $@ $<

prod.txt: base.txt
dev.txt: base.txt

check:
	@which uv > /dev/null

clean: check
	- rm *.txt
