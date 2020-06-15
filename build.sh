pyinstaller --paths=./bin ./bin/main.py \
    --additional-hooks-dir=hook-main.py
    --hidden-import=pandas
    --onefile
cd dist/main
./main