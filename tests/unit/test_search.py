import unittest
from collections import namedtuple

import mock

import resu

# Example classes and instances

class Parent(object):
    pass

class Child1(Parent):
    name = 'child1'

class Child2(Parent):
    name = 'child2'

class InstanceTracker(namedtuple('InstanceTacker', ['name'])):

    instances = []

    def __init__(self, **kwargs):
        InstanceTracker.instances.append(self)

InstanceTracker(name='instance1')

class TestSearch(unittest.TestCase):

    def test_available_subclasses(self):
        children = resu.available(Parent)
        assert 'child1' in children
        assert 'child2' in children

    def test_available_instances(self):
        instances = resu.available(InstanceTracker)
        assert 'instance1' in instances

    def test_find_subclasses(self):
        child = resu.find(Parent, 'child1')
        self.assertEquals(child, Child1)

    def test_find_instances(self):
        children = resu.find(InstanceTracker, 'instance1')
        assert 'instance1' in children
