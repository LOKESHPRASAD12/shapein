#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
       map<int,int>m;

        int n;
        cin>>n;
        int a[n];
        for(int i=0; i<n; i++){
            cin>>a[i];
            m[a[i]]++;

        }
        int ans=0;
       for(auto i:m){
         ans=max(ans,i.second);
       }
       cout<<n-ans<<endl;
    }
    return 0;
}