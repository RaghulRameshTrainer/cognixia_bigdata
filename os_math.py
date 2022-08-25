Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data=['Chennai','Bangalore']
>>> len(data)
2
>>> students=['Raja','Priya','Arun']
>>> students[0]
'Raja'
>>> students[1]
'Priya'
>>> students[2]
'Arun'
>>> import sys
>>> print(dir(sys))
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']



>>> import os
>>> os.getcwd()
'C:\\Users\\RaghulRamesh\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.chdir(r'C:\Users\RaghulRamesh\OneDrive\Desktop\cognixia')
>>> os.getcwd()
'C:\\Users\\RaghulRamesh\\OneDrive\\Desktop\\cognixia'
>>> os.mkdir('Thursday')
>>> os.rmdir('Thursday')
>>> os.mkdir('Thursday')
>>> os.rmdir('Thursday')
>>> os.mkdir('Thursday')
>>> os.mkdir('Friday')
>>> os.mkdir(r'Tech\Bigdata\Hadoop\Spark\
')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    os.mkdir(r'Tech\Bigdata\Hadoop\Spark\
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'Tech\\Bigdata\\Hadoop\\Spark\\\n'
>>> os.mkdir(r'Tech\Bigdata\Hadoop\Spark\Kafka')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.mkdir(r'Tech\Bigdata\Hadoop\Spark\Kafka')
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'Tech\\Bigdata\\Hadoop\\Spark\\Kafka'
>>> os.makedirs(r'Tech\Bigdata\Hadoop\Spark\Kafka')
>>> os.removedirs('Tech')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    os.removedirs('Tech')
  File "C:\Users\RaghulRamesh\AppData\Local\Programs\Python\Python38\lib\os.py", line 241, in removedirs
    rmdir(name)
OSError: [WinError 145] The directory is not empty: 'Tech'
>>> os.removedirs(r'Tech\Bigdata\Hadoop\Spark\Kafka')
>>> os.removedirs(r'Tech\Bigdata\Hadoop\Spark')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.removedirs(r'Tech\Bigdata\Hadoop\Spark')
  File "C:\Users\RaghulRamesh\AppData\Local\Programs\Python\Python38\lib\os.py", line 241, in removedirs
    rmdir(name)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'Tech\\Bigdata\\Hadoop\\Spark'
>>> os.getcws()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    os.getcws()
AttributeError: module 'os' has no attribute 'getcws'
>>> os.getcwd()
'C:\\Users\\RaghulRamesh\\OneDrive\\Desktop\\cognixia'
>>> os.rmdir('Thursday')
>>> os.rmdir('Friday')
>>> with open('customer.txt','w') as fo:
	pass

>>> os.rename('customer.txt','user.txt')
>>> os.remove('user.txt')
>>> import shutil
>>> with open('customer.txt','w') as fo:
	pass

>>> shutil.copy('customer.txt','users.txt')
'users.txt'
>>> os.chmod('customer.txt',777)
>>> os.chmod('customer.txt',741)
>>> os.chmod('customer.txt',751)
>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sqrt(100)
10.0
>>> math.prod(10,10)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    math.prod(10,10)
TypeError: prod() takes exactly 1 positional argument (2 given)
>>> math.prod([10,10])
100
>>> math.factorial(5)
120
>>> math.factorial(50)
30414093201713378043612608166064768844377641568960512000000000000
>>> math.factorial(500)
1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663535984174430480128938313896881639487469658817504506926365338175055478128640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> math.sin(0)
0.0
>>> math.cos(90)
-0.4480736161291701
>>> math.sin(90)
0.8939966636005579
>>> math.tan(45)
1.6197751905438615
>>> math.log2(32)
5.0
>>> math.log10(100)
2.0
>>> math.log(1000,6)
3.855291626815406
>>> math.log(1000,10)
2.9999999999999996
>>> round(99.65)
100
>>> math.ceil(99.1)
100
>>> math.floor(99.1)
99
>>> 