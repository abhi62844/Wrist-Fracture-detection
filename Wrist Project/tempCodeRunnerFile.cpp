#include<bits/stdc++.h>
using namespace std;
 int mySqrt(int x) {
        unsigned long long int l=0,r=x/2,k=x;
        if(x==0 || x==1) return x;
        while(r*r>k){
             cout<<r<<" "<<endl;
             r=r/2;
        }
        cout<<r;
        while(r*r<=k){
            r++;
        }
        return r-1;
    }
int main()
{
  mySqrt(2147395599);
            return 0;
}