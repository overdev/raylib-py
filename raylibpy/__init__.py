import sys
import os
import platform
import ctypes
import itertools
from ctypes import CDLL, wintypes

__all__ = [
    '_rl',
    'CDLLEx',
]

# region LIBRARY LOADING

# region CDLLEX

if sys.platform == 'win32':
    DONT_RESOLVE_DLL_REFERENCES = 0x00000001
    LOAD_LIBRARY_AS_DATAFILE = 0x00000002
    LOAD_WITH_ALTERED_SEARCH_PATH = 0x00000008
    LOAD_IGNORE_CODE_AUTHZ_LEVEL = 0x00000010  # NT 6.1
    LOAD_LIBRARY_AS_IMAGE_RESOURCE = 0x00000020  # NT 6.0
    LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 0x00000040  # NT 6.0

    # These cannot be combined with LOAD_WITH_ALTERED_SEARCH_PATH.
    # Install update KB2533623 for NT 6.0 & 6.1.
    LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 0x00000100
    LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 0x00000200
    LOAD_LIBRARY_SEARCH_USER_DIRS = 0x00000400
    LOAD_LIBRARY_SEARCH_SYSTEM32 = 0x00000800
    LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 0x00001000

    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

    def check_bool(result, func, args):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return args

    kernel32.LoadLibraryExW.errcheck = check_bool
    kernel32.LoadLibraryExW.restype = wintypes.HMODULE
    kernel32.LoadLibraryExW.argtypes = (wintypes.LPCWSTR,
                                        wintypes.HANDLE,
                                        wintypes.DWORD)

    class WinDLLEx(ctypes.WinDLL):
        def __init__(self, name, mode=0, handle=None,
                     use_errno=False, use_last_error=True):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(WinDLLEx, self).__init__(name, mode, handle,
                                           use_errno, use_last_error)

    class CDLLEx(ctypes.CDLL):
        def __init__(self, name, mode=0, handle=None,
                     use_errno=True, use_last_error=False):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(CDLLEx, self).__init__(name, mode, handle,
                                         use_errno, use_last_error)


# endregion (cdllex)


def raylib_so_paths():
    '''Return a list of full paths to try and load the shared library from
    '''
    def so_paths():
        main_mod = sys.modules['__main__']
        running_from_repl = '__file__' not in dir(main_mod)
        return filter(None, [
            os.environ.get('RAYLIB_BIN_PATH') if 'RAYLIB_BIN_PATH' in os.environ else None,
            os.path.join(os.path.dirname(__file__), 'bin'),
            os.path.join(os.path.dirname(main_mod.__file__), 'bin') if not running_from_repl else None,
        ])
    def so_names():
        lib_filenames = {
            'win32': ['raylib.dll', 'libraylib.dll', 'libraylib_shared.dll'],
            'linux': ['libraylib.so.3.7.0', 'libraylib.so.370', 'libraylib.so'],
            'darwin': ['libraylib.3.7.0.dylib', 'libraylib.dylib.370', 'libraylib.dylib'],
        }
        return filter(None, [
            os.environ.get('RAYLIB_BIN_FILENAME'),
            *lib_filenames[sys.platform]
        ])
    def join_paths(paths):
        return os.path.join(*paths)

    paths = itertools.product(so_paths(), so_names())
    return list(map(join_paths, paths))

def find_raylib_so(raylib_paths):
    '''Given a list of possible paths, finds the first valid one.
    If no paths are valid, throws a RuntimeError.
    '''
    valid_paths = list(filter(lambda path: os.path.isfile(path), raylib_paths))
    if len(valid_paths):
        return valid_paths[0]

    raise RuntimeError((
        'Cannot find Raylib shared object in these search paths:\n'
        '{}'
    ).format('\n'.join(raylib_paths)))



_lib_platform = sys.platform

if _lib_platform == 'win32':
    _bitness = platform.architecture()[0]
else:
    _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'


_lib_fname_abspath = find_raylib_so(raylib_so_paths())
_lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_fname_abspath))

print(
    """Library loading info:
    platform: {}
    bitness: {}
    absolute path: {}
    exists: {}
    is file: {}
    """.format(
        _lib_platform,
        _bitness,
        _lib_fname_abspath,
        'yes' if os.path.exists(_lib_fname_abspath) else 'no',
        'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
    )
)

_rl = None
if _lib_platform == 'win32':
    try:
        _rl = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
    except OSError as err:
        print(f"Unable to load {_lib_fname[_lib_platform]}.\n\tCause: {err.winerror}")
        _rl = None
else:
    _rl = CDLL(_lib_fname_abspath)

if _rl is None:
    print("Failed to load shared library.")
    exit()
else:
    print("Shared library loaded succesfully.", _rl)
