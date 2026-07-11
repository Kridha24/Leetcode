class Solution {
public:
    string intToRoman(int num) {
        vector<string>w = {"I", "X", "C", "M"};
        vector<string>w1 = {"V", "L", "D"};
        string ans = "";
        int p=0;
        while(num>0){
            int t = num%10;
            if(t==4||t==9){
                if(t==4)ans = w[p]+w1[p]+ans;
                else ans = w[p]+w[p+1]+ans;
            }else{
                if(t>=5){
                    for(int i=0;i<t-5;i++){
                    ans  = w[p] + ans;
                    }
                ans = w1[p]+ans;
                }else{
                    for(int i=0;i<t;i++){
                        ans  = w[p] + ans;
                    }
                }
            }
            p++;
            num/=10;
        }
        return ans;
    }
};