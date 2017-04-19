#include <iostream>

using namespace std;
//1,32,60,91,121,152,182,213,244,274,305,335;
//1,32,61,92,122,153,183,214,245,275,306,336;


int main()
{
	int i,j;
	int days=365;
	int count = 1;
	int total = 0;
	string w_days[7] = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
	string months[12] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
	
	for(i=0;i<100;i++)
	{
		if((1901+i)%4 == 0)
		{
			days = 366;
		}
		else
		{
			days = 365;
		}
		for(j=1;j<days;j++)
		{
			
			
			if (count == 7)count = 1;
			count++;
		}
		cout << days << endl;
	}
	cout << count << endl;
	cout << total;
	
	return 0;
}
