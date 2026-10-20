
upload:
	rm -rf dist
	python3 -m build
	python3 -m twine upload dist/*

clean:
	rm -rf dist
	rm -rf T__*

commit:message.txt
	git commit -aF message.txt
	git push
	git pull

lint:
	python3 -m black src/queenbeethreading/*.py

test-upload:
	rm -rf dist
	python3 -m build
	python -m twine upload --repository testpypi dist/*
