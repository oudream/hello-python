#include <stdio.h>
#include <Python.h>
int main(int argc, char* argv[])
{	
	PyObject *modulename, *module, *dic, *func, *args, *rel, *list;
	char *funcname1 = "sum";
	char *funcname2 = "strsplit";
	int i;
	Py_ssize_t s;
	printf("-==在C中嵌入Python==-\n");
	/* Python解释器的初始化*/
	Py_Initialize();                      
	if(!Py_IsInitialized())   
	{   
		printf("初始化失败!");   
		return -1;   
	}
	/* 导入Python模块,并检验是否正确导入 */
	modulename = Py_BuildValue("s", "pytest");  
	module = PyImport_Import(modulename);   
	if(!module)   
	{   
		printf("导入pytest失败!");   
		return  -1;   		
	} 
	/* 获得模块中函数并检验其有效性 */
	dic = PyModule_GetDict(module);  
	if(!dic)
	{
		printf("错误!\n");
		return -1;   
	}
	/* 获得sum函数地址并验证 */
	func = PyDict_GetItemString(dic,funcname1);   
	if(!PyCallable_Check(func))   
	{   
		printf("不能找到函数 %s",funcname1);     
		return -1;   
	}
	/* 构建列表 */
	list = PyList_New(5);
	printf("使用Python中的sum函数求解下列数之和\n");
	for (i = 0; i < 5; i++)
	{
		printf("%d\t",i);
		PyList_SetItem(list,i,Py_BuildValue("i",i)); 
	}
	printf("\n");
	/* 构建sum函数的参数元组*/
	args = PyTuple_New(1); 
	PyTuple_SetItem(args,0,list);
	/* 调用sum函数 */
	PyObject_CallObject(func,args); 
	/* 获得strsplit函数地址并验证*/
	func = PyDict_GetItemString(dic,funcname2);   
	if(!PyCallable_Check(func))   
	{   
		printf("不能找到函数 %s",funcname2);     
		return -1;
	}   
	/* 构建strsplit函数的参数元组 */
	args = PyTuple_New(2); 
	printf("使用Python中的函数分割以下字符串:\n");
	printf("this is an example\n");
	PyTuple_SetItem(args,0,Py_BuildValue("s","this is an example"));   
	PyTuple_SetItem(args,1,Py_BuildValue("s"," "));  
	/* 调用strsplit函数并获得返回值 */
	rel = PyObject_CallObject(func, args);   
	s = PyList_Size(rel);
	printf("结果如下所示:\n");
	for ( i = 0; i < s; i ++)
	{
		printf("%s\n",PyString_AsString(PyList_GetItem(rel,i)));
	}
	/* 释放资源 */
	Py_DECREF(list);
	Py_DECREF(args);
	Py_DECREF(module);  
	/* 结束Python解释器 */
	Py_Finalize();			
	printf("按回车键退出程序:\n");
	getchar();   
	return 0;
	
}

