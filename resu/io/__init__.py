'''
Resu abstracts IO to read and write operations to allow developers to add IO
providers to support IO for databases or respond to API calls on a website
without changing any code in Resu.
'''
from resu.io.provider import Provider
from resu.io.file import File
from resu.io.package_data import PackageData
