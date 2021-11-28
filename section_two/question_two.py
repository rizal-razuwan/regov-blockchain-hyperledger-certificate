from .question_one import Account


class DevAccount(Account):
    def __init__(self,id, name, balance):
      self._id = id
      self._name = name
      self._balance = balance

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def transfer_other_account(self, amount):
        amount = self._balance
        return amount
