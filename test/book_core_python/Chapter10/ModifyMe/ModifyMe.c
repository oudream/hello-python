#include <windows.h>
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
		LPSTR lpCmdLine, int nCmdShow)
{
	int a = 0;
	int b = 1;
	if ( a != b )
	{
		MessageBox(NULL, "Bad Python", "Python", MB_OK);
	}
	else
	{
		MessageBox(NULL, "Good Python", "Python", MB_OK);
	}
}
