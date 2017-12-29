#if !defined(AFX_INPUT_H__3B6E7728_B089_41BF_BA1B_DF11467B4994__INCLUDED_)
#define AFX_INPUT_H__3B6E7728_B089_41BF_BA1B_DF11467B4994__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Input.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CInput dialog

class CInput : public CDialog
{
// Construction
public:
	CInput(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CInput)
	enum { IDD = IDD_DIALOG1 };
	CString	m_input;
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CInput)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CInput)
		// NOTE: the ClassWizard will add member functions here
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_INPUT_H__3B6E7728_B089_41BF_BA1B_DF11467B4994__INCLUDED_)
