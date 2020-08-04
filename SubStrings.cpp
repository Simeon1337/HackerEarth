#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void transformers(string,int,int,int);
 
int main()
{
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
 
   int z,b,c;
   cin >> z >> b >>c;
   string a;
   cin >> a;
 
   transformers(a,z,b,c);
 
   return 0;
}

void transformers(string a,int n,int k, int m){
 
   int counter2 = 0;
   int allowed = m;
 
   for(int i = 0; i < k; i++){
      if(a[i] == '1' && allowed > 0){
         allowed--;
      }
      else if(a[i] == '1' && allowed == 0){
         a[i] = '0';
         counter2++;
      }
 
   }

   for(int i = 0; i < n-k; i++){
      
     
      if( a[i] == '1' && a[i+k] == '0' ){
         if(allowed < m){
            allowed++;
         }
      }
      else if(a[i] == '0' && a[i+k] == '1'){
 
         if(allowed > 0)
            allowed--;
            
         else if( allowed == 0){
            a[i+k] = '0';
            counter2++;
         }
      }
      
   }
   cout << counter2 << endl << a;
}