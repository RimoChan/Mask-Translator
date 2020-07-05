import os
from pathlib import Path
import fire
import shutil
import yaml
import logging

import 翻譯

logging.basicConfig(level=logging.INFO)


def go(o):
    輸入路徑 = Path('.')
    輸出路徑 = Path(o)

    assert 輸入路徑.is_dir()
    if not 輸出路徑.is_dir():
        if 輸出路徑.is_file():
            raise Exception('???')
        else:
            os.mkdir(輸出路徑)

    with open(輸入路徑 / 'translator.config.yaml', encoding='utf8') as f:
        config = {
            'list_of_files_to_translate': [],
            'list_of_files_to_copy': [],
            **yaml.safe_load(f),
        }

    for x in config['list_of_files_to_translate']:
        if not x.endswith('.py'):
            logging.warning(f'{x} 不是Python代碼，可能有問題。')
            
        with open(輸入路徑 / x, encoding='utf8') as f:
            結果 = 翻譯.處理(f.read())
        with open(輸出路徑 / 翻譯.處理(x), 'w', encoding='utf8') as f:
            f.write(結果)
            
        logging.info(f'translate {輸入路徑 / x} -> {輸出路徑 / 翻譯.處理(x)}')

    for x in config['list_of_files_to_copy']:
        if (輸出路徑 / x).is_dir():
            shutil.rmtree(輸出路徑 / x)
        if (輸出路徑 / x).is_file():
            os.remove(輸出路徑 / x)

        if (輸入路徑 / x).is_dir():
            shutil.copytree(輸入路徑 / x, 輸出路徑 / x)
        elif (輸入路徑 / x).is_file():
            shutil.copy(輸入路徑 / x, 輸出路徑 / x)

        logging.info(f'copy {輸入路徑 / x} -> {輸出路徑 / x}')


fire.Fire(go)
