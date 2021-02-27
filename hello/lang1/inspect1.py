import datetime
import inspect
import re
from pprint import pprint


class Parent(object):
    __priv = 'private'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, self.name)

    def doNothing(self):
        pass


class Child(Parent):
    # prefix for "private" fields
    __rePrivate = re.compile('^_(Child|Parent)__')
    # used when setting dynamic property values
    __reBleh = re.compile('\Wbleh$')

    @property
    def reBleh(self):
        return self.__reBleh

    def __init__(self, name, *args):
        super(Child, self).__init__(name)
        self.args = args

    def __dir__(self):
        myDir = filter(
            # filter out private fields
            lambda p: not self.__rePrivate.match(p),
            list(set( \
                sum([dir(base) for base in type(self).__bases__], []) \
                + type(self).__dict__.keys() \
                + self.__dict__.keys() \
                )))
        return myDir + map(
            # dynamic properties
            lambda p: p + '_bleh',
            filter(
                # don't add dynamic properties for methods and other special properties
                lambda p: (p[:2] != '__' or p[-2:] != '__') and not callable(getattr(self, p)),
                myDir))

    def __getattr__(self, name):
        if name[-5:] == '_bleh':
            # dynamic '_bleh' properties
            return str(getattr(self, name[:-5])) + ' bleh'
        if hasattr(super(Child, chld), '__getattr__'):
            return super(Child, self).__getattr__(name)
        raise AttributeError("'%s' object has no attribute '%s'" % (type(self).__name__, name))

    def __setattr__(self, name, value):
        if name[-5:] == '_bleh':
            # skip backing properties that are methods
            if not (hasattr(self, name[:-5]) and callable(getattr(self, name[:-5]))):
                setattr(self, name[:-5], self.reBleh.sub('', value))
        elif hasattr(super(Child, self), '__setattr__'):
            super(Child, self).__setattr__(name, value)
        elif hasattr(self, '__dict__'):
            self.__dict__[name] = value

    def __repr__(self):
        return '%s(%s, %s)' % (type(self).__name__, self.name, str(self.args).strip('[]()'))

    def doStuff(self):
        return (1 + 1.0 / 1e6) ** 1e6


class Member:
    def __init__(self, user_type, name, pwd, nick_name):
        self._user_type = user_type
        self._login_name = name
        self._login_pwd = pwd
        self._nick_name = nick_name

    @property
    def user_type(self):
        return self._user_type

    @property
    def login_name(self):
        return self._login_name

    @property
    def login_pwd(self):
        return self._login_pwd

    @property
    def nick_name(self):
        return self._nick_name

    def get_full_name(self):
        return self._login_name + self._login_pwd

    def get_full_id(self):
        return self._nick_name + self._login_pwd

    # def __repr__(self):
    #     return 'UserType: {0._user_type} | LoginName: {0._login_name} | LoginPwd: {0._login_pwd}'.format(self)


def get_properties_name(obj):
    attrs = inspect.classify_class_attrs(type(obj))
    return [a.name for a in attrs if a.kind == 'property']


def get_properties_value(obj):
    attrs = inspect.classify_class_attrs(type(obj))
    return [getattr(obj, a.name) for a in attrs if a.kind == 'property']


def get_properties_string(obj):
    attrs = inspect.classify_class_attrs(type(obj))
    return [str(getattr(obj, a.name)) for a in attrs if a.kind == 'property']


def get_properties_string2(obj):
    attrs = inspect.classify_class_attrs(type(obj))
    return ['%s: %s' % (a.name, str(getattr(obj, a.name))) for a in attrs if a.kind == 'property']


def get_methods_name(obj):
    attrs = inspect.classify_class_attrs(type(obj))
    return [a.name for a in attrs if a.kind == 'method']


def get_methods_value(obj, *arg):
    attrs = inspect.classify_class_attrs(type(obj))
    return [getattr(obj, a.name)(*arg) for a in attrs if a.kind == 'method']


def get_methods_string(obj, *arg):
    attrs = inspect.classify_class_attrs(type(obj))
    return [str(getattr(obj, a.name)(*arg)) for a in attrs if a.kind == 'method']


