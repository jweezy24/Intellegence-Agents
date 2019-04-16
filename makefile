
make:
	pandoc lecture.md --biblio=biblio.bib -o intelligentAgents.rst

python:
	python3 ./example/main.py
