import os.path
from multiprocessing import Pool
import time

BUFFER_SIZE_LINES = 10000  # global line buffer size across threads


def process_file(name):
    buf = ""  # Temp buffer variable to accumulate the concatenated lines
    buf_line_count = 0  # buffer record count as we progress through the file.
    with open(name, 'r', encoding='utf-8') as inp:
        with open(name+"_temp", "w", encoding='utf-8') as out:
            for line in inp:
                buf_line_count += 1
                buf += line.strip()
                if buf_line_count >= BUFFER_SIZE_LINES:
                    buf.replace('//#@/','\n')
                    out.write(buf)
                    buf = ""
                    buf_line_count = 0
            if buf != "":
                out.write(buf)


def process_files_parallel(dirname, names):
    # Process each file in parallel via Pool.map()
    pool = Pool(maxtasksperchild=10)  # control the parallel thread based on need.
    pool.map(process_file, [os.path.join(dirname, name) for name in names])


def process_files(dirname, names):
    for name in names:
        process_file(os.path.join(dirname, name))


if __name__ == '__main__':

    for path, dirs, files in os.walk("input/", topdown=True):
        start = time.time()
        process_files(path, files)
        print("process_files()", time.time() - start)

        start = time.time()
        process_files_parallel(path, files)
        print("process_files_parallel()", time.time() - start)
