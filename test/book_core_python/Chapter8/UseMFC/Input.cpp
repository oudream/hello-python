// Input.cpp : implementation file
//

#include "stdafx.h"
#include "UseMFC.h"
#include "Input.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CInput dialog


CInput::CInput(CWnd* pParent /*=NULL*/)
	: CDialog(CInput::IDD, pParent)
{
	//{{AFX_DATA_INIT(CInput)
	m_input = _T("");
	//}}AFX_DATA_INIT
}


void CInput::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CInput)
	DDX_Text(pDX, IDC_EDIT1, m_input);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CInput, CDialog)
	//{{AFX_MSG_MAP(CInput)
		// NOTE: the ClassWizard will add message map macros here
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CInput message handlers
