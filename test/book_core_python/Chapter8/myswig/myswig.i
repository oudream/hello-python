%module myswig
%inline %{
extern int show(char *message, char *title);
%}