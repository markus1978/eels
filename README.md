# parser-skeleton

## About

This is not a real parser, its a skeleton for parsers. To write you own parsers, its
best to fork this skeleton and use it as a template.

## Setup and run example

We are currently targeting Python 3.6. Some nomad dependencies might still have problems
with 3.7++. It will definitely not work with 2.x. If you run into troubles, you could
try to ignore some dependencies. Most of them are only used in the DFT context.

Best use a virtual environment:
```
virtualenv -p python3 .pyenv
source .pyenv/bin/activate
```

Clone and install the nomad infrastructure and the necessary dependencies (including this parser)
```
git clone https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR nomad
cd nomad
git submodule update --init
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
./dependencies.sh -e
pip install -e .
```

The parsers (among other things) are git submodules. The `./dependencies.sh` will run
through all the sub modules and install them as pip packages (be in you virtual env!).

Fork this project on [gitlab](https://gitlab.mpcdf.mpg.de/nomad-lab/parser-skeleton).
Rename your fork in its settings/advanced and move it to the nomad-lab namespace.
Choose a name that starts with `parser-`, e.g. `parser-your-parser-name`.
You'll need a [http://www.mpcdf.mpg.de](https://www.mpcdf.mpg.de/userspace/forms/onlineregistrationform) account.

Add your parser to the nomad project on a separate branch:
```
git checkout -b your-parser-name
git submodule add https://gitlab.mpcdf.mpg.de/nomad-lab/parser-your-parser-name dependencies/parsers/your-parser-name
```

Do the necessary changes:
- [setup.py](setup.py): Change the project metadata
- [skeletonparser](skeletonparser): Change the directory name, i.e. python package name (no uppercases, no `_` please)
- [skeletonparser/__init__.py](skeletonparser/__init__.py): Implement your parser, change the class names
- [skeletonparser/__main__.py](skeletonparser/__main__.py): Change the module/class names
- [skeletonparser/skeleton.nomadmetainfo.json](skeletonparser/skeleton.nomadmetainfo.json): Change the name, add your metadata definitions.
- [README.md](README.md): Change this readme accordingly.
- probably some other things I forgot.

General metadata quantities (those that we can agree on) go to
`dependencies/nomad-meta-info/meta_info/nomad_meta_info/general.experimental.nomadmetainfo.json`.
But we should agree first. In the mean time, just put them in [skeletonparser/skeleton.nomadmetainfo.json](skeletonparser/skeleton.nomadmetainfo.json).
You can browse around `dependencies/nomad-meta-info/meta_info/nomad_meta_info/` to
see example definitions. **You cannot add values or open sections without defining them first!**

To run the parser:
```
cd nomad/dependencies/parsers/your-parser-name
python -m yourparserpythonpackage tests/example.metadata.json
```

## Docs

Click through the [nomad archive page](https://metainfo.nomad-coe.eu/nomadmetainfo_public/archive.html)
to learn about the *meta-info* metadata format and how to define your metadata.

Here is a more involved tutorial (but its pretty DFT and parsing text files specific):
[nomad@fairdi docs](http://enc-staging-nomad.esc.rzg.mpg.de/fairdi/nomad/docs/parser_tutorial.html)

## FAQ

For any questions, **please open issues** (regarding parser development and using this skeleton)
in this [parser-skeleton project](https://gitlab.mpcdf.mpg.de/nomad-lab/parser-skeleton/issues).
We will compile a FAQ from your issues.
