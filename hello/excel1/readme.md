### python3 setup

- amd64

```text
https://www.python.org/ftp/python/3.8.8/python-3.8.8-embed-amd64.zip
```

- x86 (32bit)

```text
https://www.python.org/ftp/python/3.8.8/python-3.8.8-embed-win32.zip
```

### install module (pandas xlrd pyinstaller)

```shell
pip install pandas xlrd pyinstaller yaml
```

### 打包成一个exe (在目录 dist 中)

```shell
pyinstaller -F psm-import.py
```

### 程序运行
```shell
psm-import.exe -e "psm.xls" -d "psm.db" -c "psm.yaml"
# or
psm-import.exe -ef "psm.xls" -df "psm.db" -cf "psm.yaml"
# or
psm-import.exe -e "c:/psm.xls" -d "c:/psm.db" -c "c:/psm.yaml"
```
