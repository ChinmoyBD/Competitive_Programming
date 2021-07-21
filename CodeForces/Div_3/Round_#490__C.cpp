#include <iostream>
using namespace std;

int main(){
    int n, k, i, ch;
    string st;
    
    cin>> n >> k;
    cin >> st;

    for(ch = 'a'; ch <= 'z'; ch++){
        if(k <= 0 || n == k)
            break;
        for(i = 0; i < n; i++){
            if(st[i] == ch){
                st[i] = ' ';
                k--;
            }
            if(k <= 0)
                break;
        }
    }
    n = n - k;
    for(i = 0; i < n; i++){
        if(st[i] != ' ')
            cout<< st[i];
    }
    cout<< endl;
}