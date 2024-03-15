# 주입할 의존성을 정의
class Dependency:
    def __init__(self):
        pass
  
    def dependency(self):
        print('Dependency.__init__ called') # 출력: Dependency.__init__ called

# MyClass에 의존성 주입
class MyClass:
    def __init__(self, dependency: Dependency):
        self.dependency = dependency

# 의존성 주입 확인
dependency_instance = Dependency()
my_instance = MyClass(dependency_instance)
print(my_instance.dependency)  # 출력: <__main__.Dependency object at 0x7f37bf05b490>
my_instance.dependency()  # TypeError: 'Dependency' object is not callable
