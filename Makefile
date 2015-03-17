# vim: noexpandtab:syntax=make
CWD	=$(shell pwd)
PYTHON =python3
PYTHON_LIB_DIR =`$(PYTHON) -c "import site;print(site.getsitepackages()[0])"`
PYTHON_MODULE_NAME=demo
VCS_COMMIT=git commit
VCS_URI=git@github.com:cochiseruhulessin/demo-django-simple.git
PIP=pip3


clean:
	@find . | grep -E "(__pycache__|\.pyc$\)" | xargs rm -rf
	@rm -rf dist build
	@rm -rf *.egg-info
	@rm -rf ../*.orig.tar.gz
	@rm -rf *.egg-info


commit:
	make clean
	make coverage
	$(VCS_COMMIT)


coverage:
	./run_tests -x


install:
	make links
	$(PIP) install -r requirements.txt

install-development-deps:
	pip3 install coverage nose

links:
	@rm -rf $(PYTHON_LIB_DIR)/$(PYTHON_MODULE_NAME)
	@ln -s $(CWD)/$(PYTHON_MODULE_NAME) $(PYTHON_LIB_DIR)/$(PYTHON_MODULE_NAME)


reset-repo:
	@rm -rf .git
	@make clean
	@git init
	@git add .
	@git commit -m "Initial commit"
	@git remote add github $(VCS_URI)
	@git push -u --force github master
