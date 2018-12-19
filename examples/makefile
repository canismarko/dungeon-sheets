all: multiclass multiclass_2 wizard druid rogue warlock

clobber:
	rm -f multiclass.pdf multiclass_2.pdf wizard.pdf rogue.pdf warlock.pdf druid.pdf

redo: clobber all

multiclass: multiclass.pdf

multiclass_2: multiclass_2.pdf

wizard: wizard.pdf

rogue: rogue.pdf

warlock: warlock.pdf

druid: druid.pdf

multiclass.pdf: multiclass.py
	makesheets multiclass.py

multiclass_2.pdf: multiclass_2.py
	makesheets multiclass_2.py

wizard.pdf: wizard.py
	makesheets wizard.py

druid.pdf: druid.py
	makesheets druid.py

rogue.pdf: rogue.py
	makesheets rogue.py

warlock.pdf: warlock.py
	makesheets warlock.py
