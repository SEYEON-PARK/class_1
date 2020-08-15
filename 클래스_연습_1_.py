class Happy():
    name="Happy"
    address="301-10"

    def print_name(self):
        print(self.name)#이름 출력
    def print_address(self):
        print(self.address)#주소 출력
a1=Happy()
a1.print_name()
a1.print_address()
a1.name="Good"
a1.print_name()