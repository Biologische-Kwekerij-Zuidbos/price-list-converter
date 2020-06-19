rm -rf build dist
mkdir build dist

pyinstaller ./bin/main.py \
    --hidden-import=pandas \
    --hidden-import=pkg_resources.py2_warn

cd ./dist/main
./main