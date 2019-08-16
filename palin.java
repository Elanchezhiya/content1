import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        StringBuffer c=new StringBuffer(A);
        
        if(A.equalsIgnoreCase(c.reverse().toString()))
        System.out.print("Yes");
        else
        System.out.print("No");
    }
}



