all:
	python scripts/process.py

clean:
	rm data/* archive/*

.PHONY: clean
