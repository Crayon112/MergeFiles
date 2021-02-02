# coding: utf-8
import os
import config

class MergeFiles(object):

    def __init__(self, files=config.SOURCE, target=config.TARGET, exclude=config.EXCLUDE, encoding=config.ENCODING):
        self.files = self._files(files, exclude)
        self.target = target
        self.encoding = encoding

    def _files(self, files, exclude):
        to_process = set()
        for path in files:
            if self._is_file(path):
                to_process |= {path}
            elif self._is_dir(path):
                for parent_path, _, file_names in os.walk(path):
                    for file_name in file_names:
                        to_process |= {parent_path + '/' + file_name}
                    break
            else:
                continue
        to_process -= set(exclude)
        return list(to_process)

    def _is_file(self, path):
        return os.path.isfile(path)

    def _is_dir(self, path):
        return os.path.isdir(path)

    def _write(self):
        with open(self.target, 'w', encoding=self.encoding) as t:
            for file in self.files:
                with open(file, 'r', encoding=self.encoding) as f:
                    lines = f.readlines()
                    for line in lines:
                        t.write(line)

    def main(self):
        self._write()

if __name__ == "__main__":
    mg = MergeFiles()
    mg.main()
