#include <string.h>
#include <iostream.h>
#include <boost/python.hpp>
#include <Python.h>
// 告诉编译器链接到boost_python.lib库
#pragma comment(lib, "boost_python.lib")
using namespace std;	
using namespace boost::python;
int main(int argc, char* argv[])
{
	int size, i;
	list mylist, rel;
	handle<> module;
	char *funcname1 = "sum";
	char *funcname2 = "strsplit";
	cout << "-==使用Boost.Python在C++中嵌入Python==-" << endl;
	// Python解释器初始化
	Py_Initialize();
	if(!Py_IsInitialized())   
	{   
		cout <<"初始化失败!"<< endl;
		return -1;   
	}
	// 导入Python模块
	module = handle<> (PyImport_ImportModule("pytest"));
	cout << "使用Python中的sum函数求解下列数之和：" << endl;
	for(i = 1; i < 6; i++ )
	{
		cout << i << "\t";
		mylist.append(i);
	}
	cout << endl;
	// 调用Python中的sum函数
	call_method<void>(module.get(), funcname1, mylist);
	cout << "使用Python中的函数分割以下字符串:" << endl;
	cout << "this is an example" << endl;
	// 调用Python中的strsplit函数并获得返回值
	rel = call_method<list>(module.get(), funcname2, "this is an example", " ");
	// 输出返回值
	size = call_method<int>(rel.ptr(),"__len__");
	cout << "结果如下所示:" << endl;
	for(i = 0; i < size; i ++)
	{
		cout << call_method<char *>(rel.ptr(),"__getitem__",i) << endl;
	}
	// 结束Python解释器释放资源
	Py_Finalize();
	return 0;
}


