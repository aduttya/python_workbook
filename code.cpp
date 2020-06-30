#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        long long int n,m;
        scanf("%lld",&n);
        scanf("%lld",&m);
        long long int arr[n];
        for(int i = 0; i < n; ++i)
            scanf("%lld",&arr[i]);
        int count = 0;
        int val = arr[n-1];
        for (int i = (n-1); i >= 0; i--){
            if(val == arr[i])
                val -= 1;
            else{
                count++;
                break;}}
        if(count != 0 && val == m)
            printf("%d\n",val);
        else{
            printf("%d\n","-1");}}

}