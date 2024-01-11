from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
    # python中Assert是较为常用的调试工具
    '''
    1. Assert可以简单的理解为程序员的debug工具，
    正式的代码中应该使用raise来检查用户输入是否正确。
    2. 另外不用assert 作为检查输入参数合法性的原因还在于，对于.pyo格式的版本中是不对assert进行编译的。
    python文件的格式除了.py 还有.pyc/.pyo，后两者需要经过编译在运行，
    其中.pyo是经过优化后编译的二进制文件，可以增加程序的稳定性，隐藏源码。
    编译方法：
    python -O -m py_complie yourPythonFile.py
    3. 另外在不进行优化编译的时候 __debug__命令也默认为True，与assert相似，
    使用if __debug__作为判断可以提高编程效率。
    '''


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'