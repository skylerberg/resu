from resu.loaders.loader import Loader
from resu.loaders.file_loader import FileLoader
from resu.loaders.package_data_loader import PackageDataLoader, PackageDataSource

def load(source):
    for subclass in Loader.__subclasses__():
        if isinstance(source, subclass.source_type):
            return subclass().load(source)