def get_methods_string2(obj, *arg):
    attrs = inspect.classify_class_attrs(type(obj))
    return ['%s: %s' % (a.name, str(getattr(obj, a.name)(*arg))) for a in attrs if a.kind == 'method']


def report_properties(obj):
    """
    return ' store_name: {0.store_name} | store_age: {0.store_age}' \
           ' | store_pv: {0.store_pv} | store_follow_state: {0.store_follow_state}' \
           ' | store_friends_list_text: {0.store_friends_list_text}' \
           ' | store_guest_list_text: {0.store_guest_list_text}' \
        .format(self)

    """
    attrs = inspect.classify_class_attrs(type(obj))
    s = ['%s: {0.%s}' % (a.name, a.name) for a in attrs if a.kind == 'property']
    return '{' + ','.join(s).format(obj) + '}'


def report_gets(obj):
    """
    return ' store_name: {0.store_name} | store_age: {0.store_age}' \
           ' | store_pv: {0.store_pv} | store_follow_state: {0.store_follow_state}' \
           ' | store_friends_list_text: {0.store_friends_list_text}' \
           ' | store_guest_list_text: {0.store_guest_list_text}' \
        .format(self)

    """
    attrs = inspect.classify_class_attrs(type(obj))
    # for a in attrs:
    #     if a.kind == 'method' and a.name.startswith('get_'):
    #         method = getattr(obj, a.name)
    #         s = method()
    #         print(s)
    s = ['%s: %s' % (a.name, getattr(obj, a.name)()) for a in attrs if a.kind == 'method' and a.name.startswith('get_')]
    return '{' + ','.join(s) + '}'


def report_gets2(obj, excludes=[]):
    """

    Args:
        obj:
        excludes:

    Returns:


    """
    attrs = inspect.classify_class_attrs(type(obj))
    s = ['%s: %s' % (a.name, getattr(obj, a.name)()) for a in attrs if
         a.kind == 'method' and a.name.startswith('get_') and (a.name not in excludes)]
    return '{' + ','.join(s) + '}'


def hello1():
    m = Member(1, 2, 3, datetime.datetime.now())
    # attrs = inspect.classify_class_attrs(Member)
    # print(attrs)
    # for attr in attrs:
    #     if attr.kind == 'property':
    #         print('--------------', str(getattr(m, attr.name)))

    print(get_properties_string(m))

    #
    # par = Parent('par')
    # par.parent = True
    # dir(par)
    # # ['_Parent__priv', '__class__', ..., 'doNothing', 'name', 'parent']
    # inspect.getmembers(par)
    # # [('_Parent__priv', 'private'), ('__class__', <class '__main__.Parent'>), ..., ('doNothing', <bound method Parent.doNothing of <__main__.Parent object at 0x100777650>>), ('name', 'par'), ('parent', True)]
    #
    # chld = Child('chld', 0, 'I', 'two')
    # chld.own = "chld's own"
    # dir(chld)
    # # ['__class__', ..., 'args', 'args_bleh', 'doNothing', 'doStuff', 'name', 'name_bleh', 'own', 'own_bleh', 'reBleh', 'reBleh_bleh']
    # inspect.getmembers(chld)
    # # [('__class__', <class '__main__.Child'>), ..., ('args', (0, 'I', 'two')), ('args_bleh', "(0, 'I', 'two') bleh"), ('doNothing', <bound method Child.doNothing of Child(chld, 0, 'I', 'two')>), ('doStuff', <bound method Child.doStuff of Child(chld, 0, 'I', 'two')>), ('name', 'chld'), ('name_bleh', 'chld bleh'), ('own', "chld's own"), ('own_bleh', "chld's own bleh"), ('reBleh', <_sre.SRE_Pattern object at 0x10067bd20>), ('reBleh_bleh', '<_sre.SRE_Pattern object at 0x10067bd20> bleh')]


if __name__ == '__main__':
    hello1()
    # m = Member(1, 2, 3, 4)
    # print(str(m.user_type))
