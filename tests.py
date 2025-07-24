from functions.get_file_content import get_file_content


def test():
    
    print(get_file_content("calculator", "main.py"))
    print("\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n")
    print(get_file_content("calculator", "/bin/cat") )
    print("\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py") )

if __name__ == "__main__":
    test()