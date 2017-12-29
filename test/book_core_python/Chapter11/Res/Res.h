// Res.h : main header file for the RES DLL
//

#if !defined(AFX_RES_H__4BC3C93F_A2CB_441B_A189_B1AA57F755FC__INCLUDED_)
#define AFX_RES_H__4BC3C93F_A2CB_441B_A189_B1AA57F755FC__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CResApp
// See Res.cpp for the implementation of this class
//

class CResApp : public CWinApp
{
public:
	CResApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CResApp)
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CResApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_RES_H__4BC3C93F_A2CB_441B_A189_B1AA57F755FC__INCLUDED_)
