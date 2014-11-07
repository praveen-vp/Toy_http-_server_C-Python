

#include <stdio.h>
#include <string.h>

int main()
{
	char a[12] = "";

	char b[10] = "dss";
	char c[10] = "dss";
	printf("%d\n",strcmp(a,a));
	printf("%d\n",strcmp(b,c));
	printf("%d\n",strcmp(a,""));
	return 0;
}

