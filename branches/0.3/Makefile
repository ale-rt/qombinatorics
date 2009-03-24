local:
	python setup.py install
sdist:
	python setup.py sdist --formats=gztar,zip,bztar
rpm:
	python setup.py bdist --formats=rpm

test:
	PYTHONPATH=. python ./qombinatorics/QombLib.py

launch:
	PYTHONPATH=. python ./scripts/qombinatorics
