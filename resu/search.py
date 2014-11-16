def available(class_, id_attr='name'):
    ret = list()
    for subclass in class_.__subclasses__():
        if id_attr in subclass.__dict__:
            ret.append(subclass.__dict__[id_attr])
    return ret

def find(class_, target, id_attr='name'):
    for instance in class_.__dict__.get('instances', []):
        if instance._asdict().get(id_attr, '') == target:
            return instance
    for subclass in class_.__subclasses__():
        if subclass.__dict__[id_attr] == target:
            return subclass
