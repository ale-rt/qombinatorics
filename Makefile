local:
	python setup.py install
sdist:
	python setup.py sdist --formats=gztar,zip,bztar
rpm:
	python setup.py bdist --formats=rpm

ui:
	pyuic4 qombinatorics/QombGui.ui > qombinatorics/QombGui.py

rcc:
	pyrcc4 qombinatorics/QombResources.qrc >qombinatorics/QombResources_rc.py

test:
	PYTHONPATH=. python ./qombinatorics/QombLib.py

launch:
	PYTHONPATH=. python ./scripts/qombinatorics
