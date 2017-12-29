#include <windows.h>
int show(char *message, char *title)
{
	int r;
	r = MessageBox(NULL,message, title, MB_OK);
	return r;
}

