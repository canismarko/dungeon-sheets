install:
	python setup.py install
	@echo ""
	@echo "================="
	@echo "For optimal performance we highly recommend installing PDFTK: https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/"
	@echo "If installing on OSX >= 10.11, see here: https://stackoverflow.com/questions/32505951/pdftk-server-on-os-x-10-11/33248310#33248310"

test:
	python -m unittest discover tests/

