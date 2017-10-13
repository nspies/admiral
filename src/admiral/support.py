import math
import os

class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True

    
class JobmanagerException(Exception):
    pass

class JobSubmissionException(JobmanagerException):
    pass


def path_with_default(path, default=None):
    if path is None:
        if default is None:
            default = os.getcwd()
        path = default
    return path


def get_chunks(seq, chunk_size):
    return (seq[pos:pos + chunk_size] for pos in range(0, len(seq), chunk_size))

def get_nchunks(seq, nchunks):
    chunk_size = int(math.ceil(len(seq)/nchunks))
    yield from get_chunks(seq, chunk_size)