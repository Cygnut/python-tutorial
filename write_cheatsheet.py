import os
import sys
import logging
import datetime

_logger = logging.getLogger(__name__)

def init_logging(fmt=None):
    """Initialise logging for the application

    Args:
        fmt (str, optional): An optional logging format. Defaults to None.
    """
    formatter = logging.Formatter(fmt or '%(asctime)s | %(name)25s | %(levelname)5s | %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)

def time_this(func):
    """A decorator for profiling specific function calls

    Args:
        func (function): The function to be profiled
    """
    def decorator(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        _logger.debug(f"{func.__qualname__} took {datetime.datetime.now() - start}")
        return result
    return decorator

class _SectionFile:
    """Represents a single section file
    """

    def __init__(self, filepath):
        self.filepath = filepath

        leaf = os.path.splitext(os.path.basename(filepath))[0]
        number, self.name = leaf.split('-', 1)
        self.number = float(number)

class CheatsheetWriter:
    """Combines all sections into a single cheatsheet file
    """

    # Constants
    _SECTIONS_DIR = 'sections'
    _CHEATSHEET_MODULE_NAME = 'cheatsheet'
    _CHEATSHEET_FILENAME = f"{_CHEATSHEET_MODULE_NAME}.py"

    def __init__(self, current_dir=None):
        self._current_dir = current_dir or os.path.dirname(os.path.realpath(__file__))
        self._sections_path = os.path.join(self._current_dir, self._SECTIONS_DIR)
        self._cheatsheet_path = os.path.join(self._current_dir, self._CHEATSHEET_FILENAME)

    @time_this
    def __find_sections(self):
        """Find all sections under the sections directory

        Returns:
            list: All detected section files
        """
        section_files = os.listdir(self._sections_path)

        sections = []
        for filename in section_files:
            filepath = os.path.join(self._sections_path, filename)
            if not os.path.isfile(filepath):
                continue

            _, extension = os.path.splitext(filename)

            if '.py' != extension:
                continue

            _logger.debug(f"Found section {filepath}")
            sections.append(_SectionFile(filepath))

        # Sort by section number
        sections.sort(key=lambda s: s.number)

        return sections

    @time_this
    def __write_cheatsheet(self, sections):
        """Write a file containing all previously found sections

        Args:
            sections (list): The filepaths of all detected sections
        """
        spacer = os.linesep * 2
        mapped_sections = []
        for section in sections:
            with open(section.filepath) as f:
                _logger.debug(f"Reading file {section.filepath}")
                content = spacer.join([
                    f"\"\"\" Section {section.number} - {section.name} \"\"\"",
                    f.read()
                ])
                mapped_sections.append(content)

        cheatsheet_text = spacer.join(mapped_sections)

        with open(self._cheatsheet_path, 'w') as f:
            f.write(cheatsheet_text)

        _logger.info(f"Written to {self._cheatsheet_path}")

    @time_this
    def __validate_cheatsheet(self, name, location):
        """Note that the following is very unsafe, don't attempt to mimic this..

        Args:
            name (str): The name of the module
            location (str): The location of the python file
        """
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, location)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    @time_this
    def run(self):
        """Write a validated cheatsheet
        """
        sections = self.__find_sections()

        self.__write_cheatsheet(sections)

        self.__validate_cheatsheet(self._CHEATSHEET_MODULE_NAME, self._cheatsheet_path)

if __name__ == '__main__':
    try:
        init_logging()
        CheatsheetWriter().run()
    except Exception as e:
        _logger.exception(e)
