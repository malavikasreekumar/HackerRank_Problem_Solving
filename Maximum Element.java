import java.io.*;
import java.util.*;

public class Solution {


    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Stack<Integer>stack=new Stack<Integer>();
        Stack<Integer>MaxStack=new Stack<Integer>();

        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        for(int i=0;i<n;i++)
        {
            int query=scan.nextInt();
            switch (query) {
                case 1:
            int x = scan.nextInt();
            stack.push(x);
            if (MaxStack.isEmpty()|| x>=MaxStack.peek())
            {
                MaxStack.push(x);
            }
            break;
        
            case 2:
            int poppedValue=stack.pop();
              if (poppedValue == MaxStack.peek()) {
                        MaxStack.pop();
                    }
                    break;
                case 3:
                    System.out.println(MaxStack.peek());
                    break;
                default:
                    break;
            }
        }        
        scan.close();
    }
}



   
    
 

