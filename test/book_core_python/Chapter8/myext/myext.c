#include <python.h>
#include <windows.h>
/* 定义C扩展中的函数 */
PyObject *show(PyObject *self, PyObject *args)
{
	char *message;
	const char *title = NULL;
	HWND hwnd = NULL;
	int r;
	/* 使用PyArg_ParseTuple处理参数 */
	if (!PyArg_ParseTuple(args, "iss", &hwnd, &message, &title))
		return NULL;
	r = MessageBox(hwnd,message, title, MB_OK);
	return Py_BuildValue("i", r);
}
/* 模块的方法列表 */
static PyMethodDef myextMethods[] = 
{
	{"show", show, METH_VARARGS,"show a messagebox"},
	{NULL,NULL}
};
/* 模块的初始化函数 */
PyMODINIT_FUNC initmyext()
{
	PyObject *mod;
	/* 使用Py_InitModule初始化模块*/
	mod = Py_InitModule("myext",myextMethods);
}
