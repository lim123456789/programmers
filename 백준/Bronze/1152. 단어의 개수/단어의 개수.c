#include <stdio.h>
#include <string.h>

int main(){
	char arr[1000000];
	int i,cnt,len;
	
    scanf("%[^\n]",arr);
	
    len=strlen(arr);
 	
 	cnt=1;
 	
	 if(len==1){
 		if(arr[0]==' '){
 			printf("0\n");
 			return 0;
		 }	
	 }
	 
 	for(i = 1; i < len-1; i++)
    {
        if(arr[i] == ' '){
        	cnt++;
		}    
    }
	printf("%d\n",cnt);
 
    return 0;
    
}
