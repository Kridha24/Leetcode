class Solution {
public:
    int myAtoi(string s) {
        long res=0;
        int k=-1;
        bool isNumSeen=false;
        for(int i=0;s[i]!='\0';i++)
        {
            if(res==0 && k==-1 && !isNumSeen)
            {
                if(s[i]==' ')continue;
                if(s[i]=='-'||s[i]=='+')
                {
                    k=i;
                    isNumSeen=true;
                    continue;
                }
            }
            if(s[i]>='0'&&s[i]<='9')
            {
                isNumSeen=true;
                res=res*10+(s[i]-'0');
                if((k==-1 || s[k]=='+')&& res>INT_MAX) return INT_MAX;
                if(k!=-1 && s[k]=='-' && -res<INT_MIN) return INT_MIN;
            }
            else
            break;
        }
        if(k!=-1 && s[k]=='-')
        res*=-1;
        return res;
    }
};