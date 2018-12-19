all: wizard druid rogue warlock

clobber:
	rm -f wizard.pdf rogue.pdf warlock.pdf druid.pdf

redo: clobber all

wizard: wizard.pdf

rogue: rogue.pdf

warlock: warlock.pdf

druid: druid.pdf

wizard.pdf: wizard.py
	makesheets wizard.py

rogue.pdf: rogue.py
	makesheets rogue.py

warlock.pdf: warlock.py
	makesheets warlock.py

druid.pdf: druid.py
	makesheets druid.py

