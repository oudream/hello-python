#include <Python.h>
int main()
{
	Py_Initialize();				/* Python解释器初始化 */
	PyRun_SimpleString("print 'hi,python!'");	/* 运行字符串 */
	Py_Finalize();					/* 结束Python解释器，释放资源 */
	return 0;
}

