public class MultiplesOf3And5{
    public static void main(String[] args){
        System.out.println(sumMultiples(1000));
    }

    public static int sumMultiples(int end){
        int sum = 0;
        for (int num = 0; num < 1000; num++){
            if (((num % 3) == 0) || ((num % 5) == 0)){
                sum += num;
            }
        }

        return sum;
    }
}