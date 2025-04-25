//package Java.Questions.Other;



class GFG {
	static boolean isPrime(int n)
	{
		// Corner case
		if (n <= 1)
			return false;

		// Check from 2 to n-1
		for (int i = 2; i < n; i++)
			if (n % i == 0)
				return false;

		return true;
	}

	// Driver Program
	public static void main(String args[])
	{
		if (isPrime(10))
			System.out.println(" true");
		else
			System.out.println(" false");
		if (isPrime(5))
			System.out.println(" true");
		else
			System.out.println(" false");
	}
}
 /* Aditya */