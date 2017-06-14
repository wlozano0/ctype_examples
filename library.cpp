#define DLLIMP     __declspec(dllexport)

DLLIMP int * f1(int *a1){
    //printf("*a1 %d\n", *a1);

   *a1 = *a1 + 10;
   *(a1+1) = *(a1+1) + 10;

   return a1;
}


struct struct1{
    int a[3];
    int b[3];
};

DLLIMP struct struct1 * f2(struct struct1 *s1){
    //printf("s1->a[0] %d\n", s1->a[0]);
    //printf("s1->b[0] %d\n", s1->b[0]);

    s1->a[0] = s1->a[0] + 1;
    s1->b[0] = s1->b[0] + 10;

    return s1;
}

//------------------------------------------
// f70 will takes a1, a2, a3, and produce a4
// a1: some constant
// a2: input array
// a3: some constant
// a4: output array
//------------------------------------------
DLLIMP int f70(int a1, int *a2, int a3, int *a4)
{
	int *v4; // ebx@1
	int v5; // ebp@1
	int v6; // edi@1
	int v7; // ecx@1
	signed int result; // eax@1
	int v9; // edx@1
	int *v10; // esi@2
	int v11; // eax@3
	int v12; // ecx@3
	int v13; // ebp@6
	int v14; // [sp+Ch] [bp-8h]@1
	int v15; // [sp+10h] [bp-4h]@1
	int a2a; // [sp+1Ch] [bp+8h]@1

	//printf("a1 %d\n", a1);
	//printf("*a2 %d\n", *a2);
	//printf("a3 %d\n", a3);
	//printf("*a4 %d\n", *a4);

	v4 = a2;
	v5 = a1;
	v6 = 0;
	v7 = a2[a1];
	v14 = a2[a1 - 1];
	result = 0;
	v9 = -1;
	a2[a1 - 1] = 10000;
	v15 = v7;
	a2[a1] = -10000;
	a2a = 0;
	if ( a1 > 0 )
	{
		v10 = a4;
		do
		{
			v11 = (int)&v4[v6++];
			*v10 = v11;
			v12 = (int)&v4[v6];
			if ( v9 * (*(int *)v11 - *(int *)v12) < a3 )
			{
				do
				{
					if ( v9 * *(int *)v12 > v9 * *(int *)*v10 )
						*v10 = v12;
					v13 = *(int *)(v12 + 4);
					v12 += 4;
					++v6;
				}
				while ( v9 * (*(int *)*v10 - v13) < a3 );
				v5 = a1;
			}
			++v10;
			v9 = -v9;
			result = a2a++ + 1;
		}
		while ( v6 < v5 );
	}
	if ( result % 2 )
		--result;
	v4[v5 - 1] = v14;
	v4[v5] = v15;
	return result;
}
