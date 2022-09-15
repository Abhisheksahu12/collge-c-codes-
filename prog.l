%{
int flag=0;
int flag1=0;
%}
%%
[0-9] {flag=1;}
[+-*/==&&%%<=>=**!=] {flag1=1;}
%%
int main()
{
printf("input anything:");
yylex();
if flag==1{
printf("it is a digit");}
if flag1==1{
printf{"it is an operator"};
}
return 0;
}
