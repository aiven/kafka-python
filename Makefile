all:
	: try "make rpm"

rpm:
	git archive --output=rpmpkg-src.tar.gz --prefix=kafka-python/ HEAD
	rpmbuild -bb kafka-python.spec \
		--define '_sourcedir $(shell pwd)' \
		--define 'major_version $(shell git describe --tags --abbrev=0 | cut -c2-)' \
		--define 'minor_version $(subst -,.,$(shell git describe --tags --long | cut -f2- -d-))'
	$(RM) rpmpkg-src.tar.gz
