import java.util.Scanner;
public class sat {
    public static void main(String[] args){
     int s;
     Scanner ss=new Scanner(System.in);
     s=ss.nextInt();
     if((s>=10)||(s<=99))
     {
         System.out.println("Saturated");
     }
     else 
     {
         System.out.println("Unsaturated");
     }
}
