#include <iostream>

using namespace std;

int main()
{
  int a;
  unsigned n,i,targetnum;
  unsigned int cntr = 0;
  unsigned int endnum = 0;
for(i=2;i<1000000;i++)
{
	n=i;
 while(n!=1)
 {
   if (n%2== 0)
   {
   	n=n/2;
   	cntr++;
   }
   else
   {
 	  n=3*n+1;
 	  cntr++;
   }
  if (n >= 4294967295)
  {
  	cin >> a;
  }
    
 }
  if (cntr > endnum)
   {
   	endnum = cntr;
   	targetnum = i;
   	cout << targetnum;
   }
 cntr = 0;

}
cout << endnum << endl;
cout << targetnum;
	return 0;
}
