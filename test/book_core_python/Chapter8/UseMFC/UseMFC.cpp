// UseMFC.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "UseMFC.h"
#include "Input.h"
#include <Python.h>
#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

//
//	Note!
//
//		If this DLL is dynamically linked against the MFC
//		DLLs, any functions exported from this DLL which
//		call into MFC must have the AFX_MANAGE_STATE macro
//		added at the very beginning of the function.
//
//		For example:
//
//		extern "C" BOOL PASCAL EXPORT ExportedFunction()
//		{
//			AFX_MANAGE_STATE(AfxGetStaticModuleState());
//			// normal function body here
//		}
//
//		It is very important that this macro appear in each
//		function, prior to any calls into MFC.  This means that
//		it must appear as the first statement within the 
//		function, even before any object variable declarations
//		as their constructors may generate calls into the MFC
//		DLL.
//
//		Please see MFC Technical Notes 33 and 58 for additional
//		details.
//

/////////////////////////////////////////////////////////////////////////////
// CUseMFCApp

BEGIN_MESSAGE_MAP(CUseMFCApp, CWinApp)
	//{{AFX_MSG_MAP(CUseMFCApp)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CUseMFCApp construction

CUseMFCApp::CUseMFCApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

/////////////////////////////////////////////////////////////////////////////
// The one and only CUseMFCApp object

CUseMFCApp theApp;
// 定义扩展模块中的函数
PyObject *show(PyObject *self, PyObject *args)
{
	AFX_MANAGE_STATE(AfxGetStaticModuleState());
	CInput dia;
	dia.DoModal();	
	return Py_BuildValue("s", dia.m_input);
}
// 模块的方法列表 
static PyMethodDef UseMFCMethods[] = 
{
	{"show", show, METH_VARARGS,"show a messagebox"},
	{NULL,NULL}
};
// 模块的初始化函数
extern "C" void initUseMFC()
{
	PyObject *mod;
	mod = Py_InitModule("UseMFC",UseMFCMethods);
}