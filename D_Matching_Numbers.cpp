#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define Faster ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);



int main(){
    Faster;
    int t;                      cin>>t;
    while(t--){
        int n;                  cin>>n;
        if(n%2==0){
            cout<<"No"<<endl;
            continue;
        }
        
        cout<<"Yes"<<endl;
        int leftShift=(n+1)/2,rightShift=-n+leftShift;

        int left=1,right=n+leftShift;
        bool switched=true;
        int cnt=0;
        while(cnt<n){
            cout<<left<<" "<<right<<endl;
            cnt++;
            if(switched){
                left+=leftShift;
                right+=rightShift;
            }
            else{
                left+=rightShift;
                right+=leftShift;
            }
            switched^=true;
        }
    }
    return 0;
}
