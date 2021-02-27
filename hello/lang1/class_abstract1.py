# Abstract Member
from abc import ABC
import json
from typing import Type, Union


class Member:
    def __init__(self, name, pwd, user_type):
        self._login_name = name
        self._login_pwd = pwd
        self._user_type = user_type

    @property
    def user_type(self):
        return self._user_type

    @property
    def login_name(self):
        return self._login_name

    @property
    def login_pwd(self):
        return self._login_pwd

    def __repr__(self):
        return '(UserType: {0._user_type} , LoginName: {0._login_name} , LoginPwd: {0._login_pwd})'.format(self)


class Customer(Member, ABC):
    USER_TYPE = 'Customer'

    def __init__(self, name, pwd):
        Member.__init__(self, name, pwd, Customer.USER_TYPE)


class Seller(Member, ABC):
    USER_TYPE = 'Seller'

    def __init__(self, name, pwd):
        Member.__init__(self, name, pwd, Seller.USER_TYPE)


class Admin(Member, ABC):
    USER_TYPE = 'Admin'

    def __init__(self, name, pwd):
        Member.__init__(self, name, pwd, Admin.USER_TYPE)


class MemberManager(object):
    members = {
        '69000000': Customer('69000000', 'qwer1234'),
        '69200009': Seller('69200009', 'qwer1234'),
        'admin': Admin('admin', '123456'),
    }

    @staticmethod
    def get_customer(name=''):
        if name:
            return MemberManager.members[name]
        else:
            for v in MemberManager.members.values():
                if v.USER_TYPE == Customer.USER_TYPE:
                    return v

    @staticmethod
    def add_member(member: Member):
        """
        Args:
            member _chunk_pattern: Member

        Returns:

        """
        MemberManager.members[member.login_name] = member

    @staticmethod
    def report_all():
        # return json.dumps(MemberManager.members)
        r = [str(m) for m in MemberManager.members.values()]
        print(' | '.join(r))


def hello1():
    members = {
        '69000000': Customer('69000000', 'qwer1234'),
        '69200009': Seller('69200009', 'qwer1234'),
        'admin': Admin('admin', '123456'),
    }
    for m in members.values():
        print(m.USER_TYPE)


def hello2():
    MemberManager.add_member(Admin('admin1', '123456'))
    MemberManager.report_all()


if __name__ == '__main__':
    hello2()
