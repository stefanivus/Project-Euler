#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<unsigned long int> find_primes(int limit)
{
	vector<unsigned long int> primes;
	primes.push_back(2);
	bool isPrime;
	for(unsigned long int i = 3;i < limit;i += 2)
	{
		isPrime = true;
		for(unsigned long int j = 1; j<primes.size(); j++)
		{
			if (j > sqrt(i))
			{
				break;
			}
			if(i%primes[j] == 0)
			{
				isPrime = false;
				break;
			}
		}
		if(isPrime)
		{
			primes.push_back(i);
		}
	}
	return primes;
}
vector<unsigned long int> primes = find_primes(1000000);

vector<unsigned long int> find_prime_factors(unsigned long int n)
{
	vector<unsigned long int> factors;
	if (n == 1)
	{
		factors.push_back(1);
		return factors;
	}
	unsigned long int i = 0;
	while (n > 1)
	{
		if (n%primes[i] == 0)
		{
			factors.push_back(primes[i]);
			n = n/primes[i];
		}
		else
		{
			i += 1;
		}
	}
	return factors;
}

unsigned long int rad(unsigned long int n)
{
	vector<unsigned long int> arr = find_prime_factors(n);
	unsigned long int p = 1;
	if (n == 1)
	{
		return 1;
	}
	for (int i = 0; i < arr.size();i++)
	{
		if(p%arr[i] != 0)
		{
		    p *= arr[i];
	    }
	}
	return p;
}

unsigned long int GCD(unsigned long int a, unsigned long int b)
{
	if (a == 1)
	{
		return 1;
	}
	bool check = false;
	if (b-a < 500)
	{
		while (a != b)
		{
			if (a > b)
			{
				a -= b;
			}
			else
			{
				b -= a;
			}
			if (abs(b-a) > 500)
	    	{
	    		check = true;
		    	break;
	    	}
		}
		if (check == false)
		{
		    return a;
		}
	}
	int i = 0;
	while(primes[i] < sqrt(a)+3)
	{
		if(a%primes[i] == 0)
		{
			if (b%primes[i] == 0)
			{
				return 2;
			}
		}
		i++;
	}
	return 1;
}

vector<unsigned long int> radicalize(int limit)
{
	vector<unsigned long int> radicals;
    unsigned long int c;
     for(c = 1; c<= limit; c++)
     {
        radicals.push_back(rad(c));
     }
     return radicals;
}


int find_sum_c(int limit)
{
	vector<unsigned long int> radicals = radicalize(limit);
	cout << "Radicals initialized" << endl;
	unsigned long int suma = 0;
	unsigned long long int p,q,r;
	unsigned int c,a,b;
	for(c = 3; c < limit;c++)
	{
		p = radicals[c-1];
		if (p < c)
		{
			b = c-1;
		    a = 1;
		    while(a<b)
	    	{
	    		q = p*radicals[b-1]*radicals[a-1];
		        if (q < c)
		        {
		        	if (GCD(a,b) == 1 && GCD(a,c) == 1 && GCD(b,c) == 1)
	                {
			            suma += c;
		            }
	            }
		        b--;
		        a++;
	    	}
	    }
    }   
	return suma;
}

int main()
{
	cout << "Primes initialized" << endl;
	cout << find_sum_c(120000);
	
	
	return 0;
}
