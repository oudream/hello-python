// UseMFC.h : main header file for the USEMFC DLL
//

#if !defined(AFX_USEMFC_H__E2246445_3B21_4C18_9FFB_C8622866F6FA__INCLUDED_)
#define AFX_USEMFC_H__E2246445_3B21_4C18_9FFB_C8622866F6FA__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CUseMFCApp
// See UseMFC.cpp for the implementation of this class
//

class CUseMFCApp : public CWinApp
{
public:
	CUseMFCApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CUseMFCApp)
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CUseMFCApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_USEMFC_H__E2246445_3B21_4C18_9FFB_C8622866F6FA__INCLUDED_)
