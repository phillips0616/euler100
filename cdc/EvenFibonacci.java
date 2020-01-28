import java.util.ArrayList;

public class EvenFibonacci{
    public static void main (String[] args){
        ArrayList<Integer> myFib = new ArrayList<Integer>();
        int sum = 0;
        myFib = fibonacci(4000000);

        for (int num : myFib){
            if ((num % 2) == 0){
                sum += num;
            }
        }

        System.out.println(sum);
    }

    public static ArrayList<Integer> fibonacci(int end){
        ArrayList<Integer> fib = new ArrayList<Integer>();
        
        fib.add(1);
        fib.add(1);
        
        do{
            fib.add(fib.get(fib.size() - 1) + fib.get(fib.size() - 2));
        } while ((fib.get(fib.size() - 1) + fib.get(fib.size() - 2)) < end);
        
        return fib;
    }
}