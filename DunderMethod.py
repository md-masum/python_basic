class SuperList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __getitems__(self, index):
        return super().__getitem__(index)
    
    def __setitems__(self, index, value):
        super().__setitem__(index, value)

SuperList1 = SuperList([1, 2, 3, 4, 5])
print(SuperList1)
SuperList1.append(6)
print(SuperList1)
print(SuperList1.__getitems__(0))
SuperList1.__setitems__(0, 100)
print(SuperList1)
    
