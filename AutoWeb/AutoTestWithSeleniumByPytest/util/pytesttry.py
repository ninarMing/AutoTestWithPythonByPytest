import pytest


@pytest.fixture(scope="class")
def start_and_end():
    print("开始测试class")
    yield
    print("结束测试class")

class TestTry:
    def teardown_class(self):
        print("teardown_class结束")

    @pytest.fixture(scope="function")
    def sure_login(self):
        print("sure_login装饰器")
        yield
        print("这个test_run_more结束")

    @pytest.mark.run(order=1)
   #@pytest.mark.flaky(reruns=2,reruns_delay=2)
    @pytest.mark.parametrize("user,pwd", [("a","12")])
    def test_date_1(self,user,pwd,sure_login,start_and_end):
        print("******test_date_1**********")
        pytest.assume(1==1)
        print("test_date_1结束")

    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_date_2(self,start_and_end):
        print("*****test_date_2_*****")
        pytest.assume(1 == 1)
        print("test_date_2结束")

    @pytest.mark.run(order=-1)
    def test_date_3(self):
        pytest.assume(1 ==1)
        print("是否是最后一个执行")


if __name__ == '__main__':
    pytest.main(["-vs","util/pytesttry.py"])