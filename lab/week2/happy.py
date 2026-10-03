def print_happy(name:str) -> None:
    print("안녕하세요")
    print(name+"님의 생일을 축하합니다")
    return None

def test_print_happy() :
    print_happy("윤완")
    print_happy("김민재")
    print_happy("송영준")
    print_happy("임정아")

def test_print_happy2() :
    names = ["윤완", "김민재", "송영준", "임정아"]
    for name in names:
         print_happy(name)

def test_print_happy3() :
    print_happy("3.141592")
    print_happy("100")
    print_happy([1,2,3])

if __name__ == "__main__":
#    test_print_happy()
    test_print_happy2()
#    test_print_happy3()


 