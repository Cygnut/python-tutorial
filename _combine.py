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

class SectionCombiner:
    """Combines all sections into one file
    """

    # Various constants..
    _SECTIONS_DIR = 'sections'
    _COMBINED_MODULE_NAME = 'combined'
    _COMBINED_FILENAME = f"{_COMBINED_MODULE_NAME}.py"

    def __init__(self, current_dir=None):
        self._current_dir = current_dir or os.path.dirname(os.path.realpath(__file__))

    @time_this
    def __find_sections(self):
        """Find all sections under the sections directory

        Returns:
            list: All detected section files
        """
        sections_path = os.path.join(self._current_dir, self._SECTIONS_DIR)

        section_files = os.listdir(sections_path)

        sections = []
        for filename in section_files:
            filepath = os.path.join(sections_path, filename)
            if not os.path.isfile(filepath):
                continue

            (leaf, extension) = os.path.splitext(filename)

            if '.py' != extension:
                continue

            _logger.debug(f"Found section {filepath}")
            sections.append(_SectionFile(filepath))

        # Sort by section number
        sections.sort(key=lambda s: s.number)

        return sections

    @time_this
    def __write_combined_sections_file(self, sections):
        """Write a file containing all previously found sections

        Args:
            sections (list): The filepaths of all detected sections
        """
        newline = (os.linesep * 2)
        combined = []
        for section in sections:
            with open(section.filepath) as f:
                content = newline.join([
                    f"\"\"\" Section {section.number} - {section.name} \"\"\"",
                    f.read()
                ])
                combined.append(content)

        combined_text = newline.join(combined)

        combined_path = os.path.join(self._current_dir, self._COMBINED_FILENAME)
        with open(combined_path, 'w') as f:
            f.write(combined_text)

        _logger.info(f"Written to {combined_path}")
        return combined_path

    @time_this
    def __run_and_check_python_file(self, name, location):
        """Note that the following is very unsafe, don't attempt to mimic this..

        Args:
            name (str): The name of the module
            location (str): The location of the python file
        """
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, location)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    def run(self):
        """Combine all files into one and validate it
        """
        sections = self.__find_sections()

        combined_path = self.__write_combined_sections_file(sections)

        self.__run_and_check_python_file(self._COMBINED_MODULE_NAME, combined_path)

if __name__ == '__main__':
    try:
        init_logging()
        SectionCombiner().run()
    except Exception as e:
        _logger.exception(e)