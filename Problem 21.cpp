#include <iostream>

using namespace std;





int main()
{
	int i,x;
	int total = 0;
	cin >> x;
	
	for(i=1;i<x;i++)
	{
		if(x%i == 0)
		{
			total += i;
		}
	}
	
	cout << total;
	
	return 0;
}
